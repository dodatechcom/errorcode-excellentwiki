---
title: "[Solution] PHP Warning: session_start() — open_basedir restriction"
description: "Fix PHP Warning: session_start() open_basedir restriction. Configure session.save_path, check open_basedir, set correct permissions."
languages: ["php"]
severities: ["warning"]
error-types: ["runtime-error"]
weight: 115
---

# PHP Warning: session_start() — open_basedir restriction

This warning means PHP cannot write session files because the session save path is outside the `open_basedir` restriction or the directory does not exist. The `open_basedir` directive limits file access to specified directories for security.

## Common Causes

```php
// Cause 1: session.save_path outside open_basedir
<?php
// php.ini: open_basedir = /var/www/html
// php.ini: session.save_path = /tmp
// /tmp is not within /var/www/html
session_start();
// Warning: session_start(): open_basedir restriction in effect
?>
```

```php
// Cause 2: Session directory does not exist
<?php
ini_set('session.save_path', '/var/lib/php/sessions/nonexistent');
session_start();
// Warning: cannot create directory
?>
```

```php
// Cause 3: Insufficient permissions on session directory
<?php
// Session directory owned by root, web server cannot write
session_start();
// Warning: Permission denied
?>
```

```php
// Cause 4: open_basedir not configured for session path
<?php
// /etc/php/8.1/fpm/php.ini has open_basedir = /var/www
// But sessions are stored in /var/lib/php/sessions
session_start();
?>
```

## How to Fix

### Fix 1: Configure session.save_path Correctly

Set the session save path to a location within the `open_basedir` restriction.

```php
<?php
// Option A: Set session.save_path in php.ini
// session.save_path = /var/www/html/sessions

// Option B: Set at runtime
$sessionPath = __DIR__ . '/sessions';

if (!is_dir($sessionPath)) {
    mkdir($sessionPath, 0700, true);
}

ini_set('session.save_path', $sessionPath);
session_start();
echo "Session started at: " . session_save_path();
?>
```

### Fix 2: Check and Configure open_basedir

Ensure `open_basedir` includes the session save path.

```php
<?php
// Check current open_basedir setting
$openBasedir = ini_get('open_basedir');
$sessionPath = session_save_path();

echo "open_basedir: {$openBasedir}\n";
echo "Session path: {$sessionPath}\n";

// Verify session path is within open_basedir
if ($openBasedir !== '') {
    $allowed = explode(':', $openBasedir);
    $isAllowed = false;

    foreach ($allowed as $path) {
        if (str_starts_with(realpath($sessionPath) ?: '', rtrim($path, '/'))) {
            $isAllowed = true;
            break;
        }
    }

    if (!$isAllowed) {
        echo "Session path is NOT within open_basedir\n";
        echo "Add '{$sessionPath}' to open_basedir in php.ini\n";
    }
}
?>
```

### Fix 3: Set Correct Directory Permissions

Ensure the web server process can write to the session directory.

```bash
# Check current session save path
php -r "echo ini_get('session.save_path');"

# Create directory if it doesn't exist
sudo mkdir -p /var/lib/php/sessions

# Set ownership to web server user
sudo chown www-data:www-data /var/lib/php/sessions

# Set correct permissions
sudo chmod 733 /var/lib/php/sessions

# Verify permissions
ls -la /var/lib/php/sessions
```

```php
<?php
// Verify session directory is writable
$sessionPath = session_save_path();

if (!is_dir($sessionPath)) {
    mkdir($sessionPath, 0733, true);
}

if (!is_writable($sessionPath)) {
    chmod($sessionPath, 0733);
}

if (!is_writable($sessionPath)) {
    die("Session directory is not writable: {$sessionPath}");
}

session_start();
echo "Session started successfully";
?>
```

### Fix 4: Use a Custom Session Handler for Restricted Environments

When the filesystem is restricted, use a custom session handler.

```php
<?php
class DatabaseSessionHandler implements SessionHandlerInterface
{
    private \PDO $pdo;

    public function __construct(\PDO $pdo)
    {
        $this->pdo = $pdo;
    }

    public function open(string $path, string $name): bool
    {
        return true;
    }

    public function close(): bool
    {
        return true;
    }

    public function read(string $id): string|false
    {
        $stmt = $this->pdo->prepare("SELECT data FROM sessions WHERE id = :id");
        $stmt->execute([':id' => $id]);
        $row = $stmt->fetch();
        return $row ? $row['data'] : '';
    }

    public function write(string $id, string $data): bool
    {
        $stmt = $this->pdo->prepare(
            "INSERT INTO sessions (id, data, updated_at) VALUES (:id, :data, NOW())
             ON DUPLICATE KEY UPDATE data = :data2, updated_at = NOW()"
        );
        return $stmt->execute([':id' => $id, ':data' => $data, ':data2' => $data]);
    }

    public function destroy(string $id): bool
    {
        $stmt = $this->pdo->prepare("DELETE FROM sessions WHERE id = :id");
        return $stmt->execute([':id' => $id]);
    }

    public function gc(int $max_lifetime): int|false
    {
        $stmt = $this->pdo->prepare(
            "DELETE FROM sessions WHERE updated_at < DATE_SUB(NOW(), INTERVAL :lifetime SECOND)"
        );
        $stmt->execute([':lifetime' => $max_lifetime]);
        return $stmt->rowCount();
    }
}

// Usage
$pdo = new PDO("mysql:host=localhost;dbname=mydb", "user", "pass");
$handler = new DatabaseSessionHandler($pdo);
session_set_save_handler($handler, true);
session_start();
echo "Session started via database handler";
?>
```

## Examples

```php
<?php
// Complete session initialization with path validation
function initSession(): void
{
    $sessionPath = sys_get_temp_dir();

    if (!is_dir($sessionPath)) {
        mkdir($sessionPath, 0700, true);
    }

    ini_set('session.save_path', $sessionPath);
    ini_set('session.use_strict_mode', 1);
    ini_set('session.cookie_httponly', 1);
    ini_set('session.cookie_secure', isset($_SERVER['HTTPS']) ? 1 : 0);
    ini_set('session.cookie_samesite', 'Lax');
    ini_set('session.gc_maxlifetime', 3600);

    session_start();

    if (session_status() !== PHP_SESSION_ACTIVE) {
        throw new \RuntimeException("Failed to start session");
    }
}

try {
    initSession();
    $_SESSION['user'] = 'Alice';
    echo "Session ID: " . session_id();
} catch (\RuntimeException $e) {
    echo "Session error: " . $e->getMessage();
}
?>
```

## Related Errors

- [PHP Warning: session_start() Error](/languages/php/session-start-error)
- [PHP Session Save Path Error](/languages/php/session-save-path-error)
- [PHP Warning: ini_set() Restricted](/languages/php/warning-ini-set-restricted)
