---
title: "PHP Warning: substr() expects parameter issues"
description: "Fix PHP Warning: substr() parameter issues. Learn to check string length, validate offset, and handle multibyte strings."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# PHP Warning: substr() expects parameter issues

This warning occurs when `substr()` receives invalid parameters, such as a non-string subject, an out-of-bounds offset, or a negative length that produces unexpected results.

## Common Causes

- Passing a non-string value as the subject
- Using a negative offset on short strings
- Passing null or uninitialized variables

## How to Fix

### Check String Length Before Substring

```php
<?php
// Wrong — offset may exceed string length
$part = substr($str, 100);

// Correct — check length first
if (strlen($str) > 100) {
    $part = substr($str, 100);
} else {
    $part = '';
}
?>
```

### Validate Offset Parameters

```php
<?php
// Wrong — negative offset on a short string
$part = substr($str, -5);

// Correct — use max to avoid issues
$offset = max(0, strlen($str) - 5);
$part = substr($str, $offset);
?>
```

### Handle Multibyte Strings with mb_substr()

```php
<?php
// Wrong — breaks multibyte characters
$part = substr($utf8String, 0, 3);

// Correct — use mb_substr for UTF-8
$part = mb_substr($utf8String, 0, 3, 'UTF-8');
?>
```

## Examples

```php
<?php
// This triggers the warning
$str = null;
$part = substr($str, 0, 5);
// Warning: substr() expects parameter 1 to be string, null given

// Correct
$part = substr($str ?? '', 0, 5);
?>
```

## Related Errors

- [PHP Warning: strlen()]({{< relref "/languages/php/warning-in-strlen" >}})
- [PHP Warning: str_replace()]({{< relref "/languages/php/warning-in-str-replace" >}})
- [PHP Warning: mb_string not loaded]({{< relref "/languages/php/warning-mb-string-not-loaded" >}})
