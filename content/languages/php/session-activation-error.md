---
title: "[Solution] PHP Session Fixation — Anti-Fixation Issues"
description: "Fix PHP session fixation vulnerabilities. Use session_regenerate_id(), strict mode, and session ID validation. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 225
---

# PHP Session Fixation — Anti-Fixation Issues

Session fixation occurs when an attacker can set or predict a user's session ID before authentication. Without proper anti-fixation measures—such as regenerating IDs on login, enforcing strict mode, and validating session IDs—your application is vulnerable to session hijacking.

## Common Causes

```php
// Not regenerating session ID on login
session_start();
if (verifyCredentials($_POST['username'], $_POST['password'])) {
    $_SESSION['user_id'] = $userId;
    // Attacker can keep original session ID
}
```

```php
// Session ID from URL is accepted
// example.com/index.php?PHPSESSID=attacker_known_id
session_start(); // Uses attacker-provided session ID
```

```php
// session.use_strict_mode disabled
ini_set('session.use_strict_mode', '0');
// PHP accepts any session ID, including forged ones
```

```php
// Session ID not validated
$sessionId = $_GET['session_id'] ?? '';
session_id($sessionId); // Attacker sets arbitrary session ID
session_start();
```

```php
// Predictable session ID generation
// Using weak entropy for session ID
ini_set('session.sid_length', '26'); // Too short
ini_set('session.sid_bits_per_character', '6'); // Low entropy
```

## How to Fix

### Fix 1: Regenerate Session ID on Login

```php
function login(string $username, string $password): bool
{
    if (!verifyCredentials($username, $password)) {
        return false;
    }

    // Regenerate session ID to prevent fixation
    if (session_status() === PHP_SESSION_NONE) {
        session_start();
    }

    session_regenerate_id(true);

    $_SESSION['user_id'] = getUser($username)->id;
    $_SESSION['logged_in'] = true;
    $_SESSION['login_time'] = time();

    return true;
}
```

### Fix 2: Enable Session Strict Mode

```php
// In php.ini or at runtime before session_start()
ini_set('session.use_strict_mode', '1');
ini_set('session.use_only_cookies', '1');
ini_set('session.use_trans_sid', '0');

session_start();
```

### Fix 3: Validate Session IDs

```php
function isValidSessionId(string $id): bool
{
    // Check length
    if (strlen($id) < 22 || strlen($id) > 256) {
        return false;
    }

    // Check character set (hex + dash)
    if (!preg_match('/^[a-f0-9\-]+$/', $id)) {
        return false;
    }

    // Check entropy (not all same character)
    $uniqueChars = count(array_unique(str_split($id)));
    if ($uniqueChars < 5) {
        return false;
    }

    return true;
}

function safeSessionStart(): void
{
    if (session_status() !== PHP_SESSION_NONE) {
        return;
    }

    // Reject invalid session IDs before starting
    if (isset($_COOKIE[session_name()])) {
        $id = $_COOKIE[session_name()];
        if (!isValidSessionId($id)) {
            // Delete invalid cookie and start fresh
            setcookie(session_name(), '', time() - 42000, '/');
            session_id('');
        }
    }

    session_start();
}
```

### Fix 4: Use Custom Session ID Generator

```php
function generateSecureSessionId(): string
{
    // Use cryptographically secure random bytes
    return bin2hex(random_bytes(32));
}

// Register custom ID validator (PHP 7.1+)
session_set_save_handler([
    'open' => function ($path, $name) { return true; },
    'close' => function () { return true; },
    'read' => function ($id) { return ''; },
    'write' => function ($id, $data) { return true; },
    'destroy' => function ($id) { return true; },
    'gc' => function ($max_lifetime) { return 0; },
    'create_sid' => function () {
        return generateSecureSessionId();
    },
]);
```

### Fix 5: Complete Anti-Fixation Middleware

```php
class SessionSecurity
{
    public static function init(): void
    {
        // Set secure defaults before session_start
        ini_set('session.use_strict_mode', '1');
        ini_set('session.use_only_cookies', '1');
        ini_set('session.use_trans_sid', '0');
        ini_set('session.cookie_httponly', '1');
        ini_set('session.cookie_secure', '1');
        ini_set('session.cookie_samesite', 'Lax');

        session_set_cookie_params([
            'lifetime' => 3600,
            'path' => '/',
            'domain' => '',
            'secure' => true,
            'httponly' => true,
            'samesite' => 'Lax',
        ]);

        session_start();

        // Validate session on every request
        self::validateSession();
    }

    private static function validateSession(): void
    {
        // Check if session was recently created
        if (!isset($_SESSION['_created'])) {
            $_SESSION['_created'] = time();
            $_SESSION['_fingerprint'] = self::getClientFingerprint();
            return;
        }

        // Validate fingerprint
        $currentFingerprint = self::getClientFingerprint();
        if (hash_equals($_SESSION['_fingerprint'] ?? '', $currentFingerprint) === false) {
            // Fingerprint mismatch - possible session hijacking
            session_unset();
            session_destroy();
            session_start();
            $_SESSION = ['_security_reset' => true];
        }

        // Timeout old sessions
        if (time() - $_SESSION['_created'] > 1800) {
            session_regenerate_id(true);
            $_SESSION['_created'] = time();
        }
    }

    private static function getClientFingerprint(): string
    {
        $data = ($_SERVER['HTTP_USER_AGENT'] ?? '')
              . ($_SERVER['HTTP_ACCEPT_LANGUAGE'] ?? '');
        return hash('sha256', $data);
    }

    public static function onLogin(): void
    {
        session_regenerate_id(true);
        $_SESSION['_created'] = time();
        $_SESSION['_fingerprint'] = self::getClientFingerprint();
    }
}

// Initialize session security
SessionSecurity::init();

// On successful login
if (attemptLogin($_POST['username'], $_POST['password'])) {
    SessionSecurity::onLogin();
    $_SESSION['user_id'] = getUser($_POST['username'])->id;
}
```

## Examples

```php
// Minimal anti-fixation login
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    session_start();

    if (verifyLogin($_POST['username'], $_POST['password'])) {
        // Regenerate to prevent fixation
        session_regenerate_id(true);
        $_SESSION['user_id'] = getUser($_POST['username'])->id;
        header('Location: /dashboard');
        exit;
    }
}
```

```php
// Session security configuration file
// config/session.php
return [
    'use_strict_mode' => '1',
    'use_only_cookies' => '1',
    'use_trans_sid' => '0',
    'cookie_lifetime' => '3600',
    'cookie_httponly' => '1',
    'cookie_secure' => '1',
    'cookie_samesite' => 'Lax',
    'sid_length' => '128',
    'sid_bits_per_character' => '6',
];
```

## Related Errors

- [session-start-error.md](/content/languages/php/session-start-error.md) — PHP session_start() failure
- [session-regenerate-id-error.md](/content/languages/php/session-regenerate-id-error.md) — PHP session_regenerate_id() failure
- [session-destroy-error.md](/content/languages/php/session-destroy-error.md) — PHP session_destroy() failure
- [warning-ini-set-restricted.md](/content/languages/php/warning-ini-set-restricted.md) — INI set restricted warning
