---
title: "PHP Warning: str_replace() expects at least 3 parameters"
description: "Fix PHP Warning: str_replace() expects at least 3 parameters. Learn to provide all required arguments and handle null values."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# PHP Warning: str_replace() expects at least 3 parameters

This warning occurs when `str_replace()` is called with fewer than three arguments. The function requires a search value, a replacement value, and the subject string or array.

## Common Causes

- Omitting the subject parameter
- Passing null or undefined variables as arguments
- Confusing parameter order with other string functions

## How to Fix

### Provide All Three Parameters

```php
<?php
// Wrong — missing subject
$result = str_replace('old', 'new');

// Correct
$result = str_replace('old', 'new', $subject);
?>
```

### Check for Null Values

```php
<?php
// Wrong — null subject
$result = str_replace('old', 'new', $subject); // $subject is null

// Correct — ensure subject is a string
$result = str_replace('old', 'new', $subject ?? '');
?>
```

### Use Proper Parameter Order

```php
<?php
// Wrong — swapped search and replace
$result = str_replace($subject, 'new', 'old');

// Correct — search, replace, subject
$result = str_replace('old', 'new', $subject);
?>
```

## Examples

```php
<?php
// This triggers the warning
$result = str_replace('old');
// Warning: str_replace() expects at least 3 parameters, 1 given

// Correct usage
$text = 'Hello old world';
$result = str_replace('old', 'new', $text); // 'Hello new world'
?>
```

## Related Errors

- [PHP Warning: substr()]({{< relref "/languages/php/warning-in-substr" >}})
- [PHP Warning: strpos()]({{< relref "/languages/php/warning-in-strpos" >}})
- [PHP Warning: trim()]({{< relref "/languages/php/warning-in-trim" >}})
