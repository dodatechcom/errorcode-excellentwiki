---
title: "[Solution] PHP Warning: number_format() expects exactly 1 parameter"
description: "Fix PHP Warning: number_format() expects exactly 1 parameter (when called with 0). Provide correct parameters, check function signature."
languages: ["php"]
severities: ["warning"]
error-types: ["runtime-error"]
weight: 117
---

# PHP Warning: number_format() expects exactly 1 parameter

This warning occurs when `number_format()` is called with an incorrect number of arguments. In PHP 8, calling `number_format()` with no arguments triggers a warning because the function expects at least one parameter (the number to format).

## Common Causes

```php
// Cause 1: Calling number_format() with no arguments
<?php
$result = number_format();
// Warning: number_format() expects exactly 1 parameter, 0 given
?>
```

```php
// Cause 2: Passing null instead of a number
<?php
$value = null;
$formatted = number_format($value);
// Warning or deprecation depending on PHP version
?>
```

```php
// Cause 3: Wrong parameter types
<?php
$formatted = number_format("not a number", 2, ".", ",");
// Warning: not a valid numeric value
?>
```

```php
// Cause 4: Too many arguments
<?php
$formatted = number_format(1000.5, 2, ".", ",", "€", "extra");
// Warning in PHP < 8: too many arguments
?>
```

## How to Fix

### Fix 1: Provide Correct Parameters

Always pass at least the number to format.

```php
<?php
// WRONG — no arguments
$result = number_format();

// CORRECT — at least one argument
$price = 1234.56;
$formatted = number_format($price);           // 1,235
$formatted = number_format($price, 2);        // 1,234.56
$formatted = number_format($price, 2, '.', ','); // 1,234.56
?>
```

### Fix 2: Validate Input Before Formatting

Ensure the value is numeric before passing it to `number_format()`.

```php
<?php
function safeNumberFormat(mixed $value, int $decimals = 0): string
{
    if ($value === null || $value === '') {
        return number_format(0, $decimals);
    }

    if (!is_numeric($value)) {
        throw new \InvalidArgumentException(
            "Value must be numeric, got: " . get_debug_type($value)
        );
    }

    return number_format((float) $value, $decimals);
}

echo safeNumberFormat(null);          // 0
echo safeNumberFormat("1234.56", 2);  // 1,234.56
echo safeNumberFormat(1000);          // 1,000
?>
```

### Fix 3: Handle Currency and Locale Formatting

Use `localeconv()` and `NumberFormatter` for locale-aware formatting.

```php
<?php
// Basic number formatting
$price = 1234.56;

// US format
echo number_format($price, 2, '.', ',');  // 1,234.56

// European format
echo number_format($price, 2, ',', '.');  // 1.234,56

// Using NumberFormatter for locale-aware formatting
formatter = new \NumberFormatter('de_DE', \NumberFormatter::CURRENCY);
echo $formatter->formatCurrency($price, 'EUR');  // 1.234,56 €

$formatter = new \NumberFormatter('en_US', \NumberFormatter::CURRENCY);
echo $formatter->formatCurrency($price, 'USD');  // $1,234.56
?>
```

### Fix 4: Handle Variable Decimal Places

Dynamically determine decimal places based on the value.

```php
<?php
function formatSmart(mixed $value, int $maxDecimals = 2): string
{
    $num = filter_var($value, FILTER_VALIDATE_FLOAT);
    if ($num === false) {
        return '0';
    }

    // Determine needed decimal places
    $decimals = 0;
    if ($num != (int) $num) {
        $decimals = min($maxDecimals, strlen(substr(strrchr((string) $num, '.'), 1)));
    }

    return number_format($num, $decimals, '.', ',');
}

echo formatSmart(1000);       // 1,000
echo formatSmart(1000.5);     // 1,000.5
echo formatSmart(1000.50);    // 1,000.5
echo formatSmart(1000.123, 2); // 1,000.12
?>
```

## Examples

```php
<?php
// Complete number formatting utility
class NumberFormatter
{
    public static function format(
        float $number,
        int $decimals = 0,
        string $decPoint = '.',
        string $thousandsSep = ','
    ): string {
        return number_format($number, $decimals, $decPoint, $thousandsSep);
    }

    public static function currency(float $amount, string $symbol = '$'): string
    {
        return $symbol . number_format($amount, 2, '.', ',');
    }

    public static function percentage(float $value, int $decimals = 1): string
    {
        return number_format($value, $decimals) . '%';
    }

    public static function bytes(int $bytes): string
    {
        $units = ['B', 'KB', 'MB', 'GB', 'TB'];
        $i = 0;
        $size = (float) $bytes;

        while ($size >= 1024 && $i < count($units) - 1) {
            $size /= 1024;
            $i++;
        }

        return number_format($size, $i > 0 ? 2 : 0) . ' ' . $units[$i];
    }

    public static function abbreviate(int $number): string
    {
        if ($number >= 1e9) {
            return number_format($number / 1e9, 1) . 'B';
        }
        if ($number >= 1e6) {
            return number_format($number / 1e6, 1) . 'M';
        }
        if ($number >= 1e3) {
            return number_format($number / 1e3, 1) . 'K';
        }
        return (string) $number;
    }
}

echo NumberFormatter::format(1234567.89, 2);       // 1,234,567.89
echo "\n" . NumberFormatter::currency(49.99);       // $49.99
echo "\n" . NumberFormatter::percentage(75.5, 1);   // 75.5%
echo "\n" . NumberFormatter::bytes(1536);            // 1.50 KB
echo "\n" . NumberFormatter::abbreviate(2500000);    // 2.5M
?>
```

## Related Errors

- [PHP Warning: Wrong Parameter Count](/languages/php/warning-count)
- [PHP Warning: sprintf() Format](/languages/php/warning-in-sprintf)
- [PHP Warning: strlen() expects](/languages/php/warning-in-strlen)
