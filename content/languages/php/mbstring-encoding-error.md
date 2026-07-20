---
title: "[Solution] PHP mb_convert_encoding() Unable to Convert Character"
description: "Fix PHP mb_convert_encoding() unable to convert character by checking source/target encoding, handling illegal sequences, and using mb_substitute_character(). Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 12
---

# PHP mb_convert_encoding() Unable to Convert Character

The `mb_convert_encoding()` function encountered an illegal or unconvertible character during encoding conversion. This happens when the source string contains byte sequences that are invalid in the source encoding, or when the target encoding cannot represent certain characters.

## Common Causes

```php
// Cause 1: Invalid byte sequences in source string
$binary = "\x80\x81\x82";
$result = mb_convert_encoding($binary, 'UTF-8', 'ASCII');

// Cause 2: Mismatched source encoding declaration
$utf8String = "Café résumé";
$result = mb_convert_encoding($utf8String, 'ASCII', 'ISO-8859-1'); // Wrong source

// Cause 3: Target encoding cannot represent the character
$japanese = "日本語テスト";
$result = mb_convert_encoding($japanese, 'ASCII', 'UTF-8');

// Cause 4: Double encoding
$double = mb_convert_encoding("café", 'UTF-8', 'UTF-8');

// Cause 5: Strict mode with illegal sequences
$result = mb_convert_encoding($binary, 'UTF-8', 'ASCII', 'strict');
```

## How to Fix

### Fix 1: Use mb_substitute_character() for Fallback

```php
function safeConvertEncoding(string $string, string $to, string $from): string {
    mb_substitute_character('?');

    $result = mb_convert_encoding($string, $to, $from, mb_substitute_character());

    return $result !== false ? $result : $string;
}
```

### Fix 2: Detect Source Encoding First

```php
function smartConvertEncoding(string $string, string $targetEncoding): string {
    $detected = mb_detect_encoding($string, ['UTF-8', 'ISO-8859-1', 'ASCII', 'SJIS']);

    if ($detected === false) {
        $detected = 'UTF-8';
    }

    if (strtoupper($detected) === strtoupper($targetEncoding)) {
        return $string;
    }

    mb_substitute_character('?');

    $result = mb_convert_encoding($string, $targetEncoding, $detected);

    return $result !== false ? $result : $string;
}
```

### Fix 3: Handle Strict Mode Gracefully

```php
function convertWithFallback(string $string, string $to, string $from): string {
    // Try strict conversion first
    $result = mb_convert_encoding($string, $to, $from, 'strict');

    if ($result !== false) {
        return $result;
    }

    // Fall back to substitution
    mb_substitute_character(0xFFFD); // Unicode replacement character
    $result = mb_convert_encoding($string, $to, $from);

    return $result !== false ? $result : $string;
}
```

### Fix 4: Sanitize Input Before Conversion

```php
function cleanAndConvert(string $string, string $targetEncoding): string {
    // Strip invalid byte sequences
    $cleaned = preg_replace('/[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]/u', '', $string);

    // Remove null bytes
    $cleaned = str_replace("\x00", '', $cleaned);

    mb_substitute_character('?');

    $result = mb_convert_encoding($cleaned, $targetEncoding, 'UTF-8');

    return $result !== false ? $result : $cleaned;
}
```

## Examples

```php
// Example: Safely convert user input to UTF-8
function sanitizeUserInput(string $input): string {
    $input = trim($input);
    $input = preg_replace('/[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]/', '', $input);

    $detected = mb_detect_encoding(
        $input,
        ['ASCII', 'UTF-8', 'ISO-8859-1', 'Windows-1252'],
        true
    );

    if ($detected !== 'UTF-8') {
        mb_substitute_character('?');
        $input = mb_convert_encoding($input, 'UTF-8', $detected);
    }

    return $input;
}
```

## Related Errors

- [mb_substr() illegal character offset](/languages/php/mbstring-illegal-offset/)
- [mbstring func_overload deprecation](/languages/php/mbstring-overloaded-warning/)
- [JSON encode error](/languages/php/json-encode-error/)
