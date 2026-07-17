---
title: "PHP Warning: Invalid argument supplied for foreach()"
description: "Fix PHP Warning: Invalid argument supplied for foreach(). Learn to ensure variables are arrays before iterating."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# PHP Warning: Invalid argument supplied for foreach()

This warning occurs when you use `foreach` on a variable that is not an array or an object that implements `Traversable`. PHP cannot iterate over scalar values, `null`, or non-iterable types.

## Common Causes

- Using `foreach` on a variable that is `null` or not an array
- A function returning a non-array value when an array was expected
- Database query returning `false` instead of an array

## How to Fix

### Validate Before Iterating

```php
<?php
// Wrong
foreach ($data as $item) { ... }

// Correct
if (is_array($data)) {
    foreach ($data as $item) { ... }
}
?>
```

### Use the Null Coalescing Operator

```php
<?php
foreach ($data ?? [] as $item) {
    echo $item;
}
?>
```

### Check Function Return Values

```php
<?php
$result = mysqli_query($conn, $query);
if ($result) {
    while ($row = mysqli_fetch_assoc($result)) {
        echo $row['name'];
    }
}
?>
```

## Examples

```php
<?php
// This triggers the warning
$data = null;
foreach ($data as $item) {
    echo $item;
}
// Warning: Invalid argument supplied for foreach()

// Correct
$data = [1, 2, 3];
foreach ($data as $item) {
    echo $item . "\n";
}
?>
```

## Related Errors

- [PHP Warning: count()]({{< relref "/languages/php/warning-count" >}})
- [PHP Warning: in_array()]({{< relref "/languages/php/warning-in-in-array" >}})
- [PHP Notice: Undefined Variable]({{< relref "/languages/php/notice-undefined-variable" >}})
