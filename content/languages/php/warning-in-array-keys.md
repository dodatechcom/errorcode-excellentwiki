---
title: "PHP Warning: array_keys() expects at least 1 argument"
description: "Fix PHP Warning: array_keys() expects at least 1 argument. Learn to pass a valid array to array_keys()."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["warning", "array-keys", "array", "arguments"]
weight: 5
---

# PHP Warning: array_keys() expects at least 1 argument

This warning occurs when `array_keys()` is called with no arguments. The function requires at least one argument — the array whose keys you want to retrieve.

## Common Causes

- Calling `array_keys()` without any arguments
- Passing an undefined or null variable instead of an array
- Forgetting that the function requires at least the array parameter

## How to Fix

### Provide At Least One Argument

```php
<?php
// Wrong — no arguments
$keys = array_keys();

// Correct — pass an array
$keys = array_keys(['a' => 1, 'b' => 2]);
?>
```

### Validate Before Calling

```php
<?php
$keys = is_array($data) ? array_keys($data) : [];
?>
```

### Use the Null Coalescing Operator

```php
<?php
$keys = array_keys($data ?? []);
?>
```

## Examples

```php
<?php
// This triggers the warning
$keys = array_keys();
// Warning: array_keys() expects at least 1 parameter, 0 given

// Correct
$person = ['name' => 'Alice', 'age' => 30];
$keys = array_keys($person); // ['name', 'age']
?>
```

## Related Errors

- [PHP Warning: array_values()]({{< relref "/languages/php/warning-in-array-values" >}})
- [PHP Warning: array_flip()]({{< relref "/languages/php/warning-in-array-flip" >}})
- [PHP Warning: array_key_first()]({{< relref "/languages/php/warning-in-array-key-first" >}})
