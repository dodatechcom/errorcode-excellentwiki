---
title: "PHP Warning: array_reduce() expects at least 2 arguments"
description: "Fix PHP Warning: array_reduce() expects at least 2 arguments. Learn to provide the array and callback to array_reduce()."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# PHP Warning: array_reduce() expects at least 2 arguments

This warning occurs when `array_reduce()` is called with fewer than 2 arguments. The function requires at least the array and a callback function to reduce the array to a single value.

## Common Causes

- Calling `array_reduce()` with only the array and no callback
- Forgetting that the callback parameter is mandatory
- Passing the wrong number of arguments

## How to Fix

### Provide At Least Two Arguments

```php
<?php
// Wrong — missing callback
$result = array_reduce($arr);

// Correct — array and callback
$result = array_reduce($arr, function ($carry, $item) {
    return $carry + $item;
});
?>
```

### Use array_sum() for Simple Summation

```php
<?php
// Instead of array_reduce for summing
$sum = array_sum($numbers);
?>
```

### Use an Initial Value

```php
<?php
// Third argument sets the initial value
$result = array_reduce($arr, function ($carry, $item) {
    return $carry . $item;
}, '');
?>
```

## Examples

```php
<?php
// This triggers the warning
$numbers = [1, 2, 3, 4, 5];
$result = array_reduce($numbers);
// Warning: array_reduce() expects at least 2 parameters, 1 given

// Correct
$result = array_reduce($numbers, fn($carry, $item) => $carry + $item, 0); // 15
?>
```

## Related Errors

- [PHP Warning: array_filter()]({{< relref "/languages/php/warning-in-array-filter" >}})
- [PHP Warning: array_map()]({{< relref "/languages/php/warning-in-array-map" >}})
- [PHP Warning: array_walk()]({{< relref "/languages/php/warning-in-array-walk" >}})
