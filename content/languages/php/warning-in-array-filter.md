---
title: "PHP Warning: array_filter() expects at least 1 argument"
description: "Fix PHP Warning: array_filter() expects at least 1 argument. Learn to pass a valid array to array_filter()."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# PHP Warning: array_filter() expects at least 1 argument

This warning occurs when `array_filter()` is called with no arguments. The function requires at least one argument — the array to filter.

## Common Causes

- Calling `array_filter()` without any arguments
- Passing an undefined or null variable as the array
- Forgetting that the first parameter is mandatory

## How to Fix

### Provide At Least One Argument

```php
<?php
// Wrong — no arguments
$filtered = array_filter();

// Correct — pass an array
$filtered = array_filter([1, 2, 3, 4, 5]);
?>
```

### Validate Before Calling

```php
<?php
$filtered = is_array($data) ? array_filter($data) : [];
?>
```

### Use the Null Coalescing Operator

```php
<?php
$filtered = array_filter($data ?? []);
?>
```

## Examples

```php
<?php
// This triggers the warning
$filtered = array_filter();
// Warning: array_filter() expects at least 1 parameter, 0 given

// Correct
$numbers = [1, 2, 3, 4, 5];
$even = array_filter($numbers, fn($n) => $n % 2 === 0); // [2, 4]
?>
```

## Related Errors

- [PHP Warning: array_map()]({{< relref "/languages/php/warning-in-array-map" >}})
- [PHP Warning: array_reduce()]({{< relref "/languages/php/warning-in-array-reduce" >}})
- [PHP Warning: count()]({{< relref "/languages/php/warning-count" >}})
