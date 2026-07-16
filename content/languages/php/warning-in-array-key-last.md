---
title: "PHP Warning: array_key_last() expects exactly 1 argument"
description: "Fix PHP Warning: array_key_last() expects exactly 1 argument. Learn to use array_key_last() with a single array parameter."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["warning", "array-key-last", "array", "arguments"]
weight: 5
---

# PHP Warning: array_key_last() expects exactly 1 argument

This warning occurs when `array_key_last()` is called with more than one argument. The function accepts only one array parameter and returns the last key of that array without modifying it.

## Common Causes

- Passing extra arguments to `array_key_last()`
- Confusing `array_key_last()` with multi-argument functions
- Copy-pasting from function calls with additional parameters

## How to Fix

### Pass Exactly One Array

```php
<?php
// Wrong — extra argument
$key = array_key_last($arr, $extra);

// Correct
$key = array_key_last($arr);
?>
```

### Check the Return Value

```php
<?php
$key = array_key_last($arr);
if ($key !== null) {
    echo "Last key: " . $key;
}
?>
```

### Use end() as an Alternative

```php
<?php
// Alternative approach — end() returns the last value
$lastValue = end($arr);
// To get the key instead
$lastKey = key($arr);
?>
```

## Examples

```php
<?php
// This triggers the warning
$fruits = ['a' => 'apple', 'b' => 'banana', 'c' => 'cherry'];
$key = array_key_last($fruits, 'extra');
// Warning: array_key_last() expects exactly 1 parameter, 2 given

// Correct
$key = array_key_last($fruits); // 'c'
?>
```

## Related Errors

- [PHP Warning: array_key_first()]({{< relref "/languages/php/warning-in-array-key-first" >}})
- [PHP Warning: array_keys()]({{< relref "/languages/php/warning-in-array-keys" >}})
- [PHP Warning: array_reverse()]({{< relref "/languages/php/warning-in-array-reverse" >}})
