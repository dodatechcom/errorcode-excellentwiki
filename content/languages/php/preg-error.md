---
title: "PHP PREG compilation failed: PCRE error"
description: "Fix PHP PREG compilation failed PCRE error. Learn to resolve regex syntax errors and backtracking limit issues."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["preg", "regex", "pcre", "pattern", "compilation-failed"]
weight: 5
---

# PHP PREG compilation failed: PCRE error

This error occurs when PHP's PCRE regex engine fails to compile a regular expression. The pattern contains invalid syntax, is too complex, or exceeds internal limits.

## Common Causes

- Invalid regex syntax (unmatched brackets, unclosed delimiters)
- Pattern exceeds PCRE backtracking or recursion limit
- Unescaped special characters in the pattern
- PHP version change introduced stricter PCRE validation

## How to Fix

### Validate Regex Pattern

```php
<?php
$pattern = '/user[s]?\s+[a-z]+/';
if (preg_match($pattern, $input)) {
    echo 'Match found';
}
// Check for errors with preg_last_error()
if (preg_last_error() !== PREG_NO_ERROR) {
    echo 'Regex error: ' . preg_last_error();
}
?>
```

### Increase Backtracking Limit

```php
<?php
// Increase backtracking limit
ini_set('pcre.backtrack_limit', 1000000);
ini_set('pcre.recursion_limit', 1000000);
?>
```

### Escape Special Characters

```php
<?php
// Bad: unescaped dot and question mark
$pattern = '/file.txt?/';

// Good: properly escaped
$pattern = '/file\.txt\?/';

// Or use preg_quote()
$filename = 'file.txt?';
$pattern = '/' . preg_quote($filename, '/') . '/';
?>
```

### Use preg_last_error for Debugging

```php
<?php
$errors = [
    PREG_NO_ERROR => 'No error',
    PREG_INTERNAL_ERROR => 'Internal PCRE error',
    PREG_BACKTRACK_LIMIT_ERROR => 'Backtracking limit exhausted',
    PREG_RECURSION_LIMIT_ERROR => 'Recursion limit exhausted',
    PREG_BAD_UTF8_ERROR => 'Malformed UTF-8 data',
    PREG_BAD_UTF8_OFFSET_ERROR => 'Bad UTF-8 offset',
];
$result = preg_match($pattern, $input);
if ($result === false) {
    echo $errors[preg_last_error()] ?? 'Unknown error';
}
?>
```

## Examples

```php
<?php
// Example 1: Unclosed parenthesis
preg_match('/(foo bar/', $input);
// Warning: PREG compilation failed: unmatched parentheses
// Fix: close all parentheses: '/(foo bar)/'

// Example 2: Backtracking limit
preg_match('/^(a+)+$/', str_repeat('a', 100) . 'b');
// Warning: PREG compilation failed: backtracking limit exhausted
// Fix: ini_set('pcre.backtrack_limit', 1000000);

// Example 3: Invalid character class
preg_match('/[a-z/', $input);
// Warning: PREG compilation failed: unterminated character class
// Fix: '/[a-z]/'
?>
```

## Related Errors

- [PHP Fatal Error: Allowed memory size exhausted]({{< relref "/languages/php/fatal-error" >}})
- [PHP Warning: count()]({{< relref "/languages/php/warning-count" >}})
- [PHP Notice: Undefined Variable]({{< relref "/languages/php/notice-undefined-variable" >}})
