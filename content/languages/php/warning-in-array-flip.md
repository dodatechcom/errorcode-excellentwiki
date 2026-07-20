---
title: "PHP Warning: array_flip() invalid values"
description: "Fix PHP Warning: array_flip() invalid values. Learn to ensure array values are strings or ints, check for non-string values, and validate input."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# PHP Warning: array_flip() invalid values

This warning occurs when `array_flip()` receives an array where values cannot be used as keys. Only string and integer values are valid; arrays, objects, and null will fail.

## Common Causes

- Array contains values that are arrays or objects
- Mixing numeric and non-scalar values
- NULL or boolean values in the array

## How to Fix

### Ensure Array Values are Strings/Ints

```php
<?php
// Wrong — contains array value
$flipped = array_flip($input);

// Correct — filter out non-scalar types
$filtered = array_filter($input, function ($v) {
    return is_string($v) || is_int($v);
});
$flipped = array_flip($filtered);
?>
```

### Check for Non-string Values

```php
<?php
// Wrong — array with mixed types
$flipped = array_flip([1, 'two', null]);

// Correct — validate before flipping
$filtered = [];
foreach ($input as $key => $val) {
    if (is_string($val) || is_int($val)) {
        $filtered[$key] = $val;
    }
}
$flipped = array_flip($filtered);
?>
```

### Validate Input

```php
<?php
function safeArrayFlip(array $arr): array
{
    foreach ($arr as $v) {
        if (!is_string($v) && !is_int($v)) {
            throw new UnexpectedValueException(
                'Value of type ' . gettype($v) . ' cannot be used as key'
            );
        }
    }
    return array_flip($arr);
}
?>
```

## Examples

```php
<?php
// This triggers the warning
$fruits = ['a' => 'apple', 'b' => ['x']];
$flipped = array_flip($fruits); // array value cannot be used as key
// Warning: array_flip(): Can only flip string and integer values!

// Correct
$fruits = ['a' => 'apple', 'b' => 'banana'];
$flipped = array_flip($fruits); // ['apple' => 'a', 'banana' => 'b']
?>
```

## Related Errors

- [PHP Warning: array_combine()]({{< relref "/languages/php/warning-in-array-all" >}})
- [PHP Warning: array_keys()]({{< relref "/languages/php/warning-in-array-keys" >}})
- [PHP Warning: array_values()]({{< relref "/languages/php/warning-in-array-values" >}})
