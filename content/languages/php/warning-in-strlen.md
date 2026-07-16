---
title: "PHP Warning: strlen() expects exactly 1 argument"
description: "Fix PHP Warning: strlen() expects exactly 1 parameter. Learn to pass a single string to strlen()."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["warning", "strlen", "string", "arguments"]
weight: 5
---

# PHP Warning: strlen() expects exactly 1 argument

This warning occurs when you pass more or fewer than one argument to `strlen()`. The function expects exactly one string parameter and returns its byte length.

## Common Causes

- Accidentally passing extra arguments to `strlen()`
- Passing no arguments or multiple strings thinking it concatenates them
- Copy-pasting from multi-argument functions

## How to Fix

### Pass Exactly One String

```php
<?php
// Wrong — two arguments
echo strlen("hello", "world");

// Correct
echo strlen("hello"); // 5
?>
```

### Concatenate Before Calling strlen()

```php
<?php
// Wrong
echo strlen("hello", "world");

// Correct — concatenate first
echo strlen("hello" . "world"); // 10
?>
```

### Use strlen() for UTF-8 with mb_strlen()

```php
<?php
// For multibyte strings
echo mb_strlen("café", "UTF-8"); // 4
?>
```

## Examples

```php
<?php
// This triggers the warning
echo strlen("hello", "extra");
// Warning: strlen() expects exactly 1 parameter, 2 given

// Correct usage
$name = "Alice";
echo strlen($name); // 5
?>
```

## Related Errors

- [PHP Warning: strpos()]({{< relref "/languages/php/warning-in-strpos" >}})
- [PHP Warning: sprintf()]({{< relref "/languages/php/warning-in-sprintf" >}})
- [PHP Warning: count()]({{< relref "/languages/php/warning-count" >}})
