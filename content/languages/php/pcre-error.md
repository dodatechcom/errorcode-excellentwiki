---
title: "[Solution] PHP PCRE Error — JIT Compilation Limit"
description: "Fix PHP PCRE regex errors. Resolve 'PCRE error: JIT compilation limit' and regex performance issues in PHP."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "php"
tags: ["php", "regex", "pcre"]
severity: "error"
---

# PHP PCRE Regex Error

## Error Message

```
preg_match(): Compilation failed: PCRE error: JIT compilation limit reached
```

## Common Causes

- The regex pattern is too complex and exceeds the JIT compiler's stack or code size limit
- Catastrophic backtracking from patterns like (a+)+ against long input strings
- The PCRE JIT extension is enabled but the system has insufficient memory for it

## Solutions

### Solution 1: Increase the PCRE JIT Limit

Raise the JIT stack limit in php.ini or disable JIT if not needed.

```php
<?php
// Check current PCRE configuration
echo ini_get('pcre.jit');          // 1 = enabled
echo ini_get('pcre.jit_limit');    // JIT stack limit (default: 10000000)

// Temporarily increase the limit for this script
ini_set('pcre.jit_limit', '50000000');

// Now the complex regex can compile
$complexPattern = '/^(?:[a-z0-9]+(?:-[a-z0-9]+)*\.)+[a-z]{2,}$/i';
$email = 'user@example.com';
if (preg_match($complexPattern, $email)) {
    echo "Valid domain";
}
?>
```

### Solution 2: Optimize Regex Patterns to Avoid Catastrophic Backtracking

Rewrite patterns to use atomic groups, possessive quantifiers, or simpler alternatives.

```php
<?php
// Bad — catastrophic backtracking potential
$badPattern = '/^(a+)+$/';
// This will hang on long input like "aaaaaaaaaaaaaaaaaaaaaaaaaaaaab"

// Good — use possessive quantifiers
$goodPattern = '/^(a+)++$/';

// Good — use atomic groups (?>...)
$atomicPattern = '/^(?>a+)$/';

// Good — simplify the pattern entirely
$simplePattern = '/^a+$/';

// Test with a long input
$input = str_repeat('a', 10000) . 'b';

// This completes quickly instead of hanging
$start = microtime(true);
$result = preg_match($simplePattern, $input);
$elapsed = microtime(true) - $start;
echo "Pattern matched: " . ($result ? 'yes' : 'no');
echo " Time: " . round($elapsed * 1000, 2) . "ms\n";
?>
```

## Prevention Tips

- Use `preg_last_error()` to detect regex failures programmatically
- Test regex patterns with PCRE_DFA_MATCH for complex patterns — it uses a different algorithm
- Consider using `str_contains()` for simple substring checks instead of regex

## Related Errors

- [Mbstring Error]({{< relref "/languages/php/mbstring-error" >}})
- [Json Decode Error]({{< relref "/languages/php/json-decode-error" >}})
