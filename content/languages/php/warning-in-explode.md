---
title: "PHP Warning: explode() empty delimiter"
description: "Fix PHP Warning: explode() empty delimiter. Learn to check delimiter values, validate input, and handle empty strings properly."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# PHP Warning: explode() empty delimiter

This warning occurs when `explode()` is called with an empty string as the delimiter. PHP requires a non-empty string to split on.

## Common Causes

- Using a variable that resolves to an empty string as the delimiter
- Not validating user-provided delimiter values
- Confusing `explode()` with `str_split()`

## How to Fix

### Check Delimiter Value

```php
<?php
// Wrong — empty delimiter
$parts = explode('', $string);

// Correct — use a non-empty delimiter
$parts = explode(',', $string);
?>
```

### Validate Input Before Exploding

```php
<?php
// Wrong — delimiter may be empty
$parts = explode($delimiter, $string);

// Correct — validate first
if (strlen($delimiter) > 0) {
    $parts = explode($delimiter, $string);
} else {
    $parts = str_split($string);
}
?>
```

### Handle Empty Strings Properly

```php
<?php
// Wrong — empty string as delimiter
$parts = explode('', $input);

// Correct — use str_split for character splitting
$chars = str_split($input);
?>
```

## Examples

```php
<?php
// This triggers the warning
$delimiter = '';
$parts = explode($delimiter, 'a,b,c');
// Warning: explode(): Empty delimiter

// Correct
$parts = explode(',', 'a,b,c'); // ['a', 'b', 'c']
$chars = str_split('abc');      // ['a', 'b', 'c']
?>
```

## Related Errors

- [PHP Warning: implode()]({{< relref "/languages/php/warning-in-implode" >}})
- [PHP Warning: preg_split()]({{< relref "/languages/php/warning-in-preg-split" >}})
- [PHP Warning: str_replace()]({{< relref "/languages/php/warning-in-str-replace" >}})
