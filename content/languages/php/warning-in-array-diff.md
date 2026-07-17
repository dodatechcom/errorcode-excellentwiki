---
title: "PHP Warning: array_diff(): Arguments must be arrays"
description: "Fix PHP Warning: array_diff() arguments must be arrays. Learn to pass only arrays to array_diff()."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# PHP Warning: array_diff(): Arguments must be arrays

This warning occurs when `array_diff()` receives a non-array argument. All arguments passed to `array_diff()` must be arrays — the first is the array to compare, and the remaining are arrays to compare against.

## Common Causes

- Passing a scalar value or null instead of an array
- A variable that was expected to be an array but holds a different type
- Not checking function return values before using them in `array_diff()`

## How to Fix

### Validate All Arguments

```php
<?php
// Wrong — $exclude might not be an array
$diff = array_diff($data, $exclude);

// Correct — validate first
if (is_array($data) && is_array($exclude)) {
    $diff = array_diff($data, $exclude);
}
?>
```

### Use the Null Coalescing Operator

```php
<?php
$diff = array_diff($data ?? [], $exclude ?? []);
?>
```

### Ensure Database Results Are Arrays

```php
<?php
$result = $db->query($sql);
$data = $result ? $result->fetchAll() : [];
$diff = array_diff($data, $exclude);
?>
```

## Examples

```php
<?php
// This triggers the warning
$exclude = 'banana';
$diff = array_diff(['apple', 'banana', 'cherry'], $exclude);
// Warning: array_diff(): Arguments must be arrays

// Correct
$diff = array_diff(
    ['apple', 'banana', 'cherry'],
    ['banana']
); // ['apple', 'cherry']
?>
```

## Related Errors

- [PHP Warning: array_intersect()]({{< relref "/languages/php/warning-in-array-intersect" >}})
- [PHP Warning: array_merge()]({{< relref "/languages/php/warning-in-array-merge" >}})
- [PHP Warning: count()]({{< relref "/languages/php/warning-count" >}})
