---
title: "[Solution] PHP Transliterator Creation Failures"
description: "Fix PHP Transliterator creation failures by checking transliterator ID, verifying rule syntax, and handling invalid rules. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 14
---

# PHP Transliterator Creation Failures

The `Transliterator::create()` or `Transliterator::createFromRules()` method failed to create a transliterator. This happens when the transliterator ID is not recognized, the rule syntax is invalid, or the intl extension is not loaded.

## Common Causes

```php
// Cause 1: Invalid transliterator ID
$tr = Transliterator::create('Invalid_Transliterator');

// Cause 2: Invalid rule syntax
$tr = Transliterator::createFromRules(':: Any-Latin; :: Latin-ASCII;');

// Cause 3: Using non-existent ID
$tr = Transliterator::create('NonExistent-Script');

// Cause 4: Missing intl extension
$tr = Transliterator::create('Any-Latin'); // Function not defined

// Cause 5: Compound ID with invalid separator
$tr = Transliterator::create('Any-Latin;;Latin-ASCII');
```

## How to Fix

### Fix 1: Validate Transliterator ID

```php
function safeTransliterator(string $id): ?Transliterator {
    if (!extension_loaded('intl')) {
        error_log('Transliterator requires the intl extension');
        return null;
    }

    $validIds = Transliterator::listIDs();

    if (!in_array($id, $validIds, true)) {
        error_log("Invalid transliterator ID: {$id}");
        error_log("Available IDs: " . implode(', ', array_slice($validIds, 0, 10)));
        return null;
    }

    $tr = Transliterator::create($id);

    if ($tr === null) {
        error_log("Failed to create Transliterator for ID: {$id}");
        return null;
    }

    return $tr;
}
```

### Fix 2: Use Safe Rule Syntax

```php
function safeTransliteratorFromRules(string $rules): ?Transliterator {
    if (!extension_loaded('intl')) {
        return null;
    }

    $tr = Transliterator::createFromRules($rules);

    if ($tr === null) {
        error_log("Invalid transliterator rules: {$rules}");
        return null;
    }

    return $tr;
}
```

### Fix 3: Use Compound IDs Safely

```php
function createCompoundTransliterator(array $ids): ?Transliterator {
    $validIds = Transliterator::listIDs();
    $validChain = [];

    foreach ($ids as $id) {
        if (in_array($id, $validIds, true)) {
            $validChain[] = $id;
        } else {
            error_log("Skipping invalid transliterator ID: {$id}");
        }
    }

    if (empty($validChain)) {
        return null;
    }

    $compoundId = implode(';', $validChain);
    $tr = Transliterator::create($compoundId);

    if ($tr === null) {
        error_log("Failed to create compound transliterator: {$compoundId}");
        return null;
    }

    return $tr;
}
```

### Fix 4: Fallback Transliteration Without intl

```php
function transliterateSafe(string $text, string $rules = 'Any-Latin; Latin-ASCII'): string {
    if (extension_loaded('intl')) {
        $tr = Transliterator::create($rules);
        if ($tr !== null) {
            $result = $tr->transliterate($text);
            if ($result !== false) {
                return $result;
            }
        }
    }

    // Basic fallback: strip non-ASCII
    return preg_replace('/[^\x20-\x7E]/u', '', $text);
}
```

## Examples

```php
// Example: Slug generator using Transliterator
function generateSlug(string $title, string $locale = 'en'): string {
    $title = strtolower(trim($title));

    if (extension_loaded('intl')) {
        // Transliterate non-Latin characters to ASCII
        $tr = Transliterator::create('Any-Latin; Latin-ASCII');
        if ($tr !== null) {
            $title = $tr->transliterate($title);
        }
    }

    // Replace non-alphanumeric characters with hyphens
    $title = preg_replace('/[^a-z0-9]+/', '-', $title);

    // Trim hyphens from both ends
    $title = trim($title, '-');

    return $title;
}

echo generateSlug('Ünlaut über Ärger'); // "unlaut-uber-arger"
echo generateSlug('日本語テスト'); // "riben-yu-testu" or similar
```

## Related Errors

- [intl extension error](/languages/php/intl-error/)
- [IDN conversion errors](/languages/php/intl-idn-error/)
- [mbstring encoding errors](/languages/php/mbstring-encoding-error/)
