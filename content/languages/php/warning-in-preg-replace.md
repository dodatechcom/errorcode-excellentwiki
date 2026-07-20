---
title: "PHP Warning: preg_replace() errors"
description: "Fix PHP Warning: preg_replace() errors. Learn to check regex patterns, handle null bytes, and use preg_replace_callback() for complex cases."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# PHP Warning: preg_replace() errors

This warning occurs when `preg_replace()` encounters issues such as invalid regex patterns, null bytes in the subject, or modifier errors.

## Common Causes

- Invalid regex pattern syntax
- Null bytes or special characters in the subject string
- Backtrack limit exhaustion on large strings

## How to Fix

### Check Regex Pattern

```php
<?php
// Wrong — invalid pattern
$result = preg_replace('/[a-z/', '', $string);

// Correct — validate pattern first
$pattern = '/[a-z]/';
if (@preg_match($pattern, '') !== false) {
    $result = preg_replace($pattern, '', $string);
}
?>
```

### Handle Null Bytes

```php
<?php
// Wrong — null byte in subject
$result = preg_replace('/old/', 'new', "hello\0world");

// Correct — remove null bytes first
$cleaned = str_replace("\0", '', $string);
$result = preg_replace('/old/', 'new', $cleaned);
?>
```

### Use preg_replace_callback() for Complex Cases

```php
<?php
// Wrong — complex replacement logic in pattern
$result = preg_replace('/(\d+)/e', 'pow(2, $1)', $string);

// Correct — use callback
$result = preg_replace_callback('/(\d+)/', function ($m) {
    return pow(2, $m[1]);
}, $string);
?>
```

## Examples

```php
<?php
// This triggers the warning
$result = preg_replace('/unclosed/', 'replacement'); // missing subject
// Warning: preg_replace() expects at least 3 parameters

// Correct
$result = preg_replace('/old/', 'new', 'Hello old world'); // 'Hello new world'
?>
```

## Related Errors

- [PHP Warning: preg_match()]({{< relref "/languages/php/warning-in-preg-match" >}})
- [PHP Warning: preg_split()]({{< relref "/languages/php/warning-in-preg-split" >}})
- [PHP Warning: PCRE backtrack limit]({{< relref "/languages/php/warning-preg-backtrack-limit" >}})
