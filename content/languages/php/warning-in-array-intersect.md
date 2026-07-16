---
title: "PHP Warning: array_intersect(): Arguments must be arrays"
description: "Fix PHP Warning: array_intersect() arguments must be arrays. Learn to pass valid arrays to array_intersect()."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["warning", "array-intersect", "array", "arguments"]
weight: 5
---

# PHP Warning: array_intersect(): Arguments must be arrays

This warning occurs when `array_intersect()` receives a non-array argument. All arguments must be arrays — the first is the array to compare, and the rest are arrays to intersect with.

## Common Causes

- Passing a scalar value or null as one of the arguments
- A variable that was expected to be an array but holds a different type
- Not checking function return values before using them in `array_intersect()`

## How to Fix

### Validate All Arguments

```php
<?php
// Wrong — $filter might not be an array
$result = array_intersect($data, $filter);

// Correct — validate first
if (is_array($data) && is_array($filter)) {
    $result = array_intersect($data, $filter);
}
?>
```

### Use the Null Coalescing Operator

```php
<?php
$result = array_intersect($data ?? [], $filter ?? []);
?>
```

### Wrap Non-Array Values

```php
<?php
// If $filter might not be an array
$filterArr = is_array($filter) ? $filter : [$filter];
$result = array_intersect($data, $filterArr);
?>
```

## Examples

```php
<?php
// This triggers the warning
$allowed = null;
$result = array_intersect(['a', 'b', 'c'], $allowed);
// Warning: array_intersect(): Arguments must be arrays

// Correct
$result = array_intersect(['a', 'b', 'c'], ['b', 'c', 'd']); // ['b', 'c']
?>
```

## Related Errors

- [PHP Warning: array_diff()]({{< relref "/languages/php/warning-in-array-diff" >}})
- [PHP Warning: array_merge()]({{< relref "/languages/php/warning-in-array-merge" >}})
- [PHP Warning: in_array()]({{< relref "/languages/php/warning-in-in-array" >}})
