---
title: "[Solution] PHP intl Error — Collator Error"
description: "Fix PHP intl extension errors. Resolve 'Collator error', locale handling failures, and intl function issues."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "php"
tags: ["php", "intl", "localization"]
severity: "error"
---

# PHP intl Extension Error

## Error Message

```
Collator::create(): Invalid locale: en_INVALID_LOCALE
```

## Common Causes

- An invalid or unsupported locale string was passed to a Collator or NumberFormatter
- The intl extension is not installed or loaded in the PHP environment
- The ICU data files are missing or outdated on the server

## Solutions

### Solution 1: Validate Locales Before Use

Check whether a locale is available before creating intl objects with it.

```php
<?php
function getValidCollator(string $locale = 'en_US'): Collator {
    $availableLocales = Locale::getAvailableLocales();

    if (!in_array($locale, $availableLocales, true)) {
        error_log("Unsupported locale: $locale — falling back to en_US");
        $locale = 'en_US';
    }

    $collator = Collator::create($locale);
    if ($collator === null) {
        throw new RuntimeException("Failed to create Collator for locale: $locale");
    }

    return $collator;
}

// Usage
$collator = getValidCollator($_GET['lang'] ?? 'en_US');
$names = ['Zoë', 'Alice', 'Böb', 'André'];
$collator->asort($names);
print_r($names);
?>
```

### Solution 2: Handle Missing intl Extension Gracefully

Provide fallback implementations when the intl extension is not available.

```php
<?php
function localeSort(array $items, string $locale = 'en_US'): array {
    if (extension_loaded('intl')) {
        $collator = Collator::create($locale);
        if ($collator !== null) {
            $collator->asort($items);
            return $items;
        }
    }

    // Fallback: use PHP's built-in locale-aware sorting
    setlocale(LC_COLLATE, "$locale.UTF-8", $locale);
    usort($items, function (string $a, string $b) {
        return strcoll($a, $b);
    });
    return $items;
}

// Usage — works with or without intl
$sorted = localeSort(['München', 'Amsterdam', 'Zürich'], 'de_DE');
print_r($sorted);
?>
```

## Prevention Tips

- Install the intl extension: `sudo apt install php8.2-intl` on Debian/Ubuntu
- Check available locales with `Locale::getAvailableLocales()`
- Keep the ICU library updated for correct locale behavior

## Related Errors

- [Mbstring Error]({{< relref "/languages/php/mbstring-error" >}})
- [Json Encode Error]({{< relref "/languages/php/json-encode-error" >}})
