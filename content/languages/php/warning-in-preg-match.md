---
title: "PHP Warning: preg_match() compilation failure"
description: "Fix PHP Warning: preg_match() compilation failure. Learn to check regex syntax, escape delimiters, and validate modifiers."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# PHP Warning: preg_match() compilation failure

This warning occurs when `preg_match()` receives an invalid regular expression pattern that the PCRE engine cannot compile.

## Common Causes

- Missing or incorrect regex delimiters
- Invalid regex syntax or unescaped special characters
- Using unsupported or invalid modifiers

## How to Fix

### Check Regex Syntax

```php
<?php
// Wrong — missing delimiter
preg_match('[0-9]+', $string);

// Correct — proper delimiters
preg_match('/[0-9]+/', $string);
?>
```

### Escape Delimiters

```php
<?php
// Wrong — unescaped delimiter inside pattern
preg_match('/http://example.com/', $url);

// Correct — escape the delimiter
preg_match('/http:\/\/example\.com/', $url);
// Or use a different delimiter
preg_match('#http://example\.com#', $url);
?>
```

### Validate Modifiers

```php
<?php
// Wrong — invalid modifier
preg_match('/pattern/x/', $string);

// Correct — use valid modifiers only
preg_match('/pattern/i', $string);   // case-insensitive
preg_match('/pattern/m', $string);   // multiline
preg_match('/pattern/s', $string);   // dot matches newline
?>
```

## Examples

```php
<?php
// This triggers the warning
$pattern = '/[a-z/'; // missing closing bracket
preg_match($pattern, 'hello');
// Warning: preg_match(): Compilation failed: missing closing bracket

// Correct
preg_match('/[a-z]/', 'hello'); // 1
?>
```

## Related Errors

- [PHP Warning: preg_replace()]({{< relref "/languages/php/warning-in-preg-replace" >}})
- [PHP Warning: preg_split()]({{< relref "/languages/php/warning-in-preg-split" >}})
- [PHP Warning: PCRE backtrack limit]({{< relref "/languages/php/warning-preg-backtrack-limit" >}})
