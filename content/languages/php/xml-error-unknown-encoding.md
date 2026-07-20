---
title: "[Solution] PHP XML_ERROR_UNKNOWN_ENCODING — Unknown Character Encoding"
description: "Fix PHP XML_ERROR_UNKNOWN_ENCODING by specifying correct encoding, using UTF-8, and declaring encoding in XML header. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 18
---

# PHP XML_ERROR_UNKNOWN_ENCODING — Unknown Character Encoding

XML_ERROR_UNKNOWN_ENCODING occurs when the XML parser encounters an encoding that it doesn't recognize. This can happen when the encoding declared in the XML header doesn't match what the parser supports, or when the encoding name is misspelled. The parser needs to know the correct encoding to properly interpret the byte sequences.

## Common Causes

```php
// Unknown encoding declaration
$xml = '<?xml version="1.0" encoding="UNKNOWN"?>
<root>Content</root>';
$parser = xml_parser_create('UNKNOWN');
xml_parse($parser, $xml); // XML_ERROR_UNKNOWN_ENCODING
```

```php
// Misspelled encoding name
$xml = '<?xml version="1.0" encoding="UTF8"?>
<root>Content</root>';
$parser = xml_parser_create('UTF8');
xml_parse($parser, $xml); // XML_ERROR_UNKNOWN_ENCODING
```

```php
// Unsupported encoding
$xml = '<?xml version="1.0" encoding="EBCDIC"?>
<root>Content</root>';
$parser = xml_parser_create('EBCDIC');
xml_parse($parser, $xml); // XML_ERROR_UNKNOWN_ENCODING
```

```php
// Missing encoding declaration
$xml = '<?xml version="1.0"?>
<root>Content</root>';
$parser = xml_parser_create('ISO-8859-1');
xml_parse($parser, $xml); // XML_ERROR_UNKNOWN_ENCODING
```

```php
// Case sensitivity issue
$xml = '<?xml version="1.0" encoding="utf-8"?>
<root>Content</root>';
$parser = xml_parser_create('utf-8');
xml_parse($parser, $xml); // XML_ERROR_UNKNOWN_ENCODING
```

## How to Fix

### Fix 1: Specify Correct Encoding

Use a supported encoding name:

```php
// Supported encodings
$supported = ['UTF-8', 'ISO-8859-1', 'US-ASCII'];

$xml = '<?xml version="1.0" encoding="UTF-8"?>
<root>Content</root>';
$parser = xml_parser_create('UTF-8');
xml_parse($parser, $xml);
xml_parser_free($parser);
```

### Fix 2: Use UTF-8

Default to UTF-8 which is most commonly supported:

```php
// Always use UTF-8
$xml = '<?xml version="1.0" encoding="UTF-8"?>
<root>Content</root>';
$parser = xml_parser_create('UTF-8');
xml_parse($parser, $xml);
xml_parser_free($parser);
```

### Fix 3: Declare Encoding in XML Header

Ensure encoding is properly declared:

```php
function addEncodingDeclaration($xml, $encoding = 'UTF-8') {
    if (strpos($xml, '<?xml') === false) {
        $xml = '<?xml version="1.0" encoding="' . $encoding . '"?>' . $xml;
    } else {
        // Replace existing encoding declaration
        $xml = preg_replace(
            '/encoding="[^"]*"/',
            'encoding="' . $encoding . '"',
            $xml
        );
    }
    return $xml;
}

$xml = '<root>Content</root>';
$xml = addEncodingDeclaration($xml, 'UTF-8');
```

### Fix 4: Validate Encoding

Check if encoding is supported before parsing:

```php
function isSupportedEncoding($encoding) {
    $supported = [
        'UTF-8', 'ISO-8859-1', 'ISO-8859-2', 'ISO-8859-3',
        'ISO-8859-4', 'ISO-8859-5', 'ISO-8859-6', 'ISO-8859-7',
        'ISO-8859-8', 'ISO-8859-9', 'ISO-8859-10', 'ISO-8859-13',
        'ISO-8859-14', 'ISO-8859-15', 'ISO-8859-16',
        'US-ASCII', 'WINDOWS-1252', 'WINDOWS-1251'
    ];
    
    return in_array(strtoupper($encoding), $supported);
}

$encoding = 'UTF-8';
if (!isSupportedEncoding($encoding)) {
    $encoding = 'UTF-8';
}
```

### Fix 5: Convert Encoding

Convert content to a supported encoding:

```php
function convertToSupportedEncoding($xml, $targetEncoding = 'UTF-8') {
    // Detect current encoding
    $currentEncoding = mb_detect_encoding($xml, ['UTF-8', 'ISO-8859-1', 'ASCII']);
    
    if ($currentEncoding !== $targetEncoding) {
        $xml = mb_convert_encoding($xml, $targetEncoding, $currentEncoding);
    }
    
    // Update encoding declaration
    $xml = addEncodingDeclaration($xml, $targetEncoding);
    
    return $xml;
}

$xml = '<?xml version="1.0" encoding="LATIN1"?>
<root>Content</root>';
$xml = convertToSupportedEncoding($xml, 'UTF-8');
```

## Examples

```php
// Basic unknown encoding detection
$xml = '<?xml version="1.0" encoding="UNKNOWN"?>
<root>Content</root>';
$parser = xml_parser_create('UNKNOWN');
xml_parse($parser, $xml);
$error = xml_get_error_code($parser);
if ($error === XML_ERROR_UNKNOWN_ENCODING) {
    echo "Unknown encoding: UNKNOWN";
}
xml_parser_free($parser);
```

```php
// Safe encoding handling
function safeEncodingParse($xml) {
    // Extract encoding from declaration
    preg_match('/encoding="([^"]*)"/', $xml, $matches);
    $declaredEncoding = isset($matches[1]) ? $matches[1] : 'UTF-8';
    
    // Validate encoding
    if (!isSupportedEncoding($declaredEncoding)) {
        $declaredEncoding = 'UTF-8';
        $xml = addEncodingDeclaration($xml, $declaredEncoding);
    }
    
    $parser = xml_parser_create($declaredEncoding);
    xml_parse($parser, $xml);
    $error = xml_get_error_code($parser);
    xml_parser_free($parser);
    
    return $error === XML_ERROR_NONE;
}

$xml = '<?xml version="1.0" encoding="UTF-8"?>
<root>Content</root>';

if (safeEncodingParse($xml)) {
    echo "Parsed successfully";
}
```

```php
// Fix all encoding issues
function fixEncodingIssues($xml) {
    // Convert to UTF-8
    $xml = convertToSupportedEncoding($xml, 'UTF-8');
    
    // Ensure valid UTF-8
    if (!mb_check_encoding($xml, 'UTF-8')) {
        $xml = mb_convert_encoding($xml, 'UTF-8', 'auto');
    }
    
    return $xml;
}

$xml = '<?xml version="1.0" encoding="UNKNOWN"?>
<root>Content</root>';
$xml = fixEncodingIssues($xml);
```

```php
// List supported encodings
function getSupportedEncodings() {
    return [
        'UTF-8', 'ISO-8859-1', 'US-ASCII',
        'WINDOWS-1252', 'WINDOWS-1251'
    ];
}

$supported = getSupportedEncodings();
echo "Supported encodings: " . implode(', ', $supported);
```

## Related Errors

- [XML_ERROR_INCORRECT_ENCODING](xml-error-incorrect-encoding.md) - Incorrect encoding declaration
- [XML_ERROR_PARTIAL_CHAR](xml-error-partial-char.md) - Partial character sequence
- [XML_ERROR_INVALID_TOKEN](xml-error-invalid-token.md) - Invalid token in XML