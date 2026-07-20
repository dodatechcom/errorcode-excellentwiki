---
title: "[Solution] PHP HTTP 503 Service Unavailable — Maintenance Mode and Server Overload"
description: "Fix PHP HTTP 503 Service Unavailable: maintenance mode / server overload. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 1106
---

# PHP HTTP 503 Service Unavailable — Maintenance Mode and Server Overload

An HTTP 503 Service Unavailable error indicates the server is temporarily unable to handle the request. In PHP applications, this is commonly caused by maintenance mode, server overload, too many concurrent requests, or resource exhaustion.

## Common Causes

```php
<?php
// Maintenance mode enabled
// File-based:
if (file_exists(__DIR__ . '/maintenance.flag')) {
    http_response_code(503);
    echo 'Site is under maintenance';
    exit;
}

// Server overload from too many simultaneous requests
// No rate limiting in place
// Database connection pool exhausted

// Resource limits hit
// PHP-FPM max_children reached
// Memory limit exhausted under load
```

## How to Fix

### Fix 1: Check and Disable Maintenance Mode

```php
<?php
// bootstrap.php — check maintenance mode
function isMaintenanceMode(): bool
{
    $maintenanceFile = __DIR__ . '/storage/maintenance.flag';
    $maintenanceMode = file_exists($maintenanceFile);

    // Allow admins to bypass maintenance mode
    if ($maintenanceMode && isset($_SESSION['admin'])) {
        return false;
    }

    // Allow specific IPs to bypass
    $allowedIPs = ['127.0.0.1', '::1'];
    if ($maintenanceMode && in_array($_SERVER['REMOTE_ADDR'], $allowedIPs)) {
        return false;
    }

    return $maintenanceMode;
}

if (isMaintenanceMode()) {
    http_response_code(503);
    header('Retry-After: 3600'); // Retry after 1 hour
    header('Content-Type: text/html');
    echo file_get_contents(__DIR__ . '/resources/views/maintenance.html');
    exit;
}
```

```bash
# Create maintenance flag
touch /var/www/html/storage/maintenance.flag

# Remove maintenance flag
rm /var/www/html/storage/maintenance.flag

# Check if maintenance mode is active
ls -la /var/www/html/storage/maintenance.flag
```

### Fix 2: Implement Rate Limiting

```php
<?php
class RateLimiter
{
    private string $storagePath;
    private int $maxRequests;
    private int $windowSeconds;

    public function __construct(string $storagePath, int $maxRequests = 100, int $windowSeconds = 60)
    {
        $this->storagePath = $storagePath;
        $this->maxRequests = $maxRequests;
        $this->windowSeconds = $windowSeconds;
    }

    public function isAllowed(string $key): bool
    {
        $file = $this->storagePath . '/' . md5($key) . '.json';

        $data = ['requests' => [], 'blocked_until' => 0];

        if (file_exists($file)) {
            $data = json_decode(file_get_contents($file), true) ?? $data;
        }

        // Check if currently blocked
        if (time() < ($data['blocked_until'] ?? 0)) {
            return false;
        }

        // Clean old requests outside the window
        $cutoff = time() - $this->windowSeconds;
        $data['requests'] = array_filter($data['requests'], fn($t) => $t > $cutoff);

        // Check limit
        if (count($data['requests']) >= $this->maxRequests) {
            $data['blocked_until'] = time() + $this->windowSeconds;
            file_put_contents($file, json_encode($data));
            return false;
        }

        // Record this request
        $data['requests'][] = time();
        file_put_contents($file, json_encode($data));
        return true;
    }

    public function getRemainingRequests(string $key): int
    {
        $file = $this->storagePath . '/' . md5($key) . '.json';

        if (!file_exists($file)) {
            return $this->maxRequests;
        }

        $data = json_decode(file_get_contents($file), true) ?? ['requests' => []];
        $cutoff = time() - $this->windowSeconds;
        $data['requests'] = array_filter($data['requests'], fn($t) => $t > $cutoff);

        return max(0, $this->maxRequests - count($data['requests']));
    }
}

// Usage
$limiter = new RateLimiter('/tmp/rate_limiter', 100, 60);
$clientIP = $_SERVER['REMOTE_ADDR'];

if (!$limiter->isAllowed($clientIP)) {
    http_response_code(503);
    header('Retry-After: 60');
    header('Content-Type: application/json');
    echo json_encode(['error' => 'Rate limit exceeded. Try again later.']);
    exit;
}
```

### Fix 3: Increase Server Capacity

```ini
; php-fpm pool configuration
; /etc/php/8.2/fpm/pool.d/www.conf

; Increase max children based on available RAM
; Rule: each PHP process uses ~20-50MB depending on application
pm = dynamic
pm.max_children = 50        ; Increase based on RAM (50 * 40MB = 2GB)
pm.start_servers = 10
pm.min_spare_servers = 5
pm.max_spare_servers = 20
pm.max_requests = 500       ; Restart workers after 500 requests

; Increase timeouts for slower requests
request_terminate_timeout = 120s

; php.ini
max_execution_time = 120
memory_limit = 256M
max_input_vars = 3000
```

### Fix 4: Implement Maintenance Mode with Retry-After

```php
<?php
// maintenance.php — full maintenance mode implementation
function handleMaintenance(): void
{
    $maintenanceFile = __DIR__ . '/storage/maintenance.flag';

    if (!file_exists($maintenanceFile)) {
        return;
    }

    $data = json_decode(file_get_contents($maintenanceFile), true) ?? [];
    $retryAfter = $data['retry_after'] ?? 3600;
    $message = $data['message'] ?? 'We are currently performing scheduled maintenance.';

    http_response_code(503);
    header('Retry-After: ' . $retryAfter);
    header('Content-Type: text/html; charset=utf-8');

    echo '<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Maintenance Mode</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, sans-serif;
               display: flex; justify-content: center; align-items: center;
               min-height: 100vh; margin: 0; background: #f5f5f5; }
        .container { text-align: center; padding: 2rem; background: white;
                     border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        h1 { color: #333; }
        p { color: #666; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Scheduled Maintenance</h1>
        <p>' . htmlspecialchars($message) . '</p>
        <p>Please try again in ' . ($retryAfter / 60) . ' minutes.</p>
    </div>
</body>
</html>';

    exit;
}

handleMaintenance();
```

### Fix 5: Monitor and Alert on 503 Errors

```php
<?php
// monitor.php — track 503 error rates
class HealthMonitor
{
    private string $logFile;

    public function __construct(string $logFile)
    {
        $this->logFile = $logFile;
    }

    public function logRequest(int $statusCode, float $responseTime): void
    {
        $entry = [
            'timestamp' => date('c'),
            'status'    => $statusCode,
            'duration'  => round($responseTime, 4),
            'memory'    => memory_get_usage(true),
            'load'      => sys_getloadavg(),
        ];

        file_put_contents($this->logFile, json_encode($entry) . "\n", FILE_APPEND);
    }

    public function get503Rate(int $minutes = 5): array
    {
        $lines = file($this->logFile) ?? [];
        $cutoff = time() - ($minutes * 60);
        $total = 0;
        $errors503 = 0;

        foreach ($lines as $line) {
            $entry = json_decode($line, true);
            if ($entry === null) continue;

            $entryTime = strtotime($entry['timestamp']);
            if ($entryTime < $cutoff) continue;

            $total++;
            if ($entry['status'] === 503) {
                $errors503++;
            }
        }

        return [
            'total_requests' => $total,
            'errors_503'     => $errors503,
            'error_rate'     => $total > 0 ? round($errors503 / $total * 100, 2) : 0,
        ];
    }
}

// Usage in middleware or error handler
$monitor = new HealthMonitor('/var/log/php/health.log');
$monitor->logRequest(http_response_code(), microtime(true) - $_SERVER['REQUEST_TIME_FLOAT']);

// Check if error rate is too high
$stats = $monitor->get503Rate(5);
if ($stats['error_rate'] > 50 && $stats['total_requests'] > 10) {
    error_log("High 503 rate detected: {$stats['error_rate']}%");
    // Trigger alert (email, Slack, etc.)
}
```

## Examples

```php
<?php
// Example 1: Enable maintenance mode via CLI script
// bin/maintenance.php
$mode = $argv[1] ?? 'off';
$maintenanceFile = __DIR__ . '/storage/maintenance.flag';

if ($mode === 'on') {
    $data = [
        'enabled'    => true,
        'started_at' => date('c'),
        'message'    => 'Scheduled database maintenance. We will be back shortly.',
        'retry_after' => 7200, // 2 hours
    ];
    file_put_contents($maintenanceFile, json_encode($data));
    echo "Maintenance mode enabled.\n";

} elseif ($mode === 'off') {
    unlink($maintenanceFile);
    echo "Maintenance mode disabled.\n";

} else {
    echo "Usage: php maintenance.php [on|off]\n";
}

// Example 2: Queue-based maintenance mode (more robust)
function setMaintenanceMode(bool $enabled, string $reason = ''): void
{
    $redis = new Redis();
    $redis->connect('127.0.0.1', 6379);

    if ($enabled) {
        $redis->set('maintenance:mode', '1');
        $redis->set('maintenance:reason', $reason);
        $redis->set('maintenance:started', time());
    } else {
        $redis->del(['maintenance:mode', 'maintenance:reason', 'maintenance:started']);
    }
}

function isMaintenanceMode(): bool
{
    $redis = new Redis();
    $redis->connect('127.0.0.1', 6379);

    return $redis->get('maintenance:mode') === '1';
}
```

## Related Errors

- [PHP HTTP 502 Bad Gateway]({{< relref "/languages/php/http-502-bad-gateway" >}})
- [PHP HTTP 500 Internal Server Error]({{< relref "/languages/php/http-500-error" >}})
- [PHP Memory Exhausted]({{< relref "/languages/php/memory-exhausted" >}})
