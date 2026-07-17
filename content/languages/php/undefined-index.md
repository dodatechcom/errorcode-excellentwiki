---
title: "PHP Undefined array key \"X\""
description: "Fix PHP Undefined array key warning. Learn why this occurs and how to safely access array elements."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# PHP Undefined array key "X"

This notice (PHP 7) or warning (PHP 8) occurs when you access an array index that does not exist. In PHP 8.1+, this was elevated from a notice to a warning.

## Common Causes

- Accessing an index that was never set in the array
- Using a string key where a numeric index was expected (or vice versa)
- Variable used as index but contains an unexpected value
- Missing array element after filtering or array operations

## How to Fix

### Check Key Exists Before Access

```php
<?php
if (array_key_exists('name', $data)) {
    echo $data['name'];
}
?>
```

### Use isset() for Quick Check

```php
<?php
$value = isset($data['name']) ? $data['name'] : 'default';
?>
```

### Use the Null Coalescing Operator

```php
<?php
$value = $data['name'] ?? 'default';
?>
```

### Provide Default Array Values

```php
<?php
$defaults = ['name' => '', 'email' => '', 'age' => 0];
$data = array_merge($defaults, $userData);
echo $data['name'];
?>
```

## Examples

```php
<?php
// Example 1: Non-existent key
$colors = ['red', 'green', 'blue'];
echo $colors[3];
// Warning: Undefined array key 3
// Fix: check count($colors) > 3 or use isset()

// Example 2: String vs numeric key
$data = ['name' => 'John'];
echo $data[0];
// Warning: Undefined array key 0
// Fix: use $data['name'] instead

// Example 3: After filtering
$items = [1 => 'a', 2 => 'b', 3 => 'c'];
$filtered = array_filter($items, fn($v) => $v !== 'b');
echo $filtered[2];
// Warning: Undefined array key 2
// Fix: use isset($filtered[2]) or array_values($filtered)
?>
```

## Related Errors

- [PHP array_key_exists(): Argument #2 must be of type array]({{< relref "/languages/php/array-key-exists" >}})
- [PHP Notice: Undefined Variable]({{< relref "/languages/php/notice-undefined-variable" >}})
- [PHP Warning: Trying to get property of non-object]({{< relref "/languages/php/trying-to-get-property" >}})
