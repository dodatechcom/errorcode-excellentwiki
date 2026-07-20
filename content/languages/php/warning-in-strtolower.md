---
title: "PHP Warning: strtolower() expects parameter 1 to be string"
description: "Fix PHP Warning: strtolower() and strtoupper() expect string parameters. Learn to cast types and handle null values."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# PHP Warning: strtolower() expects parameter 1 to be string

This warning occurs when `strtolower()` or `strtoupper()` receives a non-string argument such as null, an integer, or an array.

## Common Causes

- Passing null values from database queries or form input
- Using integer or float values directly
- Passing arrays instead of strings

## How to Fix

### Cast to String

```php
<?php
// Wrong — passing an integer
$lower = strtolower(123);

// Correct — cast to string first
$lower = strtolower((string) 123); // '123'
?>
```

### Check Variable Type

```php
<?php
// Wrong — null or non-string value
$lower = strtolower($value);

// Correct — type check before conversion
if (is_string($value)) {
    $lower = strtolower($value);
}
?>
```

### Handle Null with Null Coalescing

```php
<?php
// Wrong — null causes warning
$lower = strtolower($input ?? null);

// Correct — use empty string as default
$lower = strtolower($input ?? '');
?>
```

## Examples

```php
<?php
// This triggers the warning
$value = null;
$lower = strtolower($value);
// Warning: strtolower() expects parameter 1 to be string, null given

// Correct
$lower = strtolower($value ?? '');
?>
```

## Related Errors

- [PHP Warning: trim()]({{< relref "/languages/php/warning-in-trim" >}})
- [PHP Warning: substr()]({{< relref "/languages/php/warning-in-substr" >}})
- [PHP Warning: ucfirst()]({{< relref "/languages/php/warning-in-ucfirst" >}})
