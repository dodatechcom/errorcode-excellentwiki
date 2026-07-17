---
title: "PHP Warning: array_shift() expects exactly 1 argument"
description: "Fix PHP Warning: array_shift() expects exactly 1 argument. Learn to use array_shift() with a single array parameter."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# PHP Warning: array_shift() expects exactly 1 argument

This warning occurs when `array_shift()` is called with more than one argument. The function accepts only a single array parameter and removes the first element from it.

## Common Causes

- Passing extra arguments beyond the array parameter
- Confusing `array_shift()` with functions that accept multiple parameters
- Copy-pasting from functions with different signatures

## How to Fix

### Pass Exactly One Array Argument

```php
<?php
// Wrong — extra argument
$first = array_shift($arr, $extra);

// Correct
$first = array_shift($arr);
?>
```

### Use array_slice() for Bulk Removal

```php
<?php
// Remove multiple elements from the beginning
$count = 2;
$removed = array_slice($arr, 0, $count);
$arr = array_slice($arr, $count);
?>
```

## Examples

```php
<?php
// This triggers the warning
$fruits = ['apple', 'banana', 'cherry'];
$first = array_shift($fruits, 'extra');
// Warning: array_shift() expects exactly 1 parameter, 2 given

// Correct
$first = array_shift($fruits); // 'apple', $fruits is now ['banana', 'cherry']
?>
```

## Related Errors

- [PHP Warning: array_pop()]({{< relref "/languages/php/warning-in-array-pop" >}})
- [PHP Warning: array_push()]({{< relref "/languages/php/warning-in-array-push" >}})
- [PHP Warning: array_splice()]({{< relref "/languages/php/warning-in-array-splice" >}})
