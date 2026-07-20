---
title: "[Solution] PHP mb_ereg*() Deprecated — Migrated in PHP 8.0"
description: "Fix PHP mb_ereg*() deprecated by migrating to preg_match(), using PCRE patterns, and updating regex code. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 12
---

# PHP mb_ereg*() Deprecated — Migrated in PHP 8.0

The `mb_ereg()`, `mb_eregi()`, `mb_ereg_replace()`, and related POSIX regex functions were deprecated in PHP 7.2 and removed in PHP 8.0. Replace them with PCRE functions (`preg_match()`, `preg_replace()`) which support Unicode patterns natively.

## Common Causes

```php
// Cause 1: Using mb_ereg() directly
mb_ereg('pattern', $string, $matches); // Deprecated/removed

// Cause 2: Using mb_eregi() for case-insensitive matching
mb_eregi('pattern', $string, $matches); // Deprecated/removed

// Cause 3: Using mb_ereg_replace() for substitution
$result = mb_ereg_replace('pattern', 'replacement', $string); // Deprecated/removed

// Cause 4: Using mb_split() for string splitting
$parts = mb_split(',', $string); // Deprecated/removed

// Cause 5: Legacy code using POSIX regex with multibyte strings
mb_ereg('^[a-zA-Z]+$', $japaneseString);
```

## How to Fix

### Fix 1: Replace mb_ereg() with preg_match()

```php
// Before
mb_ereg('(\w+)@(\w+)\.(\w+)', $email, $matches);

// After — Use preg_match() with u modifier for UTF-8
preg_match('/(\w+)@(\w+)\.(\w+)/u', $email, $matches);
```

```php
// Before
mb_eregi('^(café|koffie)$', $drink);

// After — Use preg_match() with /i for case-insensitive
preg_match('/^(café|koffie)$/ui', $drink);
```

### Fix 2: Replace mb_ereg_replace() with preg_replace()

```php
// Before
$result = mb_ereg_replace('\s+', ' ', $text);

// After
$result = preg_replace('/\s+/u', ' ', $text);
```

```php
// Before
$result = mb_ereg_replace('<[^>]+>', '', $html);

// After
$result = preg_replace('/<[^>]+>/u', '', $html);
```

### Fix 3: Replace mb_split() with preg_split()

```php
// Before
$parts = mb_split('\s+', $text);

// After
$parts = preg_split('/\s+/u', $text);
```

```php
// Before
$lines = mb_split("\r?\n", $content);

// After
$lines = preg_split("/\r?\n/u", $content);
```

### Fix 4: Create Compatibility Wrapper Functions

```php
function mbRegexMatch(string $pattern, string $string, ?array &$matches = null, string $encoding = 'UTF-8'): bool {
    $flags = PREG_SET_ORDER;

    if ($matches !== null) {
        $result = preg_match('/' . $pattern . '/u', $string, $matches, $flags);
    } else {
        $result = preg_match('/' . $pattern . '/u', $string);
    }

    return $result !== false && $result > 0;
}

function mbRegexReplace(string $pattern, string $replacement, string $string): string {
    $result = preg_replace('/' . $pattern . '/u', $replacement, $string);

    return $result !== null ? $result : $string;
}

function mbRegexSplit(string $pattern, string $string): array {
    $result = preg_split('/' . $pattern . '/u', $string);

    return $result !== false ? $result : [$string];
}
```

## Examples

```php
// Example: Validate UTF-8 username using preg_match()
function isValidUsername(string $username): bool {
    return preg_match('/^[a-zA-Z0-9_\x{4e00}-\x{9fff}]+$/u', $username) === 1;
}

// Example: Extract multibyte words from text
function extractWords(string $text): array {
    preg_match_all('/\p{L}+/u', $text, $matches);
    return $matches[0];
}

// Example: Replace multibyte whitespace
function normalizeWhitespace(string $text): string {
    return preg_replace('/\s+/u', ' ', trim($text));
}
```

## Related Errors

- [mb_substr() illegal character offset](/languages/php/mbstring-illegal-offset/)
- [mb_convert_encoding() unable to convert](/languages/php/mbstring-encoding-error/)
- [preg_*() PCRE errors](/languages/php/preg-error/)
