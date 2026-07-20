---
title: "[Solution] PHP Warning: set_time_limit() — Function Is Disabled"
description: "Fix PHP Warning: set_time_limit() function is disabled. Check safe_mode, use max_execution_time in php.ini, handle in configuration."
languages: ["php"]
severities: ["warning"]
error-types: ["runtime-error"]
weight: 10
---

# PHP Warning: set_time_limit() — Function Is Disabled

This warning occurs when `set_time_limit()` is called but has been disabled by the server configuration. This typically happens in shared hosting environments or when `disable_functions` includes `set_time_limit` in `php.ini`.

## Common Causes

```php
<?php
// Example 1: set_time_limit disabled in php.ini
set_time_limit(300);
// Warning: set_time_limit(): This function is disabled in your server configuration
```

```php
<?php
// Example 2: safe_mode enabled (PHP < 5.4)
set_time_limit(0);
// Warning: set_time_limit(): safe mode restriction in effect
```

```php
<?php
// Example 3: Shared hosting with restricted functions
set_time_limit(60);
// Warning: set_time_limit(): This function is disabled
```

```php
<?php
// Example 4: CLI script running under restricted PHP
set_time_limit(0);
// Warning: set_time_limit(): This function is disabled
```

```php
<?php
// Example 5: Using @ to suppress but still failing
@set_time_limit(300);
// Returns false, execution time unchanged
```

## How to Fix

### Fix 1: Use max_execution_time in php.ini

Configure the execution time limit in `php.ini` instead of using `set_time_limit()`.

```ini
; php.ini
max_execution_time = 300
max_input_time = 60

; For CLI scripts that need unlimited time
; Set via command line: php -d max_execution_time=0 script.php
```

### Fix 2: Use .htaccess for Apache Servers

Set the time limit via `.htaccess` if you cannot modify `php.ini`.

```apache
# .htaccess
php_value max_execution_time 300
php_value max_input_time 60
```

### Fix 3: Use Server Configuration (nginx/FPM)

Configure time limits in your web server or PHP-FPM configuration.

```nginx
# nginx.conf — for PHP-FPM
location ~ \.php$ {
    fastcgi_read_timeout 300;
    fastcgi_send_timeout 300;
}
```

```ini
; php-fpm.conf
request_terminate_timeout = 300s
```

### Fix 4: Handle Long-Running Tasks Properly

For tasks that need more time, break them into smaller chunks or use background processing.

```php
<?php
// WRONG: Trying to extend time for a huge task
set_time_limit(0);
processMillionRows(); // Still might hit limits

// CORRECT: Process in batches
$batchSize = 1000;
$offset = 0;

while (true) {
    $batch = getBatch($offset, $batchSize);
    if (empty($batch)) break;

    foreach ($batch as $item) {
        processItem($item);
    }

    $offset += $batchSize;

    // Check if we're running out of time
    if (connection_aborted() || connection_status() !== CONNECTION_NORMAL) {
        // Save progress and return
        saveProgress($offset);
        header("Location: /resume?offset=" . $offset);
        exit;
    }
}
```

### Fix 5: Detect and Gracefully Handle the Limitation

Check if `set_time_limit()` is available before calling it.

```php
<?php
function safeSetTimeLimit(int $seconds): bool {
    if (!function_exists('set_time_limit')) {
        return false;
    }

    if (ini_get('safe_mode')) {
        return false;
    }

    // Check if set_time_limit is disabled via disable_functions
    $disabled = explode(',', ini_get('disable_functions'));
    if (in_array('set_time_limit', $disabled)) {
        return false;
    }

    @set_time_limit($seconds);
    return true;
}

if (!safeSetTimeLimit(300)) {
    // set_time_limit is unavailable — work within default limits
    error_log("set_time_limit() unavailable — using default execution time");
}
```

## Examples

```php
<?php
// Scenario: Processing a large CSV import
function importCsv(string $filepath): void {
    // Try to extend time
    if (!@set_time_limit(0)) {
        // If we can't, process only a portion
        $maxRows = 10000;
    } else {
        $maxRows = PHP_INT_MAX;
    }

    $handle = fopen($filepath, "r");
    if ($handle === false) {
        throw new \RuntimeException("Cannot open {$filepath}");
    }

    $rowIndex = 0;
    while (($row = fgetcsv($handle)) !== false && $rowIndex < $maxRows) {
        processImportRow($row);
        $rowIndex++;
    }

    fclose($handle);
    echo "Imported {$rowIndex} rows\n";
}

importCsv("/var/www/data/users.csv");
```

## Related Errors

- [PHP Memory Exhausted](/languages/php/memory-exhausted)
- [PHP Fatal Error](/languages/php/fatal-error)
- [PHP Deprecated Filter](/languages/php/deprecated-filter)
