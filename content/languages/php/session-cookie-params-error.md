---
title: "[Solution] PHP session_set_cookie_params() — Invalid Configuration"
description: "Fix PHP session_set_cookie_params() invalid parameter errors. Validate settings and use array syntax. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 224
---

# PHP session_set_cookie_params() — Invalid Configuration

The `session_set_cookie_params()` function fails when invalid parameters are passed or when the configuration conflicts with PHP settings. Issues include invalid expiry values, path problems, and deprecated function signatures in older PHP versions.

## Common Causes

```php
// Negative expiry value
session_set_cookie_params(-3600); // Invalid: negative lifetime
session_start(); // Session cookie not set properly
```

```php
// Deprecated function signature (PHP < 7.3)
session_set_cookie_params(3600, "/path", ".example.com", true, true);
// PHP 7.3+: Use array syntax instead
```

```php
// Empty domain value causes browser rejection
session_set_cookie_params([
    'lifetime' => 3600,
    'path' => '/',
    'domain' => '', // Empty domain may cause issues
    'secure' => false,
    'httponly' => false,
]);
session_start();
```

```php
// Setting cookie params after session already started
session_start();
session_set_cookie_params(3600); // Too late, session already started
```

```php
// Mismatched SameSite values
session_set_cookie_params([
    'lifetime' => 3600,
    'path' => '/',
    'domain' => '.example.com',
    'secure' => true,
    'httponly' => true,
    'samesite' => 'Strict',
]);
// If PHP < 7.3, 'samesite' is not recognized
```

## How to Fix

### Fix 1: Use Array Syntax (PHP 7.3+)

```php
session_set_cookie_params([
    'lifetime' => 3600,        // 1 hour
    'path' => '/',
    'domain' => '.example.com',
    'secure' => true,
    'httponly' => true,
    'samesite' => 'Lax',
]);
session_start();
```

### Fix 2: Validate Parameters Before Setting

```php
function configureSessionCookie(array $params): bool
{
    $defaults = [
        'lifetime' => 3600,
        'path' => '/',
        'domain' => '',
        'secure' => false,
        'httponly' => true,
        'samesite' => 'Lax',
    ];

    $params = array_merge($defaults, $params);

    // Validate lifetime
    if ($params['lifetime'] < 0) {
        $params['lifetime'] = 0;
    }

    // Validate samesite
    $validSameSite = ['Strict', 'Lax', 'None'];
    if (!in_array($params['samesite'], $validSameSite, true)) {
        $params['samesite'] = 'Lax';
    }

    // Validate secure + None combination
    if ($params['samesite'] === 'None' && !$params['secure']) {
        $params['secure'] = true;
    }

    session_set_cookie_params($params);
    return true;
}

configureSessionCookie([
    'lifetime' => 7200,
    'secure' => true,
    'httponly' => true,
]);
session_start();
```

### Fix 3: Set Cookie Params Before session_start()

```php
// WRONG: After session_start
// session_start();
// session_set_cookie_params([...]);

// CORRECT: Before session_start
session_set_cookie_params([
    'lifetime' => 3600,
    'path' => '/',
    'domain' => $_SERVER['HTTP_HOST'],
    'secure' => isset($_SERVER['HTTPS']),
    'httponly' => true,
    'samesite' => 'Lax',
]);
session_start();
```

### Fix 4: Handle PHP Version Differences

```php
function safeSetCookieParams(array $params): void
{
    $params = array_merge([
        'lifetime' => 3600,
        'path' => '/',
        'domain' => '',
        'secure' => false,
        'httponly' => false,
    ], $params);

    if (PHP_VERSION_ID >= 70300) {
        // PHP 7.3+: Use array syntax with samesite
        session_set_cookie_params($params);
    } else {
        // PHP < 7.3: Use legacy function signature
        session_set_cookie_params(
            $params['lifetime'],
            $params['path'],
            $params['domain'],
            $params['secure'],
            $params['httponly']
        );
    }
}

safeSetCookieParams([
    'lifetime' => 3600,
    'secure' => true,
    'httponly' => true,
]);
session_start();
```

### Fix 5: Validate Domain and Path

```php
function configureSecureSession(): void
{
    $domain = $_SERVER['HTTP_HOST'] ?? '';
    $domain = preg_replace('/:\d+$/', '', $domain); // Remove port
    $domain = ltrim($domain, '.'); // Remove leading dot

    session_set_cookie_params([
        'lifetime' => 3600,
        'path' => '/',
        'domain' => $domain,
        'secure' => isset($_SERVER['HTTPS']) && $_SERVER['HTTPS'] === 'on',
        'httponly' => true,
        'samesite' => 'Lax',
    ]);

    session_start();
}

configureSecureSession();
```

## Examples

```php
// Production-ready session configuration
function initProductionSession(): void
{
    $isSecure = isset($_SERVER['HTTPS']) && $_SERVER['HTTPS'] !== 'off';

    $params = [
        'lifetime' => (int) ini_get('session.cookie_lifetime') ?: 3600,
        'path' => ini_get('session.cookie_path') ?: '/',
        'domain' => ini_get('session.cookie_domain') ?: '',
        'secure' => $isSecure,
        'httponly' => (bool) ini_get('session.cookie_httponly'),
        'samesite' => 'Lax',
    ];

    session_set_cookie_params($params);
    session_name('MYAPP_SESSION');
    session_start();
}

initProductionSession();
```

```php
// Environment-based configuration
function getCookieParams(): array
{
    $env = getenv('APP_ENV') ?: 'production';

    $base = [
        'path' => '/',
        'httponly' => true,
        'samesite' => 'Lax',
    ];

    switch ($env) {
        case 'development':
            return array_merge($base, [
                'lifetime' => 86400,
                'domain' => 'localhost',
                'secure' => false,
            ]);

        case 'staging':
            return array_merge($base, [
                'lifetime' => 7200,
                'domain' => '.staging.example.com',
                'secure' => true,
            ]);

        case 'production':
        default:
            return array_merge($base, [
                'lifetime' => 3600,
                'domain' => '.example.com',
                'secure' => true,
            ]);
    }
}

session_set_cookie_params(getCookieParams());
session_start();
```

## Related Errors

- [session-start-error.md](/content/languages/php/session-start-error.md) — PHP session_start() failure
- [session-save-path-error.md](/content/languages/php/session-save-path-error.md) — Session save path issues
- [headers-sent.md](/content/languages/php/headers-sent.md) — Cannot send headers after output
- [warning-ini-set-restricted.md](/content/languages/php/warning-ini-set-restricted.md) — INI set restricted warning
