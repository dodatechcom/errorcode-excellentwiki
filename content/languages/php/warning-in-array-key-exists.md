---
title: "PHP Warning: array_key_exists(): The second argument should be either an array or an object"
description: "Fix PHP Warning: array_key_exists() second argument. Learn to validate inputs before checking array keys."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# PHP Warning: array_key_exists(): The second argument should be either an array or an object

This warning occurs when the second argument to `array_key_exists()` is not an array or an object with the `ArrayAccess` interface. The function needs a valid array-like structure to search for the key.

## Common Causes

- Passing `null`, a string, or a scalar type as the second argument
- Using a variable that was reassigned to a non-array value
- Accessing a property that does not return an array

## How to Fix

### Validate the Second Argument

```php
<?php
// Wrong — $data might not be an array
if (array_key_exists('name', $data)) { ... }

// Correct — validate first
if (is_array($data) && array_key_exists('name', $data)) { ... }
?>
```

### Use isset() as an Alternative

```php
<?php
// isset() works on arrays and avoids some warnings
if (isset($data['name'])) {
    echo $data['name'];
}
?>
```

### Check with null Coalescing

```php
<?php
$value = $data['name'] ?? null;
?>
```

## Examples

```php
<?php
// This triggers the warning
$data = null;
echo array_key_exists('name', $data);
// Warning: array_key_exists(): The second argument should be either an array or an object

// Correct
$data = ['name' => 'Alice'];
echo array_key_exists('name', $data); // 1 (true)
?>
```

## Related Errors

- [PHP Warning: array_key_first()]({{< relref "/languages/php/warning-in-array-key-first" >}})
- [PHP Warning: array_key_last()]({{< relref "/languages/php/warning-in-array-key-last" >}})
- [PHP Notice: Undefined Index]({{< relref "/languages/php/notice-undefined-index" >}})
