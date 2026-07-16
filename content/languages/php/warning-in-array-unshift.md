---
title: "PHP Warning: array_unshift() expects at least 2 arguments"
description: "Fix PHP Warning: array_unshift() expects at least 2 arguments. Learn to provide an array and values to prepend."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["warning", "array-unshift", "array", "arguments"]
weight: 5
---

# PHP Warning: array_unshift() expects at least 2 arguments

This warning occurs when `array_unshift()` is called with fewer than 2 arguments. The function requires the array to modify plus at least one value to prepend.

## Common Causes

- Calling `array_unshift()` with only the array and no values to prepend
- Forgetting that the function needs at least one value argument
- Using the function without providing elements to add

## How to Fix

### Provide At Least Two Arguments

```php
<?php
// Wrong — only one argument
array_unshift($arr);

// Correct — array plus at least one value
array_unshift($arr, 'newitem');
?>
```

### Prepend Multiple Values

```php
<?php
// Prepend multiple values at once
array_unshift($arr, 'first', 'second', 'third');
?>
```

### Use array_merge() as an Alternative

```php
<?php
// Alternative approach
$arr = array_merge(['newitem'], $arr);
?>
```

## Examples

```php
<?php
// This triggers the warning
$fruits = ['banana', 'cherry'];
array_unshift($fruits);
// Warning: array_unshift() expects at least 2 parameters, 1 given

// Correct
array_unshift($fruits, 'apple'); // ['apple', 'banana', 'cherry']
?>
```

## Related Errors

- [PHP Warning: array_shift()]({{< relref "/languages/php/warning-in-array-shift" >}})
- [PHP Warning: array_push()]({{< relref "/languages/php/warning-in-array-push" >}})
- [PHP Warning: array_merge()]({{< relref "/languages/php/warning-in-array-merge" >}})
