---
title: "PHP Warning: array_reverse() expects exactly 1 argument"
description: "Fix PHP Warning: array_reverse() expects exactly 1 argument. Learn to pass a single array to array_reverse()."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# PHP Warning: array_reverse() expects exactly 1 argument

This warning occurs when `array_reverse()` is called with more than one argument. The function accepts only one array parameter and optionally a second boolean for preserving keys, but passing non-boolean extras triggers a warning.

## Common Causes

- Passing extra arguments beyond the array and optional preserve_keys flag
- Confusing `array_reverse()` with functions that accept multiple arrays
- Copy-pasting from multi-argument function calls

## How to Fix

### Pass One or Two Arguments Only

```php
<?php
// Wrong — extra argument
$reversed = array_reverse($arr, false, $extra);

// Correct — one argument
$reversed = array_reverse($arr);

// Or with preserve_keys
$reversed = array_reverse($arr, true);
?>
```

### Use Array Destructuring for Complex Reversals

```php
<?php
// Reverse multiple arrays separately
$a = array_reverse($first);
$b = array_reverse($second);
?>
```

## Examples

```php
<?php
// This triggers the warning
$fruits = ['apple', 'banana', 'cherry'];
$reversed = array_reverse($fruits, false, 'extra');
// Warning: array_reverse() expects exactly 1 parameter, 3 given

// Correct
$reversed = array_reverse($fruits); // ['cherry', 'banana', 'apple']
?>
```

## Related Errors

- [PHP Warning: array_flip()]({{< relref "/languages/php/warning-in-array-flip" >}})
- [PHP Warning: array_slice()]({{< relref "/languages/php/warning-in-array-slice" >}})
- [PHP Warning: array_splice()]({{< relref "/languages/php/warning-in-array-splice" >}})
