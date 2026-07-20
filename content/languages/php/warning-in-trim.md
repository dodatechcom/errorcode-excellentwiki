---
title: "PHP Warning: trim() expects parameter 1 to be string"
description: "Fix PHP trim(), ltrim(), and rtrim() parameter issues. Learn to ensure string parameters, check for null, and handle empty strings."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# PHP Warning: trim() expects parameter 1 to be string

This warning occurs when `trim()`, `ltrim()`, or `rtrim()` receives a non-string argument. The functions require a string as the first parameter and optionally a character mask as the second.

## Common Causes

- Passing null values from user input or database results
- Applying trim to non-string variables
- Omitting the string argument from the function call

## How to Fix

### Ensure String Parameter

```php
<?php
// Wrong — null or non-string
$trimmed = trim($value);

// Correct — cast to string or use default
$trimmed = trim((string) $value);
?>
```

### Check for Null Before Trimming

```php
<?php
// Wrong — null value
$trimmed = trim($value);

// Correct — null coalescing
$trimmed = trim($value ?? '');
?>
```

### Handle Empty Strings

```php
<?php
// Wrong — trimming a non-string
$trimmed = trim($input);

// Correct — check type first
$trimmed = is_string($input) ? trim($input) : '';
?>
```

## Examples

```php
<?php
// This triggers the warning
$input = null;
$trimmed = trim($input);
// Warning: trim() expects parameter 1 to be string, null given

// Correct
$trimmed = trim($input ?? '');
$name = trim('  Hello  '); // 'Hello'
?>
```

## Related Errors

- [PHP Warning: strtolower()]({{< relref "/languages/php/warning-in-strtolower" >}})
- [PHP Warning: substr()]({{< relref "/languages/php/warning-in-substr" >}})
- [PHP Warning: str_replace()]({{< relref "/languages/php/warning-in-str-replace" >}})
