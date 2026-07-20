---
title: "[Solution] PHP XML_ERROR_INCORRECT_ENCODING — Incorrect Encoding Declaration"
description: "Fix PHP XML_ERROR_INCORRECT_ENCODING by matching declared encoding with actual content, using UTF-8, and validating encoding. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 19
---

# PHP XML_ERROR_INCORRECT_ENCODING — Incorrect Encoding Declaration

XML_ERROR_INCORRECT_ENCODING occurs when the encoding declared in the XML header doesn't match the actual encoding of the content. This mismatch causes the parser to misinterpret byte sequences, leading to parsing errors. The declared encoding must accurately reflect the actual character encoding of the document.

## Common Causes

```php
// Declared UTF-8 but content is ISO-8859-1
$xml = '<?xml version="1.0" encoding="UTF-8"?><root>Caf</root>'; // Actually ISO-8859-1
$parser = xml_parser_create('UTF-8');
xml_parse($parser, $xml); // XML_ERROR_INCORRECT_ENCODING
```

```php
// Wrong encoding declaration
$xml = '<?xml version="1.0" encoding="ASCII"?><root>Content</root>'; // Actually UTF-8
$parser = xml_parser_create('ASCII');
xml_parse($parser, $xml); // XML_ERROR_INCORRECT_ENCODING
```

```php
// Mismatched encoding parameter
$xml = '<?xml version="1.0" encoding="UTF-8"?><root>Content</root>';
$parser = xml_parser_create('ISO-8859-1'); // Wrong parameter
xml_parse($parser, $xml); // XML_ERROR_INCORRECT_ENCODING
```

```php
// Case mismatch
$xml = '<?xml version="1.0" encoding="utf-8"?><root>Content</root>'; // Should be UTF-8
$parser = xml_parser_create('UTF-8');
xml_parse($parser, $xml); // XML_ERROR_INCORRECT_ENCODING
```

```php
// Encoding declaration missing but parser expects one
$xml = '<?xml version="1.0"?><root>Content</root>';
$parser = xml_parser_create('ISO-8859-1');
xml_parse($parser, $xml); // XML_ERROR_INCORRECT_ENCODING
```

## How to Fix

### Fix 1: Match Declared Encoding with Actual Content

Ensure encoding declaration matches actual content:

```php
function detectActualEncoding($xml) {
    if (mb_check_encoding($xml, 'UTF-8')) {
        return 'UTF-8';
    }
    if (mb_check_encoding($xml, 'ISO-8859-1')) {
        return 'ISO-8859-1';
    }
    return 'UTF-8';
}

$detected = detectActualEncoding($xml);
$xml = preg_replace('/encoding="[^"]*"/', 'encoding="' . $detected . '"', $xml);
```

### Fix 2: Use UTF-8

Default to UTF-8 for maximum compatibility:

```php
// Convert to UTF-8
$xml = mb_convert_encoding($xml, 'UTF-8', mb_detect_encoding($xml));
$xml = preg_replace('/encoding="[^"]*"/', 'encoding="UTF-8"', $xml);

$parser = xml_parser_create('UTF-8');
xml_parse($parser, $xml);
xml_parser_free($parser);
```

### Fix 3: Validate Encoding

Check encoding consistency before parsing:

```php
function validateEncoding($xml) {
    preg_match('/encoding="([^"]*)"/', $xml, $matches);
    $declared = isset($matches[1]) ? strtoupper($matches[1]) : 'UTF-8';
    
    $actual = mb_detect_encoding($xml, ['UTF-8', 'ISO-8859-1', 'ASCII']);
    
    return strtoupper($actual) === $declared;
}

$xml = '<?xml version="1.0" encoding="UTF-8"?><root>Content</root>';
if (!validateEncoding($xml)) {
    echo "Encoding mismatch detected";
}
```

### Fix 4: Fix Encoding Mismatch

Automatically correct encoding declarations:

```php
function fixEncodingMismatch($xml) {
    $actual = mb_detect_encoding($xml, ['UTF-8', 'ISO-8859-1', 'ASCII']);
    
    if (strpos($xml, 'encoding=') !== false) {
        $xml = preg_replace('/encoding="[^"]*"/', 'encoding="' . $actual . '"', $xml);
    } else {
        $xml = str_replace('?>', ' encoding="' . $actual . '"?>', $xml);
    }
    
    return $xml;
}

$xml = '<?xml version="1.0" encoding="UTF-8"?><root>Content</root>';
$xml = fixEncodingMismatch($xml);
```

### Fix 5: Remove Encoding Declaration

If uncertain, remove the encoding declaration:

```php
function removeEncodingDeclaration($xml) {
    return preg_replace('/\s*encoding="[^"]*"/', '', $xml);
}

$xml = '<?xml version="1.0" encoding="UTF-8"?><root>Content</root>';
$xml = removeEncodingDeclaration($xml);
```

## Examples

```php
// Basic incorrect encoding detection
$xml = '<?xml version="1.0" encoding="UTF-8"?><root>Content</root>';
$parser = xml_parser_create('UTF-8');
xml_parse($parser, $xml);
$error = xml_get_error_code($parser);
if ($error === XML_ERROR_INCORRECT_ENCODING) {
    echo "Encoding mismatch detected";
}
xml_parser_free($parser);
```

```php
// Comprehensive encoding fix
function fixAllEncodingIssues($xml) {
    // Detect actual encoding
    $actual = mb_detect_encoding($xml, ['UTF-8', 'ISO-8859-1', 'ASCII']);
    
    // Convert to UTF-8
    if ($actual !== 'UTF-8') {
        $xml = mb_convert_encoding($xml, 'UTF-8', $actual);
    }
    
    // Fix declaration
    if (strpos($xml, 'encoding=') !== false) {
        $xml = preg_replace('/encoding="[^"]*"/', 'encoding="UTF-8"', $xml);
    } else {
        $xml = str_replace('?>', ' encoding="UTF-8"?>', $xml);
    }
    
    return $xml;
}

$xml = '<?xml version="1.0" encoding="UTF-8"?><root>Content</root>';
$xml = fixAllEncodingIssues($xml);
```

```php
// Validate encoding consistency
function validateEncodingConsistency($xml) {
    preg_match('/encoding="([^"]*)"/', $xml, $matches);
    $declared = isset($matches[1]) ? $matches[1] : null;
    
    $actual = mb_detect_encoding($xml, ['UTF-8', 'ISO-8859-1', 'ASCII']);
    
    if ($declared === null) {
        return true; // No declaration to validate
    }
    
    return strtoupper($declared) === strtoupper($actual);
}

$xml = '<?xml version="1.0" encoding="UTF-8"?><root>Content</root>';
if (validateEncodingConsistency($xml)) {
    echo "Encoding is consistent";
}
```

## Related Errors

- [XML_ERROR_UNKNOWN_ENCODING](xml-error-unknown-encoding.md) - Unknown character encoding
- [XML_ERROR_PARTIAL_CHAR](xml-error-partial-char.md) - Partial character sequence
- [XML_ERROR_INVALID_TOKEN](xml-error-invalid-token.md) - Invalid token in XML