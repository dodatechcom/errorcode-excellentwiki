---
title: "[Solution] PHP E_PARSE — Parse Error Syntax Fix"
description: "Fix PHP E_PARSE syntax errors that prevent script execution. Learn to identify and fix common parse errors using php -l and code editor tools."
languages: ["php"]
severities: ["error"]
error-types: ["syntax"]
tags: ["e-parse", "parse", "syntax"]
weight: 5
---

# [Solution] PHP E_PARSE — Parse Error Syntax Fix

`E_PARSE` is a compile-time parse error in PHP. The PHP parser encounters code that violates the language grammar and cannot execute any code in the file. The error message includes the filename, line number, and the problematic token.

## Common Causes

- Missing semicolons at the end of statements
- Unclosed strings, brackets, or PHP tags
- Wrong array syntax or operator usage
- Mismatched parentheses or braces

## How to Fix

### 1. Add Missing Semicolons

```php
// WRONG
<?php
$greeting = "Hello"
echo $greeting
?>

// CORRECT
<?php
$greeting = "Hello";
echo $greeting;
?>
```

### 2. Close All Brackets

```php
// WRONG — unclosed parenthesis
<?php
function greet($name) {
    echo "Hello " . $name;
}

// CORRECT
<?php
function greet($name) {
    echo "Hello " . $name;
}
?>
```

### 3. Use `php -l` to Find Parse Errors

```bash
php -l index.php
```

Example output:

```
Parse error: syntax error, unexpected token "," in index.php on line 5
Errors parsing index.php
```

## Examples

```php
<?php
// E_PARSE: unexpected ';' on line 2
$arr = [1, 2, 3];

// E_PARSE: unexpected EOF, expecting '}'
function test() {
    echo "hello";
// missing closing brace

// E_PARSE: unescaped quote
echo 'It's broken';
?>
```

## Related Errors

- [PHP E_COMPILE_ERROR]({{< relref "/languages/php/e-compile-error" >}})
- [PHP E_ERROR]({{< relref "/languages/php/e-error" >}})
- [PHP Warning: Wrong Parameter Count]({{< relref "/languages/php/warning-count" >}})
- [PHP Parse Error]({{< relref "/languages/php/parse-error" >}})
