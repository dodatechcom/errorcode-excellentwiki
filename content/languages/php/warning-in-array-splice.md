---
title: "PHP Warning: array_splice() expects at least 3 arguments"
description: "Fix PHP Warning: array_splice() expects at least 3 arguments. Learn the correct parameter order for array_splice()."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["warning", "array-splice", "array", "arguments"]
weight: 5
---

# PHP Warning: array_splice() expects at least 3 arguments

This warning occurs when `array_splice()` is called with fewer than 3 arguments. The function requires the array, offset, and length parameters at minimum.

## Common Causes

- Calling `array_splice()` without the required length parameter
- Passing only the array and offset
- Forgetting the minimum parameter requirements

## How to Fix

### Provide At Least Three Arguments

```php
<?php
// Wrong — missing length parameter
array_splice($arr, 1);

// Correct — array, offset, and length
array_splice($arr, 1, 1);
?>
```

### Use Zero Length to Insert

```php
<?php
// Insert without removing elements
array_splice($arr, 1, 0, ['newitem']);
?>
```

### Remove from Offset to End

```php
<?php
// Remove from offset 2 to the end of the array
array_splice($arr, 2, count($arr));
?>
```

## Examples

```php
<?php
// This triggers the warning
$fruits = ['apple', 'banana', 'cherry'];
array_splice($fruits, 1);
// Warning: array_splice() expects at least 3 parameters, 2 given

// Correct — remove 1 element at index 1
array_splice($fruits, 1, 1); // ['apple', 'cherry']
?>
```

## Related Errors

- [PHP Warning: array_slice()]({{< relref "/languages/php/warning-in-array-slice" >}})
- [PHP Warning: array_pop()]({{< relref "/languages/php/warning-in-array-pop" >}})
- [PHP Warning: array_shift()]({{< relref "/languages/php/warning-in-array-shift" >}})
