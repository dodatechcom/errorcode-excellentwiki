---
title: "PHP Warning: array_walk() expects at least 2 arguments"
description: "Fix PHP Warning: array_walk() expects at least 2 arguments. Learn to provide the array and callback to array_walk()."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["warning", "array-walk", "array", "callback"]
weight: 5
---

# PHP Warning: array_walk() expects at least 2 arguments

This warning occurs when `array_walk()` is called with fewer than 2 arguments. The function requires at least the array to walk and a callback function to apply to each element.

## Common Causes

- Calling `array_walk()` with only the array and no callback
- Forgetting that the callback parameter is mandatory
- Passing the wrong number of arguments

## How to Fix

### Provide At Least Two Arguments

```php
<?php
// Wrong — missing callback
array_walk($arr);

// Correct — array and callback
array_walk($arr, function (&$value, $key) {
    $value = strtoupper($value);
});
?>
```

### Use array_map() Instead

```php
<?php
// array_map returns a new array instead of modifying in place
$result = array_map('strtoupper', $arr);
?>
```

### Use a User-Defined Function

```php
<?php
function capitalize(&$value, $key) {
    $value = ucfirst($value);
}

$names = ['alice', 'bob', 'charlie'];
array_walk($names, 'capitalize');
// $names is now ['Alice', 'Bob', 'Charlie']
?>
```

## Examples

```php
<?php
// This triggers the warning
$fruits = ['apple', 'banana', 'cherry'];
array_walk($fruits);
// Warning: array_walk() expects at least 2 parameters, 1 given

// Correct
array_walk($fruits, function (&$fruit) {
    $fruit = strtoupper($fruit);
});
// $fruits is now ['APPLE', 'BANANA', 'CHERRY']
?>
```

## Related Errors

- [PHP Warning: array_map()]({{< relref "/languages/php/warning-in-array-map" >}})
- [PHP Warning: array_filter()]({{< relref "/languages/php/warning-in-array-filter" >}})
- [PHP Warning: array_reduce()]({{< relref "/languages/php/warning-in-array-reduce" >}})
