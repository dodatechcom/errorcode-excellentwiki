---
title: "PHP Parse error: syntax error, unexpected token"
description: "Fix PHP Parse error: syntax error, unexpected token. Learn to identify and fix common PHP syntax mistakes."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["parse-error", "syntax", "unexpected-token"]
weight: 5
---

# PHP Parse error: syntax error, unexpected token

A parse error occurs when the PHP parser encounters code that violates the language grammar. PHP cannot execute any code in a file that has a parse error — it stops immediately and reports the file, line number, and problematic token.

## Common Causes

- Missing semicolons at the end of statements
- Unclosed strings, brackets, or parentheses
- Using old-style array syntax incorrectly
- Mismatched quotes or unescaped characters inside strings

## How to Fix

### Add Missing Semicolons

```php
<?php
// Wrong
$greeting = "Hello"
echo $greeting

// Correct
$greeting = "Hello";
echo $greeting;
?>
```

### Close All Brackets and Parentheses

```php
<?php
// Wrong — missing closing parenthesis
function greet($name) {
    echo "Hello " . $name;
}

// Correct
function greet($name) {
    echo "Hello " . $name;
}
?>
```

### Escape Quotes Inside Strings

```php
<?php
// Wrong
echo 'It's broken';

// Correct
echo 'It\'s fixed';
echo "It's fixed";
?>
```

## Examples

```php
<?php
// This triggers a parse error
$arr = array(1, 2, 3)
echo $arr[0]
// Parse error: syntax error, unexpected token ","
?>
```

Use `php -l` to lint-check files without executing them:

```bash
php -l index.php
```

## Related Errors

- [PHP Fatal Error]({{< relref "/languages/php/fatal-error" >}})
- [PHP Warning: count()]({{< relref "/languages/php/warning-count" >}})
- [PHP Notice: Undefined Index]({{< relref "/languages/php/notice-undefined-index" >}})
