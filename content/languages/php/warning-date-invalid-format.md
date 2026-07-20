---
title: "[Solution] PHP Warning: date() — Invalid Format"
description: "Fix PHP Warning: date() invalid format. Check format characters, use DateTime class, validate format string."
languages: ["php"]
severities: ["warning"]
error-types: ["runtime-error"]
weight: 9
---

# PHP Warning: date() — Invalid Format

This warning occurs when `date()` or `DateTime::format()` receives an invalid format string. PHP format characters must follow specific syntax, and using unrecognized characters or malformed patterns triggers this warning.

## Common Causes

```php
<?php
// Example 1: Using non-existent format character
echo date("Y-m-d X", time());
// Warning: date(): Invalid format "X"
```

```php
<?php
// Example 2: Unclosed bracket in format
echo date("Y-m-d [", time());
// Warning: date(): Invalid format "["
```

```php
<?php
// Example 3: Double percent without escaping
echo date("Y%%m%%d", time());
// Warning: date(): Invalid format
```

```php
<?php
// Example 4: Custom format from user input
$userFormat = $_GET["format"] ?? "";
echo date($userFormat, time());
// Warning: date(): Invalid format "..."
```

```php
<?php
// Example 5: Misspelled format character
echo date("Y-m-d H:i:sa", time()); // "sa" is not a valid combination
// Warning: date(): Invalid format "sa"
```

## How to Fix

### Fix 1: Use Valid Format Characters

Stick to PHP's documented format characters.

```php
<?php
// Valid format characters:
// Y - 4-digit year (2026)
// m - Month with leading zero (01-12)
// d - Day with leading zero (01-31)
// H - Hour 24-format (00-23)
// i - Minutes (00-59)
// s - Seconds (00-59)
// A - AM/PM uppercase
// l - Day of week name

echo date("Y-m-d H:i:s", time()); // 2026-07-20 14:30:00
```

### Fix 2: Use the DateTime Class

The `DateTime` class provides a more robust approach with better error handling.

```php
<?php
$date = new DateTime();
echo $date->format("Y-m-d H:i:s"); // 2026-07-20 14:30:00

// With timezone
$date = new DateTime("now", new DateTimeZone("America/New_York"));
echo $date->format("Y-m-d H:i:s T"); // 2026-07-20 10:30:00 EDT
```

### Fix 3: Validate Format Before Use

Check the format string against a whitelist of allowed characters.

```php
<?php
function safeDateFormat(string $format, int $timestamp = null): string|false {
    $allowedChars = ['Y', 'm', 'd', 'H', 'i', 's', 'A', 'a', 'D', 'l', 'N',
                     'w', 'z', 't', 'L', 'o', 'W', 'M', 'F', 'n', 'j',
                     'G', 'g', 'h', 'u', 'B', 'U', 'P', 'T', 'Z', 'e',
                     'I', 'O', 'P'];

    $cleaned = str_replace('%', '', $format);
    $chars = str_split($cleaned);

    foreach ($chars as $char) {
        if (!in_array($char, $allowedChars, true) && !ctype_digit($char) && $char !== '-') {
            return false;
        }
    }

    return date($format, $timestamp ?? time());
}

$result = safeDateFormat("Y-m-d");
$result = safeDateFormat("X"); // false — invalid format
```

### Fix 4: Escape Literal Characters with Backslashes

Use backslashes to include literal characters in the format string.

```php
<?php
// WRONG: "sa" is invalid
echo date("Y-m-d H:i:sa", time());

// CORRECT: escape literal characters
echo date("Y-m-d H:i:s a", time()); // 2026-07-20 14:30:00 pm

// Or use DateTime
$date = new DateTime();
echo $date->format("Y-m-d\\a"); // Literal "a" after day
```

### Fix 5: Use intlDateFormatter for Localization

For locale-aware date formatting, use the `IntlDateFormatter` class.

```php
<?php
$formatter = new IntlDateFormatter(
    "en_US",
    IntlDateFormatter::FULL,
    IntlDateFormatter::NONE,
    "America/New_York"
);

echo $formatter->format(new DateTime()); // Sunday, July 20, 2026
```

## Examples

```php
<?php
// Common valid format patterns
$formats = [
    "Y-m-d"           => "2026-07-20",
    "Y-m-d H:i:s"     => "2026-07-20 14:30:00",
    "d/m/Y"            => "20/07/2026",
    "F j, Y"           => "July 20, 2026",
    "l, F j, Y, g:i A" => "Sunday, July 20, 2026, 2:30 PM",
    "Y-m-d\\TH:i:sP"  => "2026-07-20T14:30:00-04:00",
];

foreach ($formats as $format => $expected) {
    $result = date($format);
    echo "{$format} => {$result}\n";
}
```

## Related Errors

- [PHP Warning: date() Timezone](/languages/php/warning-date)
- [PHP Deprecated Filter](/languages/php/deprecated-filter)
- [PHP Warning: Headers Already Sent](/languages/php/warning-headers-sent-already)
