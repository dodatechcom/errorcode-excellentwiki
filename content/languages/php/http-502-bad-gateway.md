---
title: "[Solution] PHP HTTP 502 Bad Gateway — PHP-FPM and Upstream Connection Issues"
description: "Fix PHP HTTP 502 Bad Gateway: PHP-FPM / upstream connection issues. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 1105
---

# PHP HTTP 502 Bad Gateway — PHP-FPM and Upstream Connection Issues

An HTTP 502 Bad Gateway error occurs when a web server (Nginx, Apache) acting as a gateway or proxy receives an invalid response from an upstream server (PHP-FPM). This typically means PHP-FPM is down, crashed, or timed out while processing a request.

## Common Causes

```php
<?php
// PHP script exceeding max_execution_time → FPM worker killed
sleep(300); // Exceeds max_execution_time

// Memory exhaustion crashes the FPM worker
$largeData = str_repeat('x', 100 * 1024 * 1024); // 100MB string

// Segfault in PHP extension crashes FPM
// (Usually in C extensions, not PHP code)

// FPM pool misconfiguration
// Wrong listen address or port in php-fpm.conf
```

## How to Fix

### Fix 1: Check PHP-FPM Status

```bash
# Check if PHP-FPM is running
sudo systemctl status php8.2-fpm

# Check PHP-FPM process list
ps aux | grep php-fpm

# Check PHP-FPM error log
sudo tail -f /var/log/php8.2-fpm.log

# Check for crashes or segfaults
sudo journalctl -u php8.2-fpm --since "1 hour ago"

# Test PHP-FPM directly
sudo systemctl restart php8.2-fpm
curl -I http://localhost
```

### Fix 2: Verify fastcgi_pass Configuration

```nginx
# nginx.conf — ensure correct fastcgi_pass
location ~ \.php$ {
    # For Unix socket:
    fastcgi_pass unix:/var/run/php/php8.2-fpm.sock;

    # For TCP socket:
    # fastcgi_pass 127.0.0.1:9000;

    # Required fastcgi parameters
    include fastcgi_params;
    fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
    fastcgi_param PATH_INFO $fastcgi_path_info;

    # Timeouts should match or exceed PHP max_execution_time
    fastcgi_read_timeout 300s;
    fastcgi_send_timeout 300s;

    # Buffer settings
    fastcgi_buffer_size 128k;
    fastcgi_buffers 4 256k;
    fastcgi_busy_buffers_size 256k;
}
```

### Fix 3: Increase Timeout Settings

```ini
; php.ini — increase execution limits
max_execution_time = 300
max_input_time = 300
memory_limit = 256M

; FPM pool config: /etc/php/8.2/fpm/pool.d/www.conf
; Increase timeout for long-running scripts
request_terminate_timeout = 300s

; Increase number of workers if requests are queuing
pm = dynamic
pm.max_children = 50
pm.start_servers = 10
pm.min_spare_servers = 5
pm.max_spare_servers = 20
pm.max_requests = 500
```

### Fix 4: Restart PHP-FPM

```bash
# Restart PHP-FPM
sudo systemctl restart php8.2-fpm

# Reload configuration without downtime
sudo systemctl reload php8.2-fpm

# Check for configuration errors before restarting
sudo php-fpm8.2 -t

# Monitor FPM process health
watch -n 1 'ps aux | grep php-fpm | grep -v grep | wc -l'
```

### Fix 5: Implement FPM Health Checks

```php
<?php
// health-check.php — monitor PHP-FPM status
function checkFpmHealth(): array
{
    $checks = [];

    // Check 1: Can we process a request?
    $start = microtime(true);
    $result = @file_get_contents('http://127.0.0.1/health-check-ping.php');
    $elapsed = microtime(true) - $start;

    $checks['response_time'] = round($elapsed, 3) . 's';
    $checks['response_ok'] = ($result !== false);

    // Check 2: Process manager status
    $statusFile = '/var/run/php/php8.2-fpm.pid';
    $checks['pid_file_exists'] = file_exists($statusFile);

    // Check 3: Socket file exists (Unix socket mode)
    $socketFile = '/var/run/php/php8.2-fpm.sock';
    $checks['socket_exists'] = file_exists($socketFile);

    // Check 4: Memory usage
    $checks['memory_usage'] = round(memory_get_usage(true) / 1024 / 1024, 2) . ' MB';
    $checks['memory_peak'] = round(memory_get_peak_usage(true) / 1024 / 1024, 2) . ' MB';

    return $checks;
}

header('Content-Type: application/json');
echo json_encode(checkFpmHealth(), JSON_PRETTY_PRINT);
```

## Examples

```php
<?php
// Example 1: Nginx upstream configuration for multiple PHP-FPM instances
// In nginx.conf:
// upstream php-backend {
//     server unix:/var/run/php/php8.2-fpm.sock;
//     server 127.0.0.1:9001;
//     server 127.0.0.1:9002;
// }

// Example 2: Graceful timeout handling
function longRunningTask(): void
{
    // Set a reasonable execution time
    set_time_limit(120);

    // Process in chunks to avoid FPM timeout
    $totalItems = 10000;
    $chunkSize = 100;

    for ($i = 0; $i < $totalItems; $i += $chunkSize) {
        $chunk = range($i, min($i + $chunkSize - 1, $totalItems));
        processChunk($chunk);

        // Flush output to prevent timeout
        if (ob_get_level() > 0) {
            ob_flush();
        }
        flush();

        // Small sleep to allow other requests to be served
        usleep(100000); // 100ms
    }
}

// Example 3: Return 503 instead of 502 when overloaded
function handleRequest(): void
{
    $load = sys_getloadavg();

    if ($load[0] > 50) {
        http_response_code(503);
        header('Retry-After: 60');
        echo json_encode(['error' => 'Server overloaded, please retry']);
        return;
    }

    // Normal request handling
    http_response_code(200);
    echo json_encode(['status' => 'ok']);
}
```

## Related Errors

- [PHP HTTP 500 Internal Server Error]({{< relref "/languages/php/http-500-error" >}})
- [PHP HTTP 503 Service Unavailable]({{< relref "/languages/php/http-503-service-unavailable" >}})
- [PHP Fatal Out of Memory]({{< relref "/languages/php/fatal-out-of-memory" >}})
