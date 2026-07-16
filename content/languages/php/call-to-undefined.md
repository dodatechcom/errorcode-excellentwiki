---
title: "PHP Fatal error: Call to undefined function X()"
description: "Fix PHP Fatal error: Call to undefined function. Learn why PHP cannot find a function and how to resolve missing functions."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["fatal-error", "undefined-function", "call-to-undefined", "function"]
weight: 5
---

# PHP Fatal error: Call to undefined function X()

This fatal error occurs when PHP tries to call a function that does not exist. PHP stops execution immediately because it cannot find a definition for the function name.

## Common Causes

- Function name is misspelled (case-sensitive)
- Required extension is not loaded (e.g., calling `curl_init()` without ext-curl)
- Function was removed or renamed in a newer PHP version
- Autoloader fails to load the class containing the method

## How to Fix

### Verify Function Exists

```php
<?php
if (function_exists('curl_init')) {
    $ch = curl_init();
} else {
    // Handle missing extension
}
?>
```

### Enable the Required Extension

```ini
; php.ini
extension=curl
extension=mbstring
extension=pdo_mysql
```

### Check PHP Version Compatibility

```php
<?php
echo PHP_VERSION;
// If function was removed in newer PHP, find the replacement
// Example: create_function() removed in PHP 8.0, use anonymous functions instead
?>
```

### Use Proper Autoloading

```php
<?php
// Ensure Composer autoloader is included
require_once __DIR__ . '/vendor/autoload.php';

// Now class methods are available
$obj = new MyClass();
$obj->someMethod();
?>
```

## Examples

```php
<?php
// Example 1: Missing extension
$conn = mysqli_connect('localhost', 'user', 'pass');
// Fatal error: Call to undefined function mysqli_connect()
// Fix: extension=mysqli in php.ini

// Example 2: Misspelled function
$result = arra_key_exists('key', $array);
// Fatal error: Call to undefined function arra_key_exists()
// Fix: use array_key_exists('key', $array)

// Example 3: Removed in PHP 8
$fn = create_function('$a', 'return $a + 1;');
// Fatal error: Call to undefined function create_function()
// Fix: use fn($a) => $a + 1
?>
```

## Related Errors

- [PHP Fatal Error: Allowed memory size exhausted]({{< relref "/languages/php/fatal-error" >}})
- [PHP Notice: Undefined Variable]({{< relref "/languages/php/notice-undefined-variable" >}})
- [PHP Warning: count()]({{< relref "/languages/php/warning-count" >}})
