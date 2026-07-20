---
title: "[Solution] PHP session_write_close() — Output Buffering Conflicts"
description: "Fix PHP session_write_close() issues including output buffering conflicts and session locking. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 222
---

# PHP session_write_close() — Output Buffering Conflicts

The `session_write_close()` function manually ends the session and flushes session data to storage. Issues arise when output buffering interferes, when session data is modified after closing, or when session locking creates bottlenecks in concurrent requests.

## Common Causes

```php
// Modifying session data after session_write_close()
session_start();
session_write_close();
$_SESSION['key'] = 'value'; // Data may not persist
```

```php
// Output buffering prevents session data from being flushed
ob_start();
session_start();
// Session data stuck in output buffer
session_write_close();
```

```php
// Not calling session_write_close() causes long locks
// In long-running scripts without explicit close
for ($i = 0; $i < 1000; $i++) {
    // Processing continues while session file remains locked
}
session_write_close(); // Called too late
```

```php
// Double close causes errors
session_start();
session_write_close();
session_write_close(); // Warning or error on second call
```

```php
// AJAX requests causing session deadlocks
// Each request holds session lock until script ends
// Without session_write_close(), queue builds up
```

## How to Fix

### Fix 1: Set Session Data Before Closing

```php
session_start();

// Set all session data first
$_SESSION['user_id'] = 42;
$_SESSION['last_activity'] = time();
$_SESSION['cart'] = ['item1', 'item2'];

// Now close the session for the rest of the script
session_write_close();

// These changes will NOT be saved
// $_SESSION['late_change'] = 'lost';
```

### Fix 2: Handle Output Buffering Properly

```php
session_start();

// Flush any output buffers before closing session
while (ob_get_level() > 0) {
    ob_end_flush();
}

$_SESSION['data'] = 'value';
session_write_close();
```

### Fix 3: Use Early Close for Long-Running Scripts

```php
session_start();

// Load session data
$user = $_SESSION['user'];

// Save what needs saving
$_SESSION['last_access'] = time();

// Close session early - release the lock
session_write_close();

// Now do expensive operations without holding the lock
$result = performHeavyComputation($user);
sendNotifications($result);

// Cannot modify $_SESSION after this point
```

### Fix 4: Prevent Double Close

```php
function safeSessionClose(): void
{
    if (session_status() === PHP_SESSION_ACTIVE) {
        session_write_close();
    }
}

// Use this helper throughout the script
safeSessionClose();
safeSessionClose(); // Safe to call multiple times
```

### Fix 5: Use Database Sessions for Concurrent Access

```php
class DatabaseSessionHandler implements SessionHandlerInterface
{
    private PDO $db;

    public function __construct(PDO $db)
    {
        $this->db = $db;
    }

    public function write(string $id, string $data): bool
    {
        $stmt = $this->db->prepare("
            INSERT INTO sessions (id, data, last_access)
            VALUES (?, ?, NOW())
            ON DUPLICATE KEY UPDATE data = VALUES(data), last_access = NOW()
        ");
        return $stmt->execute([$id, $data]);
    }

    public function read(string $id): string|false
    {
        $stmt = $this->db->prepare("SELECT data FROM sessions WHERE id = ?");
        $stmt->execute([$id]);
        return $stmt->fetchColumn() ?: '';
    }

    // Implement other SessionHandlerInterface methods...
    public function open(string $path, string $name): bool { return true; }
    public function close(): bool { return true; }
    public function destroy(string $id): bool { return true; }
    public function gc(int $max_lifetime): int|false { return 0; }
}
```

## Examples

```php
// AJAX-friendly session handling
function handleAjaxRequest(): void
{
    if (session_status() === PHP_SESSION_NONE) {
        session_start();
    }

    // Save session data
    $_SESSION['ajax_request_time'] = microtime(true);

    // Close immediately to release lock
    session_write_close();

    // Process AJAX request without holding session lock
    $response = processRequest($_GET['action']);

    header('Content-Type: application/json');
    echo json_encode($response);
}

handleAjaxRequest();
```

```php
// Long-running CLI with periodic session saves
function processQueue(): void
{
    $queue = getPendingJobs();

    foreach ($queue as $index => $job) {
        // Periodically start and save session for status tracking
        if ($index % 100 === 0) {
            if (session_status() !== PHP_SESSION_ACTIVE) {
                session_start();
            }
            $_SESSION['queue_progress'] = $index;
            $_SESSION['last_update'] = time();
            session_write_close();
        }

        processJob($job);
    }
}
```

## Related Errors

- [session-start-error.md](/content/languages/php/session-start-error.md) — PHP session_start() failure
- [session-destroy-error.md](/content/languages/php/session-destroy-error.md) — PHP session_destroy() failure
- [session-regenerate-id-error.md](/content/languages/php/session-regenerate-id-error.md) — PHP session_regenerate_id() failure
- [headers-sent.md](/content/languages/php/headers-sent.md) — Cannot send headers after output
