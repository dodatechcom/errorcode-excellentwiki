---
title: "[Solution] PHP mb_substr()/mb_strpos() Illegal Character Offset"
description: "Fix PHP mb_substr()/mb_strpos() illegal character offset by checking offset validity, using mb_strlen() for bounds, and handling multibyte properly. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 12
---

# PHP mb_substr()/mb_strpos() Illegal Character Offset

The `mb_substr()` or `mb_strpos()` function received an illegal character offset. This happens when the offset points to the middle of a multibyte character, is negative beyond the string length, or the encoding parameter doesn't match the actual string encoding.

## Common Causes

```php
// Cause 1: Offset lands in the middle of a multibyte character
$string = "日本語テスト"; // 6 characters, but 18 bytes
echo mb_substr($string, 1, 2, 'UTF-8'); // Works
echo mb_substr($string, 1, 1, 'UTF-8'); // May trigger warning

// Cause 2: Offset is beyond string length
$string = "Hello";
echo mb_substr($string, 10, 5, 'UTF-8');

// Cause 3: Negative offset beyond string length
$string = "Hello";
echo mb_substr($string, -10, 5, 'UTF-8');

// Cause 4: Encoding mismatch
$gbk = mb_convert_encoding("测试", 'GBK', 'UTF-8');
echo mb_strpos($gbk, '测', 0, 'UTF-8'); // Wrong encoding specified

// Cause 5: Non-numeric offset passed
echo mb_substr("Hello", "abc", 5, 'UTF-8');
```

## How to Fix

### Fix 1: Validate Offset Before Calling mb_* Functions

```php
function safeMbSubstr(string $string, int $offset, ?int $length = null, string $encoding = 'UTF-8'): string {
    $len = mb_strlen($string, $encoding);

    if ($offset < 0) {
        $offset = max(0, $len + $offset);
    }

    $offset = min($offset, $len);

    if ($length !== null && $length < 0) {
        $length = max(0, $len + $length - $offset);
    }

    if ($length !== null) {
        $length = min($length, $len - $offset);
    }

    return mb_substr($string, $offset, $length, $encoding);
}
```

### Fix 2: Use mb_strrpos/mb_strpos with Bounds Checking

```php
function safeMbStrpos(string $haystack, string $needle, int $offset = 0, string $encoding = 'UTF-8'): int|false {
    $haystackLen = mb_strlen($haystack, $encoding);

    if ($offset < 0) {
        $offset = max(0, $haystackLen + $offset);
    }

    $offset = min($offset, $haystackLen);

    return mb_strpos($haystack, $needle, $offset, $encoding);
}
```

### Fix 3: Detect Encoding Automatically

```php
function smartMbSubstr(string $string, int $offset, ?int $length = null): string {
    $encoding = mb_detect_encoding($string, ['UTF-8', 'ASCII', 'ISO-8859-1', 'SJIS']);

    if ($encoding === false) {
        $encoding = 'UTF-8';
    }

    $len = mb_strlen($string, $encoding);

    if ($offset < 0) {
        $offset = max(0, $len + $offset);
    }

    $offset = min($offset, $len);

    return mb_substr($string, $offset, $length, $encoding);
}
```

### Fix 4: Clamp Offset and Length Values

```php
function mbSubstrSafe(string $text, int $start, int $length = null, string $enc = 'UTF-8'): string {
    $textLen = mb_strlen($text, $enc);

    if ($textLen === 0) {
        return '';
    }

    $start = max(0, min($start, $textLen));

    if ($length === null) {
        return mb_substr($text, $start, null, $enc);
    }

    if ($length < 0) {
        $length = max(0, $textLen + $length - $start);
    }

    $length = max(0, min($length, $textLen - $start));

    return mb_substr($text, $start, $length, $enc);
}
```

## Examples

```php
// Example: Safe multibyte string truncation
function truncateUtf8(string $string, int $maxChars, string $suffix = '...'): string {
    $encoding = 'UTF-8';
    $len = mb_strlen($string, $encoding);

    if ($len <= $maxChars) {
        return $string;
    }

    $truncated = mb_substr($string, 0, $maxChars, $encoding);

    // Ensure we don't end on a partial character
    while ($maxChars > 0 && mb_check_encoding($truncated, $encoding) === false) {
        $maxChars--;
        $truncated = mb_substr($string, 0, $maxChars, $encoding);
    }

    return $truncated . $suffix;
}
```

## Related Errors

- [mb_convert_encoding() unable to convert](/languages/php/mbstring-encoding-error/)
- [mbstring func_overload deprecation](/languages/php/mbstring-overloaded-warning/)
- [mb_ereg*() deprecated](/languages/php/mbstring-ereg-deprecated/)
