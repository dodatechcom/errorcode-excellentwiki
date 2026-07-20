---
title: "[Solution] PHP IntlDateFormatter Locale/Date Formatting Errors"
description: "Fix PHP IntlDateFormatter locale and date formatting errors by checking locale, verifying date pattern, and handling timezone issues. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 14
---

# PHP IntlDateFormatter Locale/Date Formatting Errors

The `IntlDateFormatter` class failed to create an instance or format a date. This happens when an invalid locale is provided, the date pattern is malformed, or the timezone cannot be resolved.

## Common Causes

```php
// Cause 1: Invalid locale
$fmt = IntlDateFormatter::create('xx_INVALID', IntlDateFormatter::FULL, IntlDateFormatter::NONE);

// Cause 2: Invalid date pattern
$fmt = IntlDateFormatter::create('en_US', IntlDateFormatter::FULL, IntlDateFormatter::NONE, 'Europe/London');
$fmt->setPattern('yyyy-MM-dd HH:mm:ss'); // May fail with wrong type

// Cause 3: Invalid timezone identifier
$fmt = IntlDateFormatter::create('en_US', IntlDateFormatter::FULL, IntlDateFormatter::NONE, 'Invalid/Timezone');

// Cause 4: Formatting null or invalid timestamp
$fmt = IntlDateFormatter::create('en_US', IntlDateFormatter::FULL, IntlDateFormatter::NONE, 'UTC');
echo $fmt->format(null); // May produce unexpected result

// Cause 5: Using calendar parameter with wrong locale
$fmt = IntlDateFormatter::create('en_US', IntlDateFormatter::FULL, IntlDateFormatter::NONE, null, IntlDateFormatter::GREGORIAN, 'japanese');
```

## How to Fix

### Fix 1: Validate Locale and Timezone

```php
function safeDateFormatter(
    string $locale = null,
    int $dateType = IntlDateFormatter::FULL,
    int $timeType = IntlDateFormatter::NONE,
    string $timezone = null
): ?IntlDateFormatter {
    if ($locale === null) {
        $locale = Locale::getDefault();
    }

    $availableLocales = Locale::getAvailableLocales();
    if (!in_array($locale, $availableLocales, true)) {
        error_log("Invalid locale for IntlDateFormatter: {$locale}");
        $locale = 'en_US';
    }

    if ($timezone !== null && DateTimeZone::listIdentifiers().length > 0) {
        if (!in_array($timezone, DateTimeZone::listIdentifiers(), true)) {
            error_log("Invalid timezone: {$timezone}");
            $timezone = 'UTC';
        }
    }

    $formatter = IntlDateFormatter::create($locale, $dateType, $timeType, $timezone);

    if ($formatter === null) {
        error_log("Failed to create IntlDateFormatter for locale: {$locale}");
        return null;
    }

    return $formatter;
}
```

### Fix 2: Use Safe Pattern Syntax

```php
function formatDateWithPattern(int $timestamp, string $pattern, string $locale = 'en_US'): ?string {
    $fmt = safeDateFormatter($locale);
    if ($fmt === null) {
        return null;
    }

    if ($fmt->setPattern($pattern) === false) {
        error_log("Invalid date pattern: {$pattern}");
        return null;
    }

    $result = $fmt->format($timestamp);
    if ($result === false) {
        error_log("IntlDateFormatter::format() failed");
        return null;
    }

    return $result;
}
```

### Fix 3: Handle Timezone Fallback

```php
function formatDateSafe(DateTimeInterface $date, string $locale = 'en_US'): string {
    if (extension_loaded('intl')) {
        $fmt = IntlDateFormatter::create(
            $locale,
            IntlDateFormatter::MEDIUM,
            IntlDateFormatter::MEDIUM,
            $date->getTimezone()->getName()
        );

        if ($fmt !== null) {
            $result = $fmt->format($date);
            if ($result !== false) {
                return $result;
            }
        }
    }

    // Fallback to DateTime::format()
    return $date->format('Y-m-d H:i:s');
}
```

### Fix 4: Use DateIntervalFormatter for Relative Dates

```php
function formatRelativeDate(DateTimeInterface $past, DateTimeInterface $now, string $locale = 'en_US'): string {
    if (extension_loaded('intl')) {
        $interval = $past->diff($now);
        $fmt = DateIntervalFormatter::create($locale, '%in %duration');

        if ($fmt !== null) {
            $result = $fmt->format($interval);
            if ($result !== false) {
                return $result;
            }
        }
    }

    $diff = $now->getTimestamp() - $past->getTimestamp();
    $hours = (int)($diff / 3600);

    if ($hours < 1) return 'just now';
    if ($hours < 24) return "{$hours}h ago";
    $days = (int)($hours / 24);
    return "{$days}d ago";
}
```

## Examples

```php
// Example: Format dates for multiple locales
function formatForLocales(DateTimeInterface $date, array $locales): array {
    $results = [];

    foreach ($locales as $locale) {
        $fmt = IntlDateFormatter::create(
            $locale,
            IntlDateFormatter::LONG,
            IntlDateFormatter::SHORT,
            'UTC'
        );

        if ($fmt !== null) {
            $results[$locale] = $fmt->format($date);
        } else {
            $results[$locale] = $date->format('Y-m-d H:i');
        }
    }

    return $results;
}

$date = new DateTime('2026-07-15T14:30:00');
$formats = formatForLocales($date, ['en_US', 'de_DE', 'ja_JP', 'ar_SA']);
```

## Related Errors

- [NumberFormatter errors](/languages/php/intl-numberformat-error/)
- [MessageFormatter pattern errors](/languages/php/intl-messageformatter-error/)
- [intl extension error](/languages/php/intl-error/)
