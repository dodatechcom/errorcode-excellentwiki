---
title: "PHP Warning: count(): Parameter must be an array or an object that implements Countable"
description: "Fix PHP Warning: count() expects an array or Countable. Learn to validate variables before counting."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["warning", "count", "array", "countable"]
weight: 5
---

# PHP Warning: count(): Parameter must be an array or an object that implements Countable

This warning occurs when `count()` receives a parameter that is not an array and does not implement the `Countable` interface. In PHP 7.2+, passing `null` or non-countable types to `count()` triggers this warning.

## Common Causes

- Passing `null` or a non-array variable to `count()`
- Using `count()` on a variable that may not be initialized as an array
- Calling `count()` on a result that returns a non-countable type

## How to Fix

### Check the Type Before Counting

```php
<?php
// Wrong — $data might not be an array
$count = count($data);

// Correct — validate first
if (is_array($data)) {
    $count = count($data);
} else {
    $count = 0;
}
?>
```

### Use the Null Coalescing Operator

```php
<?php
$count = count($data ?? []);
?>
```

### Use is_array() with count()

```php
<?php
function getItemCount($items): int {
    return is_array($items) ? count($items) : 0;
}
?>
```

## Examples

```php
<?php
// This triggers the warning
$data = null;
echo count($data);
// Warning: count(): Parameter must be an array or an object that implements Countable

// Correct
$data = [1, 2, 3];
echo count($data); // 3
?>
```

## Related Errors

- [PHP Warning: strlen()]({{< relref "/languages/php/warning-in-strlen" >}})
- [PHP Warning: foreach()]({{< relref "/languages/php/warning-in-foreach" >}})
- [PHP Fatal Error]({{< relref "/languages/php/fatal-error" >}})
