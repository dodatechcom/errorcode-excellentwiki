---
title: "[Solution] Composer Autoload Error Fix"
description: "Fix Composer autoload failure. Class not found errors, autoload configuration, and namespace mapping."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 1107
---

# Composer Autoload Error

Composer autoload errors occur when classes cannot be found at runtime because the autoloader has not been generated, the autoload configuration is incorrect, or namespace mappings don't match the actual directory structure. This is one of the most common PHP errors when working with Composer.

## Common Causes

```php
<?php
// Cause 1: Autoloader not generated after install
require 'vendor/autoload.php'; // File exists but is stale

// Cause 2: Incorrect PSR-4 namespace mapping
// composer.json has: "autoload": { "psr-4": { "App\\": "src/" } }
// But class is in wrong directory

// Cause 3: Class namespace doesn't match directory structure
namespace App\Models; // Class says Models but file is in src/Controller/

// Cause 4: Missing autoload entry for new files
// New class added but composer dump-autoload not run

// Cause 5: Autoload not requiring the file
// Using classmap or files autoloading but entry missing
```

## How to Fix

### Fix 1: Regenerate the autoloader

```bash
composer dump-autoload
# Or for optimized autoloader
composer dump-autoload -o
```

### Fix 2: Check and fix PSR-4 autoload configuration

```json
{
    "autoload": {
        "psr-4": {
            "App\\": "app/",
            "App\\Models\\": "app/Models/",
            "Database\\Factories\\": "database/factories/"
        }
    }
}
```

```php
<?php
// Verify namespace matches directory
// File: app/Models/User.php
namespace App\Models;

class User
{
    // This will be found if autoload config maps "App\\Models\\" to "app/Models/"
}
```

### Fix 3: Verify directory structure matches namespace

```bash
# Check your autoload config
cat composer.json | grep -A 10 '"autoload"'

# Verify directory structure
ls -la app/Models/

# Ensure the namespace separators map to directories
# App\Models\User → app/Models/User.php
```

### Fix 4: Include autoloader in your application entry point

```php
<?php
// Ensure autoloader is loaded before any class usage
require __DIR__ . '/vendor/autoload.php';

// If using a framework, check bootstrap file
// Laravel: vendor/autoload.php is loaded in public/index.php
// Symfony: vendor/autoload.php is loaded in bin/console

// If still failing, check file permissions
// chmod 755 vendor/autoload.php
```

### Fix 5: Use composer update to resolve conflicts

```bash
# Update all packages
composer update

# Or update specific package
composer update vendor/package-name

# If there's a lock file issue
rm composer.lock
composer install
```

## Examples

```php
<?php
// Debugging autoload issues

// 1. Check if autoloader exists
if (!file_exists('vendor/autoload.php')) {
    echo "Run: composer install\n";
    exit(1);
}

// 2. Verify a class is autoloadable
$autoloader = require 'vendor/autoload.php';
$classPath = $autoloader->findFile('App\\Models\\User');
var_dump($classPath); // string or false

// 3. Check if class exists after autoloading
var_dump(class_exists('App\\Models\\User')); // true or false

// 4. Manually register an autoloader for debugging
spl_autoload_register(function ($class) {
    $prefix = 'App\\';
    $baseDir = __DIR__ . '/app/';

    $len = strlen($prefix);
    if (strncmp($prefix, $class, $len) !== 0) {
        return;
    }

    $relativeClass = substr($class, $len);
    $file = $baseDir . str_replace('\\', '/', $relativeClass) . '.php';

    if (file_exists($file)) {
        require $file;
    }
});
```

## Related Errors

- [Composer Package Not Found]({{< relref "/languages/php/composer-package-not-found" >}}) — package installation issues
- [Composer Conflict Error]({{< relref "/languages/php/composer-conflict-error" >}}) — dependency conflicts
- [Composer Error]({{< relref "/languages/php/composer-error" >}}) — general Composer errors
