---
title: "PHP Warning: array_search(): Needle cannot be empty"
description: "Fix PHP Warning: array_search() needle cannot be empty. Learn to validate search values before using array_search()."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["warning", "array-search", "needle", "empty-string"]
weight: 5
---

# PHP Warning: array_search(): Needle cannot be empty

This warning occurs when you pass an empty string as the needle to `array_search()`. The function requires a non-empty value to search for within the haystack array.

## Common Causes

- Passing an uninitialized or empty variable as the search needle
- Not trimming or validating user input before searching
- Using string interpolation that results in an empty value

## How to Fix

### Validate the Needle Before Searching

```php
<?php
// Wrong — needle may be empty
$key = array_search($needle, $haystack);

// Correct — check first
if (!empty($needle)) {
    $key = array_search($needle, $haystack);
} else {
    $key = false;
}
?>
```

### Use a Guard Function

```php
<?php
function safeArraySearch(mixed $needle, array $haystack): int|string|false {
    if ($needle === '' || $needle === null) {
        return false;
    }
    return array_search($needle, $haystack, true);
}
?>
```

### Use in_array() for Existence Checks

```php
<?php
if (!empty($needle) && in_array($needle, $haystack)) {
    echo "Found";
}
?>
```

## Examples

```php
<?php
// This triggers the warning
$needle = '';
$haystack = ['apple', 'banana', 'cherry'];
$key = array_search($needle, $haystack);
// Warning: array_search(): Needle cannot be empty

// Correct
$key = array_search('banana', $haystack); // 1
?>
```

## Related Errors

- [PHP Warning: in_array()]({{< relref "/languages/php/warning-in-in-array" >}})
- [PHP Warning: strpos()]({{< relref "/languages/php/warning-in-strpos" >}})
- [PHP Warning: array_diff()]({{< relref "/languages/php/warning-in-array-diff" >}})
