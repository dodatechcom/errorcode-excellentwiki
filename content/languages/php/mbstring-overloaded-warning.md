---
title: "[Solution] PHP mbstring.func_overload Deprecated — mb_* Function Overloading"
description: "Fix PHP mbstring.func_overload deprecation by disabling func_overload, using mb_* functions directly, and updating legacy code. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 12
---

# PHP mbstring.func_overload Deprecated — mb_* Function Overloading

The `mbstring.func_overload` INI setting has been deprecated since PHP 7.2 and removed in PHP 8.0. This setting replaced PHP's built-in string functions with their `mb_*` equivalents, which caused unpredictable behavior and was removed to improve code clarity.

## Common Causes

```php
// Cause 1: Using func_overload in php.ini
// mbstring.func_overload = 7  (deprecated/removed)

// Cause 2: Legacy code relying on overloaded strlen()
(strlen("Café résumé")); // Expected mb_strlen behavior but got byte count

// Cause 3: substr() behaving differently after func_overload removal
$utf8 = "日本語テスト";
echo substr($utf8, 0, 3); // Corrupts multibyte string

// Cause 4: strpos() returning wrong offset for multibyte strings
$utf8 = "café résumé";
echo strpos($utf8, "é"); // May return wrong position

// Cause 5: Code that mixed byte and character counting
$text = "Hello 世界";
echo strlen($text); // 12 bytes, not 10 characters
```

## How to Fix

### Fix 1: Disable func_overload in php.ini

```ini
; php.ini - Remove or set to 0
mbstring.func_overload = 0
```

```bash
# Check current func_overload setting
php -r 'echo ini_get("mbstring.func_overload");'

# Disable via command line
php -d mbstring.func_overload=0 script.php
```

### Fix 2: Replace String Functions with mb_* Equivalents

```php
// Before (relied on func_overload)
strlen($string);
strpos($string, $search);
substr($string, $offset, $length);
strtolower($string);
strtoupper($string);
strrpos($string, $search);
strstr($string, $search);

// After (explicit mb_* functions)
mb_strlen($string, 'UTF-8');
mb_strpos($string, $search, 0, 'UTF-8');
mb_substr($string, $offset, $length, 'UTF-8');
mb_strtolower($string, 'UTF-8');
mb_strtoupper($string, 'UTF-8');
mb_strrpos($string, $search, 0, 'UTF-8');
mb_strstr($string, $search, false, 'UTF-8');
```

### Fix 3: Create Compatibility Wrapper Functions

```php
function safeStrlen(string $string, string $encoding = 'UTF-8'): int {
    if (extension_loaded('mbstring')) {
        return mb_strlen($string, $encoding);
    }
    return strlen($string);
}

function safeStrpos(string $haystack, string $needle, int $offset = 0, string $encoding = 'UTF-8'): int|false {
    if (extension_loaded('mbstring')) {
        return mb_strpos($haystack, $needle, $offset, $encoding);
    }
    return strpos($haystack, $needle, $offset);
}

function safeSubstr(string $string, int $offset, ?int $length = null, string $encoding = 'UTF-8'): string {
    if (extension_loaded('mbstring')) {
        return mb_substr($string, $offset, $length, $encoding);
    }
    if ($length !== null) {
        return substr($string, $offset, $length);
    }
    return substr($string, $offset);
}
```

### Fix 4: Use preg_* Functions as Alternative

```php
// Replace overloaded strlen with preg to count characters
function countChars(string $string): int {
    return preg_match_all('/./us', $string);
}

// Replace overloaded substr
function utf8Substr(string $string, int $start, int $length = null): string {
    if ($length === null) {
        $pattern = '/\G.{' . $start . '}/us';
        if (preg_match($pattern, $string, $matches)) {
            return $matches[0];
        }
        return '';
    }

    $pattern = '/\G.{' . $start . '}.{' . $length . '}/us';
    if (preg_match($pattern, $string, $matches)) {
        return $matches[0];
    }
    return '';
}
```

## Examples

```php
// Example: Migrate code from func_overload to explicit mb_* functions
function processUserText(string $text): array {
    $encoding = 'UTF-8';

    return [
        'length' => mb_strlen($text, $encoding),
        'lowercase' => mb_strtolower($text, $encoding),
        'uppercase' => mb_strtoupper($text, $encoding),
        'first_word' => mb_substr($text, 0, mb_strpos($text, ' ', 0, $encoding), $encoding),
        'char_count' => preg_match_all('/./us', $text),
    ];
}
```

## Related Errors

- [mb_substr() illegal character offset](/languages/php/mbstring-illegal-offset/)
- [mb_convert_encoding() unable to convert](/languages/php/mbstring-encoding-error/)
- [mb_ereg*() deprecated](/languages/php/mbstring-ereg-deprecated/)
