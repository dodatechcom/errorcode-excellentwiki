---
title: "PHP Warning: array_slice() expects at least 2 arguments"
description: "Fix PHP Warning: array_slice() expects at least 2 arguments. Learn to provide the required offset parameter."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["warning", "array-slice", "array", "arguments"]
weight: 5
---

# PHP Warning: array_slice() expects at least 2 arguments

This warning occurs when `array_slice()` is called with only one argument. The function requires at least the array and offset parameters.

## Common Causes

- Calling `array_slice()` with only the array parameter
- Forgetting that the offset parameter is mandatory
- Confusing with functions that accept a single array argument

## How to Fix

### Provide At Least Two Arguments

```php
<?php
// Wrong — missing offset
$slice = array_slice($arr);

// Correct — array and offset
$slice = array_slice($arr, 0);
?>
```

### Slice from the Beginning

```php
<?php
// Get first 3 elements
$slice = array_slice($arr, 0, 3);
?>
```

### Slice from the End

```php
<?php
// Get last 2 elements
$slice = array_slice($arr, -2);
?>
```

## Examples

```php
<?php
// This triggers the warning
$fruits = ['apple', 'banana', 'cherry', 'date'];
$slice = array_slice($fruits);
// Warning: array_slice() expects at least 2 parameters, 1 given

// Correct
$slice = array_slice($fruits, 1, 2); // ['banana', 'cherry']
?>
```

## Related Errors

- [PHP Warning: array_splice()]({{< relref "/languages/php/warning-in-array-splice" >}})
- [PHP Warning: array_merge()]({{< relref "/languages/php/warning-in-array-merge" >}})
- [PHP Warning: count()]({{< relref "/languages/php/warning-count" >}})
