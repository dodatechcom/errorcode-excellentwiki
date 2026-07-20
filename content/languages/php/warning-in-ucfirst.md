---
title: "PHP Warning: ucfirst() / lcfirst() / ucwords() parameter issues"
description: "Fix PHP Warning: ucfirst, lcfirst, and ucwords parameter issues. Learn to ensure string parameters, check for null, and validate encoding."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# PHP Warning: ucfirst() / lcfirst() / ucwords() parameter issues

This warning occurs when `ucfirst()`, `lcfirst()`, or `ucwords()` receive a non-string argument. These functions expect a string and will warn on null, array, or other types.

## Common Causes

- Passing null or uninitialized variables
- Passing numbers or boolean values
- Multibyte encoding issues with non-ASCII strings

## How to Fix

### Ensure String Parameter

```php
<?php
// Wrong — passing null
$result = ucfirst($value);

// Correct — cast or default
$result = ucfirst((string) $value);
?>
```

### Check for Null

```php
<?php
// Wrong — null variable
$result = ucfirst($name);

// Correct — null coalescing
$result = ucfirst($name ?? '');
?>
```

### Handle Multibyte Strings with mb_convert_case()

```php
<?php
// Wrong — ucfirst breaks UTF-8 characters
$result = ucfirst($utf8String);

// Correct — use mb_convert_case
$result = mb_convert_case($utf8String, MB_CASE_TITLE, 'UTF-8');
?>
```

## Examples

```php
<?php
// This triggers the warning
$value = null;
$result = ucfirst($value);
// Warning: ucfirst() expects parameter 1 to be string, null given

// Correct
$result = ucfirst('hello'); // 'Hello'
$result = ucfirst($value ?? '');
?>
```

## Related Errors

- [PHP Warning: strtolower()]({{< relref "/languages/php/warning-in-strtolower" >}})
- [PHP Warning: trim()]({{< relref "/languages/php/warning-in-trim" >}})
- [PHP Warning: substr()]({{< relref "/languages/php/warning-in-substr" >}})
