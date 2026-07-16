---
title: "PHP Warning: in_array(): Needle cannot be empty"
description: "Fix PHP Warning: in_array() needle cannot be empty. Learn to validate search values before using in_array()."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["warning", "in-array", "needle", "empty-string"]
weight: 5
---

# PHP Warning: in_array(): Needle cannot be empty

This warning occurs when you pass an empty string as the needle to `in_array()`. The function requires a non-empty value to search for within the haystack array.

## Common Causes

- Passing an uninitialized or empty variable as the search needle
- Not trimming or validating user input before searching
- Using string interpolation that results in an empty value

## How to Fix

### Validate the Needle Before Searching

```php
<?php
// Wrong — needle may be empty
$result = in_array($needle, $haystack);

// Correct — check first
if (!empty($needle)) {
    $result = in_array($needle, $haystack);
} else {
    $result = false;
}
?>
```

### Use Strict Comparison with a Guard

```php
<?php
function safeInArray(mixed $needle, array $haystack): bool {
    if ($needle === '' || $needle === null) {
        return false;
    }
    return in_array($needle, $haystack, true);
}
?>
```

### Use array_search() as Alternative

```php
<?php
$key = array_search($needle, $haystack);
if ($key !== false) {
    echo "Found at key: " . $key;
}
?>
```

## Examples

```php
<?php
// This triggers the warning
$needle = '';
$haystack = ['apple', 'banana', 'cherry'];
echo in_array($needle, $haystack) ? 'Found' : 'Not found';
// Warning: in_array(): Needle cannot be empty

// Correct
$needle = 'banana';
echo in_array($needle, $haystack) ? 'Found' : 'Not found'; // Found
?>
```

## Related Errors

- [PHP Warning: array_search()]({{< relref "/languages/php/warning-in-array-search" >}})
- [PHP Warning: strpos()]({{< relref "/languages/php/warning-in-strpos" >}})
- [PHP Warning: array_diff()]({{< relref "/languages/php/warning-in-array-diff" >}})
