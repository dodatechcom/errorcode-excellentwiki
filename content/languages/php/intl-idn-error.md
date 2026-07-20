---
title: "[Solution] PHP idn_to_ascii()/idn_to_utf8() Failures"
description: "Fix PHP idn_to_ascii()/idn_to_utf8() failures by checking INTL_IDNA_VARIANT, verifying domain format, and handling encoding errors. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 14
---

# PHP idn_to_ascii()/idn_to_utf8() Failures

The `idn_to_ascii()` or `idn_to_utf8()` function failed to convert an internationalized domain name. This happens when the domain format is invalid, the IDNA variant is incorrect, or the intl extension is not loaded.

## Common Causes

```php
// Cause 1: Invalid domain format
$ascii = idn_to_ascii('not a domain name');

// Cause 2: Missing intl extension
$ascii = idn_to_ascii('example.com'); // Function not defined

// Cause 3: Invalid IDNA variant (deprecated variant)
$ascii = idn_to_ascii('münchen.de', IDNA_NONTRANSITIONAL_TO_ASCII, INTL_IDNA_VARIANT_2003);

// Cause 4: Empty or null domain
$ascii = idn_to_ascii('');

// Cause 5: Domain with invalid characters
$ascii = idn_to_ascii('exam ple.com');
```

## How to Fix

### Fix 1: Validate Domain Before Conversion

```php
function safeIdnToAscii(string $domain): ?string {
    if (!function_exists('idn_to_ascii')) {
        error_log('idn_to_ascii() requires the intl extension');
        return null;
    }

    $domain = trim($domain, '.');

    if (empty($domain)) {
        error_log('Empty domain provided for IDN conversion');
        return null;
    }

    if (preg_match('/\s/', $domain)) {
        error_log("Domain contains whitespace: {$domain}");
        return null;
    }

    $ascii = idn_to_ascii(
        $domain,
        IDNA_NONTRANSITIONAL_TO_ASCII,
        INTL_IDNA_VARIANT_UTS46
    );

    if ($ascii === false) {
        error_log("idn_to_ascii() failed for: {$domain}");
        return null;
    }

    return $ascii;
}
```

### Fix 2: Use Modern IDNA Variant (UTS46)

```php
function convertDomainToAscii(string $domain): ?string {
    if (!function_exists('idn_to_ascii')) {
        return null;
    }

    // Use INTL_IDNA_VARIANT_UTS46 (recommended for PHP 7.2+)
    $ascii = idn_to_ascii(
        $domain,
        IDNA_NONTRANSITIONAL_TO_ASCII,
        INTL_IDNA_VARIANT_UTS46
    );

    if ($ascii === false) {
        // Fallback to 2003 variant
        $ascii = idn_to_ascii(
            $domain,
            IDNA_DEFAULT,
            INTL_IDNA_VARIANT_2003
        );
    }

    return $ascii !== false ? $ascii : null;
}
```

### Fix 3: Handle Both Directions Safely

```php
function idnToUtf8Safe(string $asciiDomain): ?string {
    if (!function_exists('idn_to_utf8')) {
        error_log('idn_to_utf8() requires the intl extension');
        return null;
    }

    $utf8 = idn_to_utf8(
        $asciiDomain,
        IDNA_NONTRANSITIONAL_TO_UTF8,
        INTL_IDNA_VARIANT_UTS46
    );

    if ($utf8 === false) {
        error_log("idn_to_utf8() failed for: {$asciiDomain}");
        return null;
    }

    return $utf8;
}

function idnToAsciiSafe(string $utf8Domain): ?string {
    if (!function_exists('idn_to_ascii')) {
        error_log('idn_to_ascii() requires the intl extension');
        return null;
    }

    $ascii = idn_to_ascii(
        $utf8Domain,
        IDNA_NONTRANSITIONAL_TO_ASCII,
        INTL_IDNA_VARIANT_UTS46
    );

    if ($ascii === false) {
        error_log("idn_to_ascii() failed for: {$utf8Domain}");
        return null;
    }

    return $ascii;
}
```

### Fix 4: Fallback Without intl Extension

```php
function convertDomainSafe(string $domain): string {
    if (function_exists('idn_to_ascii')) {
        $result = idn_to_ascii(
            $domain,
            IDNA_NONTRANSITIONAL_TO_ASCII,
            INTL_IDNA_VARIANT_UTS46
        );

        if ($result !== false) {
            return $result;
        }
    }

    // Fallback: use punycode encoding manually or return as-is
    return $domain;
}
```

## Examples

```php
// Example: Validate and convert international domain names
function validateInternationalDomain(string $domain): array {
    $result = [
        'original' => $domain,
        'ascii' => null,
        'utf8' => null,
        'valid' => false,
    ];

    $ascii = safeIdnToAscii($domain);
    if ($ascii === null) {
        return $result;
    }

    $result['ascii'] = $ascii;
    $result['valid'] = true;

    if (function_exists('idn_to_utf8')) {
        $result['utf8'] = idn_to_utf8($ascii, IDNA_NONTRANSITIONAL_TO_UTF8, INTL_IDNA_VARIANT_UTS46);
    }

    return $result;
}

$domains = ['münchen.de', '例え.jp', 'prueba.com', 'مثال.شبكة'];
foreach ($domains as $domain) {
    $info = validateInternationalDomain($domain);
    echo "{$info['original']} -> {$info['ascii']} (valid: " . ($info['valid'] ? 'yes' : 'no') . ")\n";
}
```

## Related Errors

- [intl extension error](/languages/php/intl-error/)
- [Transliterator errors](/languages/php/intl-transliterator-error/)
- [NumberFormatter errors](/languages/php/intl-numberformat-error/)
