---
title: "PHP Warning: array_column() expects at least 2 arguments"
description: "Fix PHP Warning: array_column() expects at least 2 arguments. Learn to provide the required column key parameter."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["warning", "array-column", "array", "arguments"]
weight: 5
---

# PHP Warning: array_column() expects at least 2 arguments

This warning occurs when `array_column()` is called with fewer than 2 arguments. The function requires the input array and the column key to extract, with an optional third argument for the index key.

## Common Causes

- Calling `array_column()` with only the array and no column key
- Forgetting the second mandatory parameter
- Passing `null` where a column key string is expected

## How to Fix

### Provide At Least Two Arguments

```php
<?php
// Wrong — missing column key
$names = array_column($users);

// Correct — array and column key
$names = array_column($users, 'name');
?>
```

### Use array_map() as an Alternative

```php
<?php
// Extract a column using array_map
$names = array_map(fn($user) => $user['name'], $users);
?>
```

### Extract with Index Key

```php
<?php
// Third argument sets the index key
$byId = array_column($users, 'name', 'id');
?>
```

## Examples

```php
<?php
// This triggers the warning
$users = [
    ['id' => 1, 'name' => 'Alice'],
    ['id' => 2, 'name' => 'Bob'],
];
$names = array_column($users);
// Warning: array_column() expects at least 2 parameters, 1 given

// Correct
$names = array_column($users, 'name'); // ['Alice', 'Bob']
?>
```

## Related Errors

- [PHP Warning: array_map()]({{< relref "/languages/php/warning-in-array-map" >}})
- [PHP Warning: array_values()]({{< relref "/languages/php/warning-in-array-values" >}})
- [PHP Warning: array_keys()]({{< relref "/languages/php/warning-in-array-keys" >}})
