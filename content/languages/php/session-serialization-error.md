---
title: "[Solution] PHP Session unserialize() — Corrupted Session Data"
description: "Fix PHP session unserialize() failures from corrupted data and serializer mismatches. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 223
---

# PHP Session unserialize() — Corrupted Session Data

Session deserialization errors occur when PHP cannot parse session data stored in files or databases. This happens due to corrupted session files, serializer mismatches, PHP version upgrades changing serialization formats, or unauthorized session data modification.

## Common Causes

```php
// Corrupted session file content
// File contains: user_id|s:5:"admin";corrupt_data
// unserialize() fails or returns false
session_start();
// Warning: SessionHandler::read(): open_basedir restriction in effect
```

```php
// PHP serializer changed between versions
// Session saved with PHP 7.x, read with PHP 8.x
// Different internal representation of objects
session_start();
```

```php
// Session data modified directly in database
// Manual edit broke serialization format
// Example: user_id|i:42; -> user_id|i:42,extra
```

```php
// Incorrect session.serialize_handler setting
// PHP < 7.1: php default serializer
// PHP 7.1+: supports php_serialize by default
ini_set('session.serialize_handler', 'php');
session_start(); // Mismatch with stored format
```

```php
// Binary data in session causes encoding issues
// Session file contains corrupted bytes
// unserialize() returns false
```

## How to Fix

### Fix 1: Check Session Serializer Compatibility

```php
// Verify current serializer
$handler = ini_get('session.serialize_handler');
error_log("Current session serializer: $handler");

// php: name|s:5:"value"; (default before PHP 7.1)
// php_serialize: a:1:{s:4:"name";s:5:"value";}
// igbinary: binary format

// Match the serializer to your stored session format
ini_set('session.serialize_handler', 'php');
```

### Fix 2: Use session_set_save_handler() for Custom Validation

```php
class ValidatingSessionHandler implements SessionHandlerInterface
{
    public function read(string $id): string|false
    {
        $path = session_save_path() . '/sess_' . $id;

        if (!file_exists($path)) {
            return '';
        }

        $data = file_get_contents($path);

        if ($data === false) {
            error_log("Cannot read session file: $path");
            return '';
        }

        // Validate data can be unserialized
        $unserialized = @unserialize($data);
        if ($unserialized === false && $data !== 'b:0;') {
            error_log("Corrupted session data for ID: $id");
            // Return empty string to start fresh
            return '';
        }

        return $data;
    }

    // Implement other SessionHandlerInterface methods...
    public function open(string $path, string $name): bool { return true; }
    public function close(): bool { return true; }
    public function write(string $id, string $data): bool { return true; }
    public function destroy(string $id): bool { return true; }
    public function gc(int $max_lifetime): int|false { return 0; }
}
```

### Fix 3: Handle Corrupted Sessions Gracefully

```php
function startSafeSession(): void
{
    if (session_status() === PHP_SESSION_ACTIVE) {
        return;
    }

    // Store original error handler to restore later
    $originalHandler = set_error_handler(function ($errno, $errstr) {
        return true; // Suppress session errors
    });

    session_start();
    restore_error_handler();

    // Check if session data is valid
    if (isset($_SESSION['_corrupted']) || session_status() !== PHP_SESSION_ACTIVE) {
        // Session is corrupted, start fresh
        session_regenerate_id(true);
        $_SESSION = [];
        $_SESSION['_fresh_start'] = true;
    }
}

startSafeSession();
```

### Fix 4: Migrate Sessions Between PHP Versions

```php
function migrateSessionData(array $oldData): array
{
    // Handle objects that changed between PHP versions
    $migrated = [];

    foreach ($oldData as $key => $value) {
        if (is_object($value)) {
            // Reconstruct object with current PHP version
            $className = get_class($value);
            if (class_exists($className)) {
                $migrated[$key] = new $className();
                // Copy properties manually if needed
            } else {
                error_log("Class $className not found, skipping migration");
                continue;
            }
        } else {
            $migrated[$key] = $value;
        }
    }

    return $migrated;
}
```

### Fix 5: Prevent Session Tampering

```php
function startSignedSession(string $secretKey): void
{
    if (session_status() === PHP_SESSION_NONE) {
        session_start();
    }

    // Check if session was tampered with
    if (isset($_SESSION['_signature'])) {
        $expectedSig = hash_hmac('sha256', serialize($_SESSION['_data']), $secretKey);
        if (!hash_equals($expectedSig, $_SESSION['_signature'])) {
            error_log("Session tampering detected");
            $_SESSION = [];
            session_regenerate_id(true);
        }
    }
}

function saveSignedSession(array $data, string $secretKey): void
{
    $_SESSION['_data'] = $data;
    $_SESSION['_signature'] = hash_hmac('sha256', serialize($data), $secretKey);
}
```

## Examples

```php
// Database session handler with corruption protection
class DatabaseSessionHandler implements SessionHandlerInterface
{
    private PDO $db;

    public function __construct(PDO $db)
    {
        $this->db = $db;
    }

    public function read(string $id): string|false
    {
        $stmt = $this->db->prepare("SELECT data FROM sessions WHERE id = ?");
        $stmt->execute([$id]);
        $data = $stmt->fetchColumn();

        if ($data === false) {
            return '';
        }

        // Validate serialization
        $test = @unserialize($data);
        if ($test === false && $data !== 'b:0;') {
            error_log("Corrupted session in database: $id");
            return '';
        }

        return $data;
    }

    public function write(string $id, string $data): bool
    {
        // Validate before writing
        $test = @unserialize($data);
        if ($test === false && $data !== 'b:0;') {
            error_log("Refusing to write corrupted session data: $id");
            return false;
        }

        $stmt = $this->db->prepare("
            INSERT INTO sessions (id, data, last_access)
            VALUES (?, ?, NOW())
            ON DUPLICATE KEY UPDATE data = VALUES(data), last_access = NOW()
        ");
        return $stmt->execute([$id, $data]);
    }

    // Implement other SessionHandlerInterface methods...
    public function open(string $path, string $name): bool { return true; }
    public function close(): bool { return true; }
    public function destroy(string $id): bool { return true; }
    public function gc(int $max_lifetime): int|false { return 0; }
}
```

## Related Errors

- [session-start-error.md](/content/languages/php/session-start-error.md) — PHP session_start() failure
- [session-save-path-error.md](/content/languages/php/session-save-path-error.md) — Session save path issues
- [json-decode-error.md](/content/languages/php/json-decode-error.md) — JSON decode failures
- [warning-session-save-path.md](/content/languages/php/warning-session-save-path.md) — Session save path warning
