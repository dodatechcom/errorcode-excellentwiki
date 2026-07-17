---
title: "PHP Warning: array_values() expects exactly 1 argument"
description: "Fix PHP Warning: array_values() expects exactly 1 argument. Learn to use array_values() with a single array parameter."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# PHP Warning: array_values() expects exactly 1 argument

This warning occurs when `array_values()` is called with more than one argument. The function accepts only one array parameter and returns all the values from that array.

## Common Causes

- Passing extra arguments to `array_values()`
- Confusing `array_values()` with multi-argument functions
- Copy-pasting from function calls that accept multiple parameters

## How to Fix

### Pass Exactly One Array

```php
<?php
// Wrong — extra argument
$values = array_values($arr, $extra);

// Correct
$values = array_values($arr);
?>
```

### Use array_column() for Nested Arrays

```php
<?php
// Extract a specific column from nested arrays
$names = array_column($users, 'name');
?>
```

## Examples

```php
<?php
// This triggers the warning
$person = ['name' => 'Alice', 'age' => 30];
$values = array_values($person, 'extra');
// Warning: array_values() expects exactly 1 parameter, 2 given

// Correct
$values = array_values($person); // ['Alice', 30]
?>
```

## Related Errors

- [PHP Warning: array_keys()]({{< relref "/languages/php/warning-in-array-keys" >}})
- [PHP Warning: array_column()]({{< relref "/languages/php/warning-in-array-column" >}})
- [PHP Warning: array_flip()]({{< relref "/languages/php/warning-in-array-flip" >}})
