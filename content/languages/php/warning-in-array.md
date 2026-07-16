---
title: "PHP Warning: array() expects at least 1 argument"
description: "Fix PHP Warning: array() expects at least 1 argument. Learn to properly initialize arrays in PHP."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["warning", "array", "initialization", "arguments"]
weight: 5
---

# PHP Warning: array() expects at least 1 argument

This warning occurs when you call `array()` or the short array syntax `[]` without providing at least one element. While empty arrays are valid in PHP, certain operations or contexts expect initial values.

## Common Causes

- Passing an uninitialized variable to functions expecting an array with elements
- Incorrect use of `array()` in a context requiring at least one element
- Dynamically building arrays where the element source is empty

## How to Fix

### Initialize Arrays with At Least One Element

```php
<?php
// Wrong — no initial elements in context requiring them
$arr = array();

// Correct — provide at least one element
$arr = array('first');
?>
```

### Guard Against Empty Input

```php
<?php
function processItems(array $items): string {
    if (empty($items)) {
        return 'No items to process';
    }
    return implode(', ', $items);
}

echo processItems(['a', 'b']);
?>
```

### Use Short Array Syntax

```php
<?php
// Correct — short array syntax with elements
$colors = ['red', 'green', 'blue'];
?>
```

## Examples

```php
<?php
// This can trigger the warning
$arr = array();
echo count($arr); // 0 — empty but valid

// In some function contexts:
$result = array_map('strtoupper', $arr); // works but may warn if context expects elements
?>
```

## Related Errors

- [PHP Warning: count()]({{< relref "/languages/php/warning-count" >}})
- [PHP Warning: array_push()]({{< relref "/languages/php/warning-in-array-push" >}})
- [PHP Warning: array_merge()]({{< relref "/languages/php/warning-in-array-merge" >}})
