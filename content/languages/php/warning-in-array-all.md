---
title: "PHP Warning: array_all() expects exactly 1 argument"
description: "Fix PHP Warning: array_all() expects exactly 1 argument. Learn to use array_all() with a single array parameter."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["warning", "array-all", "array", "arguments"]
weight: 5
---

# PHP Warning: array_all() expects exactly 1 argument

This warning occurs when `array_all()` is called with more than one argument. The function accepts only one array parameter and returns `true` if all elements satisfy the callback condition (PHP 8.4+).

## Common Causes

- Passing extra arguments to `array_all()`
- Confusing `array_all()` with multi-argument functions
- Using the function on a PHP version that does not support it

## How to Fix

### Pass Exactly One Array

```php
<?php
// Wrong — extra argument
$result = array_all($arr, $callback, $extra);

// Correct
$result = array_all($arr, $callback);
?>
```

### Use array_filter() for Older PHP Versions

```php
<?php
// For PHP < 8.4
function allMatch(array $arr, callable $callback): bool {
    return count(array_filter($arr, $callback)) === count($arr);
}
?>
```

### Check the Callback Return Value

```php
<?php
$numbers = [2, 4, 6, 8];
$allEven = array_all($numbers, fn($n) => $n % 2 === 0); // true
?>
```

## Examples

```php
<?php
// This triggers the warning (PHP 8.4+)
$numbers = [2, 4, 5, 8];
$result = array_all($numbers, fn($n) => $n % 2 === 0, 'extra');
// Warning: array_all() expects exactly 1 parameter, 3 given

// Correct
$result = array_all($numbers, fn($n) => $n % 2 === 0); // false (5 is odd)
?>
```

## Related Errors

- [PHP Warning: array_any()]({{< relref "/languages/php/warning-in-array-any" >}})
- [PHP Warning: array_filter()]({{< relref "/languages/php/warning-in-array-filter" >}})
- [PHP Warning: array_reduce()]({{< relref "/languages/php/warning-in-array-reduce" >}})
