---
title: "[Solution] PHP NumberFormatter Creation/Formatting Failures"
description: "Fix PHP NumberFormatter creation and formatting failures by checking locale, verifying pattern syntax, and handling INTL_ICU_DATA_ERROR. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 14
---

# PHP NumberFormatter Creation/Formatting Failures

The `NumberFormatter` class failed to create an instance or format a number. This happens when an invalid locale is provided, the ICU pattern syntax is incorrect, or the ICU data files are missing.

## Common Causes

```php
// Cause 1: Invalid locale
$fmt = NumberFormatter::create('xx_INVALID', NumberFormatter::DECIMAL);

// Cause 2: Invalid pattern syntax
$fmt = NumberFormatter::create('en_US', NumberFormatter::PATTERN_RULEBASED);
$fmt = $fmt->setPattern('#,##0.## '); // Trailing space may cause issues

// Cause 3: Missing ICU data
$fmt = NumberFormatter::create('en_US', NumberFormatter::CURRENCY);

// Cause 4: Formatting with wrong type
$fmt = NumberFormatter::create('en_US', NumberFormatter::CURRENCY);
echo $fmt->format(100); // May fail without currency code

// Cause 5: null locale with PATTERN_RULEBASED
$fmt = NumberFormatter::create(null, NumberFormatter::PATTERN_RULEBASED);
```

## How to Fix

### Fix 1: Validate Locale Before Creating Formatter

```php
function safeNumberFormatter(string $locale = null, int $style = NumberFormatter::DECIMAL): ?NumberFormatter {
    if ($locale === null) {
        $locale = Locale::getDefault();
    }

    $availableLocales = Locale::getAvailableLocales();

    if (!in_array($locale, $availableLocales, true)) {
        error_log("Invalid locale for NumberFormatter: {$locale}");
        $locale = 'en_US';
    }

    $formatter = NumberFormatter::create($locale, $style);

    if ($formatter === null) {
        error_log("Failed to create NumberFormatter for locale: {$locale}");
        return null;
    }

    return $formatter;
}
```

### Fix 2: Use Safe Pattern Syntax

```php
function formatNumber(float $number, string $locale = 'en_US', string $pattern = null): ?string {
    $fmt = safeNumberFormatter($locale);
    if ($fmt === null) {
        return null;
    }

    if ($pattern !== null) {
        if ($fmt->setPattern($pattern) === false) {
            error_log("Invalid pattern: {$pattern}");
            return null;
        }
    }

    $result = $fmt->format($number);
    if ($result === false) {
        error_log("NumberFormatter::format() failed");
        return null;
    }

    return $result;
}
```

### Fix 3: Handle Currency Formatting Properly

```php
function formatCurrency(float $amount, string $currencyCode, string $locale = 'en_US'): ?string {
    $fmt = safeNumberFormatter($locale, NumberFormatter::CURRENCY);
    if ($fmt === null) {
        return null;
    }

    $result = $fmt->formatCurrency($amount, $currencyCode);
    if ($result === false) {
        error_log("formatCurrency() failed for {$currencyCode}");
        return null;
    }

    return $result;
}
```

### Fix 4: Fallback for Missing ICU Data

```php
function formatNumberSafe(float $number, int $decimals = 2): string {
    if (extension_loaded('intl')) {
        $fmt = NumberFormatter::create('en_US', NumberFormatter::DECIMAL);
        if ($fmt !== null) {
            $fmt->setAttribute(NumberFormatter::MIN_FRACTION_DIGITS, $decimals);
            $fmt->setAttribute(NumberFormatter::MAX_FRACTION_DIGITS, $decimals);
            $result = $fmt->format($number);
            if ($result !== false) {
                return $result;
            }
        }
    }

    // Fallback to number_format()
    return number_format($number, $decimals, '.', ',');
}
```

## Examples

```php
// Example: Format prices for multiple locales
function formatPrice(float $price, string $locale, string $currency): string {
    $fmt = safeNumberFormatter($locale, NumberFormatter::CURRENCY);
    if ($fmt === null) {
        return number_format($price, 2) . ' ' . $currency;
    }

    $result = $fmt->formatCurrency($price, $currency);
    return $result !== false ? $result : number_format($price, 2) . ' ' . $currency;
}

$locales = ['en_US', 'de_DE', 'ja_JP', 'fr_FR'];
foreach ($locales as $locale) {
    echo formatPrice(1234.56, $locale, 'USD') . "\n";
}
```

## Related Errors

- [IntlDateFormatter errors](/languages/php/intl-dateformat-error/)
- [MessageFormatter pattern errors](/languages/php/intl-messageformatter-error/)
- [intl extension error](/languages/php/intl-error/)
