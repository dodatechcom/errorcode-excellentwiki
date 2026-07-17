---
title: "PHP Warning: array_any() expects exactly 1 argument"
description: "Fix PHP Warning: array_any() expects exactly 1 argument. Learn to use array_any() with a single array parameter."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# PHP Warning: array_any() expects exactly 1 argument

This warning occurs when `array_any()` is called with more than one argument. The function accepts only one array parameter and returns `true` if any element satisfies the callback condition (PHP 8.4+).

## Common Causes

- Passing extra arguments to `array_any()`
- Confusing `array_any()` with multi-argument functions
- Using the function on a PHP version that does not support it

## How to Fix

### Pass Exactly One Array

```php
<?php
// Wrong — extra argument
$result = array_any($arr, $callback, $extra);

// Correct
$result = array_any($arr, $callback);
?>
```

### Use array_filter() for Older PHP Versions

```php
<?php
// For PHP < 8.4
function hasAny(array $arr, callable $callback): bool {
    return count(array_filter($arr, $callback)) > 0;
}
?>
```

### Check the Callback Return Value

```php
<?php
$numbers = [1, 2, 3, 4, 5];
$hasEven = array_any($numbers, fn($n) => $n % 2 === 0); // true
?>
```

## Examples

```php
<?php
// This triggers the warning (PHP 8.4+)
$numbers = [1, 3, 5, 7];
$result = array_any($numbers, fn($n) => $n % 2 === 0, 'extra');
// Warning: array_any() expects exactly 1 parameter, 3 given

// Correct
$result = array_any($numbers, fn($n) => $n % 2 === 0); // false
?>
```

## Related Errors

- [PHP Warning: array_all()]({{< relref "/languages/php/warning-in-array-all" >}})
- [PHP Warning: array_filter()]({{< relref "/languages/php/warning-in-array-filter" >}})
- [PHP Warning: array_map()]({{< relref "/languages/php/warning-in-array-map" >}})
