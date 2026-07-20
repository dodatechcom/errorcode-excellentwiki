---
title: "[Solution] PHP MessageFormatter Pattern Syntax Errors"
description: "Fix PHP MessageFormatter pattern syntax errors by checking ICU message format, verifying placeholders, and handling plural rules. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 14
---

# PHP MessageFormatter Pattern Syntax Errors

The `MessageFormatter` class failed to format a message due to an invalid pattern, mismatched placeholders, or malformed plural rules. ICU message format syntax is strict and errors are often difficult to diagnose.

## Common Causes

```php
// Cause 1: Unmatched braces in pattern
$fmt = MessageFormatter::create('en_US', 'Hello {name!'); // Missing closing brace

// Cause 2: Mismatched placeholder names
$fmt = MessageFormatter::create('en_US', '{greeting} {name}');
$fmt->format(['welcome' => 'Hello', 'name' => 'World']); // Wrong key

// Cause 3: Invalid plural form
$fmt = MessageFormatter::create('en_US', '{count, plural, one {# item} other {# items}');
// Missing closing brace for plural

// Cause 4: Nested format with wrong syntax
$fmt = MessageFormatter::create('en_US', '{amount, number, currency}'); // Missing locale

// Cause 5: Special characters not escaped
$fmt = MessageFormatter::create('en_US', 'Price: ${amount}');
// $ is not special in ICU but curly brace issues cause problems
```

## How to Fix

### Fix 1: Validate Pattern Syntax

```php
function safeMessageFormatter(string $locale, string $pattern): ?MessageFormatter {
    $availableLocales = Locale::getAvailableLocales();

    if (!in_array($locale, $availableLocales, true)) {
        error_log("Invalid locale for MessageFormatter: {$locale}");
        $locale = 'en_US';
    }

    $formatter = MessageFormatter::create($locale, $pattern);

    if ($formatter === null) {
        error_log("Failed to create MessageFormatter with pattern: {$pattern}");
        return null;
    }

    return $formatter;
}
```

### Fix 2: Match Placeholders to Arguments

```php
function formatMessage(string $pattern, array $args, string $locale = 'en_US'): ?string {
    $fmt = safeMessageFormatter($locale, $pattern);
    if ($fmt === null) {
        return null;
    }

    $result = $fmt->format($args);

    if ($result === false) {
        error_log("MessageFormatter::format() failed: " . $fmt->getErrorMessage());
        return null;
    }

    return $result;
}
```

### Fix 3: Use Correct Plural Rules

```php
// Correct plural syntax
$pattern = '{count, plural, one {# item} other {# items}}';
$fmt = MessageFormatter::create('en_US', $pattern);
echo $fmt->format(['count' => 1]); // "1 item"
echo $fmt->format(['count' => 5]); // "5 items"

// Complex plural with offset
$pattern = '{elapsed, plural, =0 {just now} one {# second ago} other {# seconds ago}}';
$fmt = MessageFormatter::create('en_US', $pattern);
echo $fmt->format(['elapsed' => 0]); // "just now"
echo $fmt->format(['elapsed' => 1]); // "1 second ago"
echo $fmt->format(['elapsed' => 5]); // "5 seconds ago"
```

### Fix 4: Escape Special Characters Properly

```php
// Use single quotes to escape literal text in ICU format
$pattern = "It's a {type} '{name}' test";

// Or use # for number placeholders
$pattern = '{count, plural, one {# user} other {# users}}';

// For literal braces, use apostrophe escaping
$pattern = "This is '}' not a placeholder";
```

### Fix 5: Handle MessageFormatter Errors Gracefully

```php
function formatWithFallback(string $pattern, array $args, string $locale = 'en_US'): string {
    if (!extension_loaded('intl')) {
        // Simple str_replace fallback
        $result = $pattern;
        foreach ($args as $key => $value) {
            $result = str_replace('{' . $key . '}', (string)$value, $result);
        }
        return $result;
    }

    $fmt = MessageFormatter::create($locale, $pattern);
    if ($fmt === null) {
        return $pattern;
    }

    $result = $fmt->format($args);
    if ($result === false) {
        error_log("MessageFormatter error: " . $fmt->getErrorMessage());
        return $pattern;
    }

    return $result;
}
```

## Examples

```php
// Example: Localized notification messages
function getNotification(string $type, int $count, string $locale = 'en_US'): string {
    $patterns = [
        'upload' => '{count, plural, =0 {No files uploaded} one {# file uploaded} other {# files uploaded}}',
        'comment' => '{count, plural, =0 {No comments} one {# comment} other {# comments}}',
        'error' => '{count, plural, =0 {No errors} one {# error} other {# errors}}',
    ];

    $pattern = $patterns[$type] ?? '{count} items';

    return formatWithFallback($pattern, ['count' => $count], $locale);
}

echo getNotification('upload', 0, 'en_US'); // "No files uploaded"
echo getNotification('upload', 1, 'en_US'); // "1 file uploaded"
echo getNotification('upload', 5, 'en_US'); // "5 files uploaded"
```

## Related Errors

- [NumberFormatter errors](/languages/php/intl-numberformat-error/)
- [IntlDateFormatter errors](/languages/php/intl-dateformat-error/)
- [intl extension error](/languages/php/intl-error/)
