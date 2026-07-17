---
title: "PHP Warning: strpos(): Empty needle"
description: "Fix PHP Warning: strpos() empty needle. Learn to validate strings before searching with strpos()."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# PHP Warning: strpos(): Empty needle

This warning occurs when you pass an empty string as the needle (search term) to `strpos()`. The function requires a non-empty string to search for within the haystack.

## Common Causes

- Passing an uninitialized or empty variable as the needle
- Not trimming or validating input before searching
- Using string interpolation that results in an empty value

## How to Fix

### Validate the Needle Before Searching

```php
<?php
// Wrong — needle may be empty
$needle = '';
$pos = strpos($haystack, $needle);

// Correct — check first
if (!empty($needle)) {
    $pos = strpos($haystack, $needle);
} else {
    $pos = false;
}
?>
```

### Use the Null Coalescing Operator

```php
<?php
$pos = strpos($haystack, $needle ?? '');
?>
```

### Check strlen() Before strpos()

```php
<?php
function safeStrpos(string $haystack, ?string $needle): int|false {
    if ($needle === null || strlen($needle) === 0) {
        return false;
    }
    return strpos($haystack, $needle);
}
?>
```

## Examples

```php
<?php
// This triggers the warning
$needle = '';
echo strpos("hello world", $needle);
// Warning: strpos(): Empty needle

// Correct
echo strpos("hello world", "world"); // 6
?>
```

## Related Errors

- [PHP Warning: strlen()]({{< relref "/languages/php/warning-in-strlen" >}})
- [PHP Warning: array_search()]({{< relref "/languages/php/warning-in-array-search" >}})
- [PHP Notice: Undefined Index]({{< relref "/languages/php/notice-undefined-index" >}})
