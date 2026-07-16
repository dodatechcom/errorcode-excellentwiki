---
title: "PHP Warning: implode(): Invalid arguments"
description: "Fix PHP Warning: implode() invalid arguments. Learn the correct parameter order and types for implode()."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["warning", "implode", "array", "join"]
weight: 5
---

# PHP Warning: implode(): Invalid arguments

This warning occurs when `implode()` receives incorrect arguments — either the wrong parameter order, non-array input, or invalid types. The function joins array elements into a string using a glue separator.

## Common Causes

- Passing arguments in the wrong order (separator, array) instead of (glue, array)
- Passing a non-array value as the array parameter
- Passing `null` or an empty array without proper handling

## How to Fix

### Use the Correct Parameter Order

```php
<?php
// Wrong — reversed parameters
echo implode($array, ", ");

// Correct — glue first, then array
echo implode(", ", $array);
?>
```

### Validate the Array Input

```php
<?php
// Wrong — might not be an array
echo implode(", ", $data);

// Correct
if (is_array($data)) {
    echo implode(", ", $data);
}
?>
```

### Use the Null Coalescing Operator

```php
<?php
echo implode(", ", $data ?? []);
?>
```

## Examples

```php
<?php
// This triggers the warning
echo implode(", ", null);
// Warning: implode(): Invalid arguments

// This triggers the warning
echo implode([1, 2, 3], ", ");

// Correct
$fruits = ['apple', 'banana', 'cherry'];
echo implode(", ", $fruits); // apple, banana, cherry
?>
```

## Related Errors

- [PHP Warning: join()]({{< relref "/languages/php/warning-in-join" >}})
- [PHP Warning: array_merge()]({{< relref "/languages/php/warning-in-array-merge" >}})
- [PHP Warning: strlen()]({{< relref "/languages/php/warning-in-strlen" >}})
