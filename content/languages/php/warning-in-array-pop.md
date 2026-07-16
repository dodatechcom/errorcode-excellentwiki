---
title: "PHP Warning: array_pop() expects exactly 1 argument"
description: "Fix PHP Warning: array_pop() expects exactly 1 argument. Learn to use array_pop() with a single array parameter."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["warning", "array-pop", "array", "arguments"]
weight: 5
---

# PHP Warning: array_pop() expects exactly 1 argument

This warning occurs when `array_pop()` is called with more than one argument. The function accepts only a single array parameter and removes the last element from it.

## Common Causes

- Accidentally passing extra arguments to `array_pop()`
- Confusing `array_pop()` with other array functions that take multiple arguments
- Copy-pasting function calls without adjusting parameters

## How to Fix

### Pass Exactly One Array Argument

```php
<?php
// Wrong — extra argument
$last = array_pop($arr, $extra);

// Correct
$last = array_pop($arr);
?>
```

### Use array_slice() for Multiple Elements

```php
<?php
// To remove multiple elements from the end
$count = 3;
$slice = array_slice($arr, 0, -$count);
$removed = array_slice($arr, -$count);
$arr = $slice;
?>
```

## Examples

```php
<?php
// This triggers the warning
$fruits = ['apple', 'banana', 'cherry'];
$last = array_pop($fruits, 'extra');
// Warning: array_pop() expects exactly 1 parameter, 2 given

// Correct
$last = array_pop($fruits); // 'cherry', $fruits is now ['apple', 'banana']
?>
```

## Related Errors

- [PHP Warning: array_push()]({{< relref "/languages/php/warning-in-array-push" >}})
- [PHP Warning: array_shift()]({{< relref "/languages/php/warning-in-array-shift" >}})
- [PHP Warning: array_splice()]({{< relref "/languages/php/warning-in-array-splice" >}})
