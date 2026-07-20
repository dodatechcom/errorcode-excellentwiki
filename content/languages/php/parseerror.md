---
title: "[Solution] PHP ParseError — Syntax Error in Code"
description: "Fix PHP ParseError by checking syntax, using php -l linting, and verifying bracket matching."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 57
---

# ParseError — Syntax Error in Code

ParseError (previously `Parse error` in PHP < 7) is thrown when PHP encounters a syntax error while parsing code. This commonly occurs with missing semicolons, unmatched brackets, incorrect function calls, or invalid string interpolation. PHP 7.0+ throws this as an `Error` subclass.

## Common Causes

```php
<?php
// Cause 1: Missing semicolon
$value = 10
echo $value; // ParseError

// Cause 2: Unmatched brackets
function test() {
    if (true) {
        echo "hello";
    // Missing closing brace
} // ParseError

// Cause 3: Invalid function call syntax
echo strlen("hello" // Missing closing parenthesis); // ParseError

// Cause 4: Invalid string interpolation
$name = "World";
echo "Hello {$name"; // ParseError: unclosed variable

// Cause 5: Invalid use of reserved keywords
$class = new class {}; // ParseError in PHP < 7.0
?>
```

## How to Fix

### Fix 1: Use php -l to lint files

```bash
# Check a single file
php -l script.php

# Check all PHP files in a directory
find . -name "*.php" -exec php -l {} \;

# Check for common issues
php -l -d short_open_tag=1 script.php
```

### Fix 2: Verify bracket and parenthesis matching

```php
<?php
// Use an IDE or editor with bracket matching
// Common bracket patterns to verify:

// Correctly matched brackets
if ($condition) {
    echo "yes";
} else {
    echo "no";
}

// Correctly matched parentheses
$result = array_map(function ($item) {
    return $item * 2;
}, $array);

// Correctly matched quotes
$text = "Hello \"World\"";
$template = "Name: {$name}";
?>
```

### Fix 3: Use a pre-commit hook for syntax checking

```bash
#!/bin/bash
# .git/hooks/pre-commit

for file in $(git diff --cached --name-only --diff-filter=ACM | grep '\.php$'); do
    php -l "$file" 2>/dev/null
    if [ $? -ne 0 ]; then
        echo "Syntax error in $file — commit aborted"
        exit 1
    fi
done
```

## Examples

```php
<?php
// Common ParseError fixes

// WRONG — missing comma in array
$config = [
    'host' => 'localhost'
    'port' => 3306
];

// CORRECT
$config = [
    'host' => 'localhost',
    'port' => 3306,
];

// WRONG — missing closing tag
<?php echo "hello";

// CORRECT
<?php echo "hello"; ?>
?>
```

## Related Errors

- [PHP CompileError]({{< relref "/languages/php/compileerror" >}}) — compile-time error
- [PHP E_COMPILE_ERROR]({{< relref "/languages/php/e-compile-error" >}}) — compilation error
- [PHP Fatal Error]({{< relref "/languages/php/fatal-error" >}}) — fatal error
