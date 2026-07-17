---
title: "PHP Warning: array_key_first() expects exactly 1 argument"
description: "Fix PHP Warning: array_key_first() expects exactly 1 argument. Learn to use array_key_first() with a single array parameter."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# PHP Warning: array_key_first() expects exactly 1 argument

This warning occurs when `array_key_first()` is called with more than one argument. The function accepts only one array parameter and returns the first key of that array without modifying it.

## Common Causes

- Passing extra arguments to `array_key_first()`
- Confusing `array_key_first()` with multi-argument functions
- Copy-pasting from function calls with additional parameters

## How to Fix

### Pass Exactly One Array

```php
<?php
// Wrong — extra argument
$key = array_key_first($arr, $extra);

// Correct
$key = array_key_first($arr);
?>
```

### Check the Return Value

```php
<?php
$key = array_key_first($arr);
if ($key !== null) {
    echo "First key: " . $key;
}
?>
```

### Use reset() for Older PHP Versions

```php
<?php
// For PHP < 7.3
$key = key($arr);
?>
```

## Examples

```php
<?php
// This triggers the warning
$fruits = ['a' => 'apple', 'b' => 'banana'];
$key = array_key_first($fruits, 'extra');
// Warning: array_key_first() expects exactly 1 parameter, 2 given

// Correct
$key = array_key_first($fruits); // 'a'
?>
```

## Related Errors

- [PHP Warning: array_key_last()]({{< relref "/languages/php/warning-in-array-key-last" >}})
- [PHP Warning: array_keys()]({{< relref "/languages/php/warning-in-array-keys" >}})
- [PHP Warning: array_key_exists()]({{< relref "/languages/php/warning-in-array-key-exists" >}})
