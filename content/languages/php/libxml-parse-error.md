---
title: "[Solution] PHP libxml Parsing Error — XML Parse Failed"
description: "Fix PHP libxml parsing error by validating XML structure, checking encoding, and using proper error reporting. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 14
---

# PHP libxml Parsing Error — XML Parse Failed

XML parsing failed because the document structure is invalid or contains syntax errors. This affects DOMDocument, SimpleXML, and any other libxml-based XML operations in PHP.

## Common Causes

```php
// Cause 1: Malformed XML
$xml = '<root><child>text</child><unclosed>';
$doc = new DOMDocument();
$doc->loadXML($xml); // Parse error

// Cause 2: Encoding mismatch
$xml = '<?xml version="1.0" encoding="UTF-8"?>' . '<root>' . chr(0xFF) . '</root>';
$doc = new DOMDocument();
$doc->loadXML($xml); // Invalid UTF-8

// Cause 3: Mismatched tags
$xml = '<root><child></child></rootWrong>';
$doc = new DOMDocument();
$doc->loadXML($xml); // Tag mismatch

// Cause 4: Invalid characters in XML
$xml = '<root>text\x00more text</root>';
$doc = new DOMDocument();
$doc->loadXML($xml); // Null character

// Cause 5: Incorrect namespace usage
$xml = '<root xmlns:ns="http://example.com"><ns:child/></root>';
$doc = new DOMDocument();
$doc->loadXML($xml); // May fail with namespace issues
```

## How to Fix

### Fix 1: Validate XML Structure Before Parsing

```php
function isXmlValid(string $xml): bool {
    libxml_use_internal_errors(true);

    $doc = new DOMDocument();
    $result = $doc->loadXML($xml);

    if (!$result) {
        libxml_clear_errors();
        libxml_use_internal_errors(false);
        return false;
    }

    libxml_clear_errors();
    libxml_use_internal_errors(false);
    return true;
}

// Quick syntax check
function checkXmlSyntax(string $xml): array {
    libxml_use_internal_errors(true);
    $doc = new DOMDocument();
    $doc->loadXML($xml);

    $errors = [];
    foreach (libxml_get_errors() as $error) {
        $errors[] = [
            'message' => trim($error->message),
            'line' => $error->line,
            'column' => $error->column,
            'level' => $error->level,
        ];
    }

    libxml_clear_errors();
    libxml_use_internal_errors(false);
    return $errors;
}
```

### Fix 2: Handle Character Encoding

```php
function safeLoadXml(string $xml, string $encoding = 'UTF-8'): ?DOMDocument {
    // Ensure valid UTF-8
    if ($encoding === 'UTF-8') {
        $xml = mb_convert_encoding($xml, 'UTF-8', 'UTF-8');
    }

    // Remove invalid XML characters (excluding allowed whitespace)
    $xml = preg_replace('/[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]/', '', $xml);

    libxml_use_internal_errors(true);
    $doc = new DOMDocument();

    if (!$doc->loadXML($xml)) {
        $errors = libxml_get_errors();
        libxml_clear_errors();
        libxml_use_internal_errors(false);
        error_log('XML parse failed: ' . (isset($errors[0]) ? trim($errors[0]->message) : 'unknown'));
        return null;
    }

    libxml_use_internal_errors(false);
    return $doc;
}
```

### Fix 3: Fix Common XML Issues Automatically

```php
function fixCommonXmlIssues(string $xml): string {
    // Add XML declaration if missing
    if (strpos($xml, '<?xml') === false) {
        $xml = '<?xml version="1.0" encoding="UTF-8"?>' . "\n" . $xml;
    }

    // Replace & with &amp; where not already encoded
    $xml = preg_replace('/&(?!amp;|lt;|gt;|quot;|apos;|#\d+;|#x[0-9a-fA-F]+;)/', '&amp;', $xml);

    // Remove control characters (except tab, newline, carriage return)
    $xml = preg_replace('/[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]/', '', $xml);

    // Convert to UTF-8 if needed
    $encoding = mb_detect_encoding($xml, ['UTF-8', 'ISO-8859-1', 'Windows-1252']);
    if ($encoding !== 'UTF-8') {
        $xml = mb_convert_encoding($xml, 'UTF-8', $encoding);
    }

    return $xml;
}
```

## Examples

```php
// Example: Robust XML parser with automatic fixing
function parseXmlRobustly(string $xml): ?DOMDocument {
    libxml_use_internal_errors(true);

    // First attempt: direct parse
    $doc = new DOMDocument();
    if ($doc->loadXML($xml)) {
        libxml_use_internal_errors(false);
        return $doc;
    }

    // Second attempt: fix common issues
    $fixed = fixCommonXmlIssues($xml);
    $doc = new DOMDocument();
    if ($doc->loadXML($fixed)) {
        libxml_use_internal_errors(false);
        return $doc;
    }

    // Log all errors
    foreach (libxml_get_errors() as $error) {
        error_log("XML parse error at line {$error->line}: " . trim($error->message));
    }
    libxml_clear_errors();
    libxml_use_internal_errors(false);

    return null;
}
```

## Related Errors

- [libxml error](/languages/php/libxml-error/)
- [libxml entity error](/languages/php/libxml-entity-error/)
- [libxml schema validation error](/languages/php/libxml-scheme-error/)
