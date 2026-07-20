---
title: "PHP Warning: array_merge() / array_diff() type mismatch"
description: "Fix PHP Warning: array_merge and array_diff type mismatch. Learn to ensure arrays are proper type, handle mixed types, and validate input."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# PHP Warning: array_merge() / array_diff() type mismatch

This warning occurs when `array_merge()`, `array_diff()`, or similar array functions receive non-array arguments. These functions expect all parameters to be arrays.

## Common Causes

- Passing null values instead of arrays
- Passing scalar values or objects
- Confusion between function parameter orders

## How to Fix

### Ensure Arrays are Proper Type

```php
<?php
// Wrong — non-array passed
$result = array_merge($arr1, $arr2);

// Correct — cast or default
$result = array_merge((array) $arr1, (array) $arr2);
?>
```

### Handle Mixed Types

```php
<?php
// Wrong — variable may not be an array
$result = array_merge($arr1, $arr2);

// Correct — ensure both are arrays
$arr1 = is_array($arr1) ? $arr1 : [];
$arr2 = is_array($arr2) ? $arr2 : [];
$result = array_merge($arr1, $arr2);
?>
```

### Validate Input

```php
<?php
// Wrong — no validation
$diff = array_diff($a, $b);

// Correct — check before using
if (is_array($a) && is_array($b)) {
    $diff = array_diff($a, $b);
}
?>
```

## Examples

```php
<?php
// This triggers the warning
$arr1 = ['a', 'b'];
$arr2 = null;
$result = array_merge($arr1, $arr2);
// Warning: array_merge(): Argument #2 is not an array

// Correct
$result = array_merge($arr1, $arr2 ?? []);
$result = array_merge($arr1, is_array($arr2) ? $arr2 : []);
?>
```

## Related Errors

- [PHP Warning: array_diff()]({{< relref "/languages/php/warning-in-array-diff" >}})
- [PHP Warning: array_merge()]({{< relref "/languages/php/warning-in-array-merge" >}})
- [PHP Warning: array_intersect()]({{< relref "/languages/php/warning-in-array-intersect" >}})
