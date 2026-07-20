---
title: "[Solution] PHP session_destroy() — Cannot Destroy Session"
description: "Fix PHP session_destroy() failures. Check session status, close session first, handle output buffering. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 221
---

# PHP session_destroy() — Cannot Destroy Session

The `session_destroy()` function fails when the session is not active, output buffering interferes with session data, or the session file cannot be removed from storage. This typically happens during logout or cleanup routines.

## Common Causes

```php
// Session not started before destroying
session_destroy();
// Warning: session_destroy(): Session is not active
```

```php
// Session data not properly registered
$_SESSION['user'] = null;
session_destroy();
// Session data may persist if not cleared properly
```

```php
// Output buffering active during destroy
ob_start();
$_SESSION['data'] = 'value';
session_destroy();
// ob_start prevents session data from being written properly
```

```php
// Attempting to destroy session without clearing superglobal
session_destroy();
// $_SESSION still contains old data in current request
```

```php
// Session save path not writable
session_destroy();
// Returns false if session file cannot be deleted
```

## How to Fix

### Fix 1: Check Session Status Before Destroying

```php
if (session_status() === PHP_SESSION_ACTIVE) {
    session_destroy();
} else {
    // Session was not started, nothing to destroy
    error_log("Attempted to destroy inactive session");
}
```

### Fix 2: Clear Session Data and Unset Superglobal

```php
function destroySession(): bool
{
    if (session_status() !== PHP_SESSION_ACTIVE) {
        return false;
    }

    // Clear all session data
    $_SESSION = [];

    // Delete the session cookie if it exists
    if (ini_get("session.use_cookies")) {
        $params = session_get_cookie_params();
        setcookie(
            session_name(),
            '',
            time() - 42000,
            $params["path"],
            $params["domain"],
            $params["secure"],
            $params["httponly"]
        );
    }

    // Destroy the session
    return session_destroy();
}

destroySession();
```

### Fix 3: Handle Output Buffering

```php
function safeSessionDestroy(): bool
{
    if (session_status() !== PHP_SESSION_ACTIVE) {
        return false;
    }

    // Flush output buffers to ensure session data is written
    while (ob_get_level() > 0) {
        ob_end_flush();
    }

    $_SESSION = [];
    return session_destroy();
}
```

### Fix 4: Use Session Save Handler for Custom Cleanup

```php
class DatabaseSessionHandler implements SessionHandlerInterface
{
    private PDO $db;

    public function __construct(PDO $db)
    {
        $this->db = $db;
    }

    public function destroy(string $id): bool
    {
        $stmt = $this->db->prepare("DELETE FROM sessions WHERE id = ?");
        $result = $stmt->execute([$id]);
        return $result && $stmt->rowCount() > 0;
    }

    // Implement other SessionHandlerInterface methods...
    public function open(string $path, string $name): bool { return true; }
    public function close(): bool { return true; }
    public function read(string $id): string|false { return ''; }
    public function write(string $id, string $data): bool { return true; }
    public function gc(int $max_lifetime): int|false { return 0; }
}
```

### Fix 5: Complete Logout With Error Handling

```php
function logout(): void
{
    if (session_status() === PHP_SESSION_NONE) {
        session_start();
    }

    if (session_status() !== PHP_SESSION_ACTIVE) {
        return;
    }

    // Unset all session variables
    $_SESSION = [];

    // Destroy the session
    $destroyed = session_destroy();

    if (!$destroyed) {
        error_log("Failed to destroy session");
    }

    // Regenerate a fresh session if needed
    if (session_status() === PHP_SESSION_NONE) {
        session_start();
    }
}

logout();
```

## Examples

```php
// Secure logout implementation
function secureLogout(): void
{
    if (session_status() === PHP_SESSION_NONE) {
        session_start();
    }

    // Regenerate to invalidate old session
    session_regenerate_id(true);

    // Clear session data
    $_SESSION = [];

    // Remove session cookie
    if (ini_get("session.use_cookies")) {
        $params = session_get_cookie_params();
        setcookie(
            session_name(),
            '',
            time() - 42000,
            $params["path"],
            $params["domain"],
            $params["secure"],
            $params["httponly"]
        );
    }

    // Destroy session
    session_destroy();

    // Destroy and clear old session
    @unlink(session_save_path() . '/sess_' . session_id());
}
```

```php
// AJAX logout with proper error handling
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['action'])) {
    if ($_POST['action'] === 'logout') {
        if (session_status() === PHP_SESSION_ACTIVE) {
            $_SESSION = [];
            session_destroy();
            header('Content-Type: application/json');
            echo json_encode(['success' => true]);
        } else {
            header('Content-Type: application/json');
            http_response_code(400);
            echo json_encode(['success' => false, 'error' => 'No active session']);
        }
        exit;
    }
}
```

## Related Errors

- [session-start-error.md](/content/languages/php/session-start-error.md) — PHP session_start() failure
- [session-regenerate-id-error.md](/content/languages/php/session-regenerate-id-error.md) — PHP session_regenerate_id() failure
- [session-write-close-error.md](/content/languages/php/session-write-close-error.md) — PHP session_write_close() issues
- [session-save-path-error.md](/content/languages/php/session-save-path-error.md) — Session save path issues
