---
title: "PHP Warning: array_flip() expects exactly 1 argument"
description: "Fix PHP Warning: array_flip() expects exactly 1 argument. Learn to use array_flip() with a single array parameter."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["warning", "array-flip", "array", "arguments"]
weight: 5
---

# PHP Warning: array_flip() expects exactly 1 argument

This warning occurs when `array_flip()` is called with more than one argument. The function accepts only one array parameter and exchanges all keys with their associated values.

## Common Causes

- Passing extra arguments to `array_flip()`
- Confusing `array_flip()` with multi-argument array functions
- Copy-pasting function calls without removing extra parameters

## How to Fix

### Pass Exactly One Array

```php
<?php
// Wrong — extra argument
$flipped = array_flip($arr, $extra);

// Correct
$flipped = array_flip($arr);
?>
```

### Use array_combine() as an Alternative

```php
<?php
// Flip keys and values manually
$values = array_values($arr);
$keys = array_keys($arr);
$flipped = array_combine($values, $keys);
?>
```

## Examples

```php
<?php
// This triggers the warning
$fruits = ['a' => 'apple', 'b' => 'banana'];
$flipped = array_flip($fruits, 'extra');
// Warning: array_flip() expects exactly 1 parameter, 2 given

// Correct
$flipped = array_flip($fruits); // ['apple' => 'a', 'banana' => 'b']
?>
```

## Related Errors

- [PHP Warning: array_reverse()]({{< relref "/languages/php/warning-in-array-reverse" >}})
- [PHP Warning: array_keys()]({{< relref "/languages/php/warning-in-array-keys" >}})
- [PHP Warning: array_values()]({{< relref "/languages/php/warning-in-array-values" >}})
