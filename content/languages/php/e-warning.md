---
title: "[Solution] PHP E_WARNING — Runtime Warning Fix"
description: "Fix PHP E_WARNING runtime errors. Learn common causes and solutions for PHP warnings that don't halt script execution but indicate potential problems."
languages: ["php"]
severities: ["warning"]
error-types: ["runtime-error"]
weight: 5
---

# [Solution] PHP E_WARNING — Runtime Warning Fix

`E_WARNING` is a non-fatal runtime error in PHP. The script continues executing after a warning, but the operation that triggered the warning did not work as expected. Warnings indicate potential problems that should be reviewed and fixed.

## Common Causes

- Passing invalid arguments to built-in functions
- Trying to open a file that does not exist or is unreadable
- Dividing a number by zero in non-strict mode
- Using deprecated or incompatible function parameters

## How to Fix

### 1. Check File Existence Before Operations

```php
// WRONG — warning if file does not exist
<?php
$lines = file('missing.txt');
?>

// CORRECT
<?php
if (file_exists('missing.txt')) {
    $lines = file('missing.txt');
} else {
    echo "File not found";
}
?>
```

### 2. Validate Function Arguments

```php
// WRONG — invalid argument
<?php
strlen(null); // Warning: strlen() expects parameter 1 to be string, null given
?>

// CORRECT
<?php
$value = 'hello';
echo strlen($value); // 5
?>
```

### 3. Prevent Division by Zero

```php
// WRONG — division by zero
<?php
$result = 10 / 0;
?>

// CORRECT
<?php
$b = 0;
if ($b !== 0) {
    $result = 10 / $b;
} else {
    echo "Cannot divide by zero";
}
?>
```

## Examples

```php
<?php
// Warning: fopen() — file does not exist
$fp = fopen('nonexistent.txt', 'r');

// Warning: preg_match() — missing delimiter
preg_match('[a-z]', 'hello');

// Warning: file_get_contents() — failed to open stream
$content = file_get_contents('http://invalid-url-that-does-not-exist.test');
?>
```

## Related Errors

- [PHP Notice: Undefined Variable]({{< relref "/languages/php/notice-undefined-variable" >}})
- [PHP Notice: Undefined Index]({{< relref "/languages/php/notice-undefined-index" >}})
- [PHP Fatal Error]({{< relref "/languages/php/fatal-error" >}})
- [PHP Deprecated Warning]({{< relref "/languages/php/deprecated-filter" >}})
