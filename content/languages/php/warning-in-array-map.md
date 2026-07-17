---
title: "PHP Warning: array_map(): Argument #2 is not an array"
description: "Fix PHP Warning: array_map() argument #2 is not an array. Learn to pass valid arrays to array_map()."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# PHP Warning: array_map(): Argument #2 is not an array

This warning occurs when the second argument (or subsequent arguments after the callback) to `array_map()` is not an array. The function requires at least one array to iterate over.

## Common Causes

- Passing a non-array variable as the second argument
- A function returning a non-array value when an array was expected
- Using `null` or a scalar value instead of an array

## How to Fix

### Validate the Input Array

```php
<?php
// Wrong — $data might not be an array
$result = array_map('strtoupper', $data);

// Correct — validate first
if (is_array($data)) {
    $result = array_map('strtoupper', $data);
}
?>
```

### Use the Null Coalescing Operator

```php
<?php
$result = array_map('strtoupper', $data ?? []);
?>
```

### Use array_values() for Safety

```php
<?php
// Ensure the result is always an array
$result = array_values(array_map('strtoupper', $data ?? []));
?>
```

## Examples

```php
<?php
// This triggers the warning
$data = null;
$result = array_map('strtoupper', $data);
// Warning: array_map(): Argument #2 is not an array

// Correct
$result = array_map('strtoupper', ['hello', 'world']); // ['HELLO', 'WORLD']
?>
```

## Related Errors

- [PHP Warning: array_filter()]({{< relref "/languages/php/warning-in-array-filter" >}})
- [PHP Warning: array_column()]({{< relref "/languages/php/warning-in-array-column" >}})
- [PHP Warning: foreach()]({{< relref "/languages/php/warning-in-foreach" >}})
