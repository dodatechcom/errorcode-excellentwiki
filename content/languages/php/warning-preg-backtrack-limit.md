---
title: "PHP Warning: PCRE backtrack limit exhausted"
description: "Fix PHP Warning: preg_replace or preg_match: PCRE backtrack limit exhausted. Learn to increase pcre.backtrack_limit, optimize regex, and avoid catastrophic backtracking."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# PHP Warning: PCRE backtrack limit exhausted

This warning occurs when a regular expression causes the PCRE backtracking limit to be exceeded. It usually indicates a pattern with catastrophic backtracking.

## Common Causes

- Nested quantifiers causing exponential backtracking
- Complex regex on large strings
- Default backtrack limit too low for the pattern

## How to Fix

### Increase pcre.backtrack_limit

```php
<?php
// Wrong — default limit may be insufficient
preg_match($pattern, $longString);

// Correct — increase the backtrack limit
ini_set('pcre.backtrack_limit', 1000000);
preg_match($pattern, $longString);
?>
```

### Optimize Regex Using Atomic Groups

```php
<?php
// Wrong — catastrophic backtracking
preg_match('/(a+)+b/', $string);

// Correct — use atomic groups
preg_match('/(?>a+)+b/', $string);
?>
```

### Avoid Nested Quantifiers

```php
<?php
// Wrong — nested quantifiers
preg_match('/(x+y+)+z/', $string);

// Correct — simplify pattern
preg_match('/x+y+z/', $string);
?>
```

## Examples

```php
<?php
// This triggers the warning
$long = str_repeat('a', 10000);
$result = preg_match('/(a+)+b/', $long);
// Warning: preg_match(): Compilation failed: pcre.backtrack_limit exhausted

// Correct — optimized pattern
$result = preg_match('/a++b/', $long);
?>
```

## Related Errors

- [PHP Warning: preg_match()]({{< relref "/languages/php/warning-in-preg-match" >}})
- [PHP Warning: preg_replace()]({{< relref "/languages/php/warning-in-preg-replace" >}})
- [PHP Warning: preg_split()]({{< relref "/languages/php/warning-in-preg-split" >}})
