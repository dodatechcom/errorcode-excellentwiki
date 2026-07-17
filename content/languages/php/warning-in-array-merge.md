---
title: "PHP Warning: array_merge(): Argument #1 is not an array"
description: "Fix PHP Warning: array_merge() argument not an array. Learn to validate inputs before merging arrays."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# PHP Warning: array_merge(): Argument #1 is not an array

This warning occurs when `array_merge()` receives a non-array value as one of its arguments. All arguments must be arrays for the merge to succeed.

## Common Causes

- Passing a non-array variable (string, null, integer) as an argument
- A function returning a non-array value when an array was expected
- Database query returning `false` instead of an array

## How to Fix

### Validate Inputs Before Merging

```php
<?php
// Wrong — $data might not be an array
$merged = array_merge($data, $more);

// Correct — validate first
if (is_array($data)) {
    $merged = array_merge($data, $more);
}
?>
```

### Use the Null Coalescing Operator

```php
<?php
$merged = array_merge($data ?? [], $more ?? []);
?>
```

### Use the Spread Operator

```php
<?php
// PHP 5.6+ — also requires array arguments
$merged = [...$data, ...$more];
?>
```

## Examples

```php
<?php
// This triggers the warning
$data = null;
$merged = array_merge($data, ['b']);
// Warning: array_merge(): Argument #1 is not an array

// Correct
$merged = array_merge(['a'], ['b']); // ['a', 'b']
?>
```

## Related Errors

- [PHP Warning: implode()]({{< relref "/languages/php/warning-in-implode" >}})
- [PHP Warning: array_diff()]({{< relref "/languages/php/warning-in-array-diff" >}})
- [PHP Warning: array_intersect()]({{< relref "/languages/php/warning-in-array-intersect" >}})
