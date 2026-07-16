---
title: "[Solution] PHP Error 128 — SIGTERM Script Terminated Fix"
description: "Fix PHP error code 128 SIGTERM script termination. Learn to handle external process termination signals and prevent unexpected script death."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["error-128", "SIGTERM", "signal", "terminated"]
weight: 5
---

# [Solution] PHP Error 128 — SIGTERM Script Terminated Fix

PHP error code 128 indicates the script was terminated by a `SIGTERM` (signal 15) from an external source. This is not a PHP error itself — it means the operating system or a process manager killed the PHP process. PHP exit codes are calculated as `128 + signal number`, so `128 + 15 = 143` for SIGTERM, but error 128 specifically reflects the base exit code when the process receives a termination signal.

## Common Causes

- Web server (Apache/Nginx) timeout killing long-running scripts
- Process manager (systemd, supervisord) terminating the process
- Manual `kill` command sent to the PHP process
- Container orchestration (Docker, Kubernetes) stopping the container

## How to Fix

### 1. Increase Script Timeout

```php
// WRONG — script exceeds max_execution_time
<?php
sleep(300); // 5 minutes, will be killed by timeout
?>

// CORRECT — increase execution time limit
<?php
set_time_limit(600); // 10 minutes
// Or disable for CLI scripts
set_time_limit(0);
?>
```

### 2. Configure Server Timeout Settings

```apache
# Apache httpd.conf or .htaccess
# Increase timeout from default 300 seconds
Timeout 600
```

```nginx
# nginx.conf for PHP-FPM
location ~ \.php$ {
    fastcgi_read_timeout 600;
    proxy_read_timeout 600;
}
```

```ini
; php.ini
max_execution_time = 600
```

### 3. Handle Signals in PHP

```php
<?php
declare(ticks=1);
pcntl_signal(SIGTERM, function($signo) {
    error_log("Received SIGTERM, shutting down gracefully");
    // Cleanup logic
    exit(143);
});

// Long-running process
while (true) {
    pcntl_signal_dispatch();
    do_work();
    sleep(1);
}
?>
```

### 4. Use Background Processing for Long Tasks

```php
<?php
// WRONG — long-running task in web request
process_large_import($file); // may be killed by timeout

// CORRECT — queue the task and run via CLI
exec('php /path/to/import.php ' . escapeshellarg($file) . ' > /dev/null 2>&1 &');
echo "Import started in background";
?>
```

## Examples

```php
<?php
// This script may receive SIGTERM from web server timeout
function longRunningTask() {
    for ($i = 0; $i < 100000; $i++) {
        // heavy computation
    }
}
longRunningTask(); // Exit code: 128 if killed externally
?>
```

## Related Errors

- [PHP Fatal Error]({{< relref "/languages/php/fatal-error" >}})
- [PHP Fatal Out of Memory]({{< relref "/languages/php/fatal-out-of-memory" >}})
- [PHP E_ERROR]({{< relref "/languages/php/e-error" >}})
- [PHP E_USER_ERROR]({{< relref "/languages/php/e-user-error" >}})
