---
title: "PHP Warning: array_push() expects at least 2 arguments"
description: "Fix PHP Warning: array_push() expects at least 2 arguments. Learn to provide an array and at least one value to push."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["warning", "array-push", "array", "arguments"]
weight: 5
---

# PHP Warning: array_push() expects at least 2 arguments

This warning occurs when `array_push()` is called with fewer than 2 arguments. The function requires the array to push to, plus at least one value to add.

## Common Causes

- Calling `array_push()` with only the array and no values
- Passing the wrong number of arguments due to a coding mistake
- Forgetting that `array_push()` requires at least 2 arguments

## How to Fix

### Provide At Least Two Arguments

```php
<?php
// Wrong — only one argument
array_push($arr);

// Correct — array plus at least one value
array_push($arr, 'newitem');
?>
```

### Use Short Array Syntax Instead

```php
<?php
// More efficient — use [] instead of array_push()
$arr[] = 'newitem';
?>
```

### Push Multiple Values at Once

```php
<?php
// Push multiple values
array_push($arr, 'item1', 'item2', 'item3');
?>
```

## Examples

```php
<?php
// This triggers the warning
$fruits = ['apple'];
array_push($fruits);
// Warning: array_push() expects at least 2 arguments, 1 given

// Correct
array_push($fruits, 'banana'); // ['apple', 'banana']
$fruits[] = 'cherry'; // ['apple', 'banana', 'cherry']
?>
```

## Related Errors

- [PHP Warning: array_pop()]({{< relref "/languages/php/warning-in-array-pop" >}})
- [PHP Warning: array_shift()]({{< relref "/languages/php/warning-in-array-shift" >}})
- [PHP Warning: array_merge()]({{< relref "/languages/php/warning-in-array-merge" >}})
