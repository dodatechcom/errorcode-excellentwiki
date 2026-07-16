---
title: "[Solution] PHP E_COMPILE_WARNING — Compilation Warning Fix"
description: "Fix PHP E_COMPILE_WARNING non-fatal compilation warnings. Learn to resolve compile-time warnings about missing classes, extensions, and configuration."
languages: ["php"]
severities: ["warning"]
error-types: ["runtime-error"]
tags: ["e-compile-warning", "compile", "warning"]
weight: 5
---

# [Solution] PHP E_COMPILE_WARNING — Compilation Warning Fix

`E_COMPILE_WARNING` is a non-fatal warning that occurs during script compilation. The script can still execute, but the warning indicates a potential issue with includes, class definitions, or extension availability that should be investigated.

## Common Causes

- Including files that generate non-fatal warnings
- Using extensions that are partially loaded
- Class aliases that conflict with existing definitions
- Non-critical compilation warnings from opcode caches

## How to Fix

### 1. Fix Include Warnings

```php
// WARNING — include file may have issues
<?php
include 'config.php'; // generates a compile warning
?>

// CORRECT — use require with error handling
<?php
if (file_exists('config.php')) {
    require_once 'config.php';
} else {
    error_log("Missing config.php");
    die("Configuration file not found");
}
?>
```

### 2. Check Extension Status

```bash
# List all loaded extensions
php -m

# Check if a specific extension is loaded
php -m | grep redis
```

### 3. Resolve Class Alias Conflicts

```php
// WRONG — alias conflicts with existing class
<?php
class_exists('DateTime') or class_alias('CustomDateTime', 'DateTime');
?>

// CORRECT — use a unique alias name
<?php
class_alias('CustomDateTime', 'MyDateTime');
?>
```

### 4. Clear Opcode Cache

```bash
# Restart PHP-FPM to clear opcache
sudo systemctl restart php8.2-fpm

# Or clear via CLI
php -r "opcache_reset();"
```

## Examples

```php
<?php
// E_COMPILE_WARNING: include with issues
include 'partial-file.php';

// E_COMPILE_WARNING: class alias conflict
class_alias('ExtendsClass', 'ExistingClass');

// E_COMPILE_WARNING: extension not fully loaded
redis_connect(); // if redis extension is partially loaded
?>
```

## Related Errors

- [PHP E_COMPILE_ERROR]({{< relref "/languages/php/e-compile-error" >}})
- [PHP E_CORE_WARNING]({{< relref "/languages/php/e-core-warning" >}})
- [PHP E_WARNING]({{< relref "/languages/php/e-warning" >}})
- [PHP E_PARSE]({{< relref "/languages/php/e-parse" >}})
