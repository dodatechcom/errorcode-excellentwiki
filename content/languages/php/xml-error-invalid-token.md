---
title: "[Solution] PHP XML_ERROR_INVALID_TOKEN — Invalid Token in XML"
description: "Fix PHP XML_ERROR_INVALID_TOKEN by escaping special characters, checking encoding, and validating XML content. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 4
---

# PHP XML_ERROR_INVALID_TOKEN — Invalid Token in XML

XML_ERROR_INVALID_TOKEN occurs when the XML parser encounters an invalid character or token in the document. This can happen with special characters that aren't properly escaped, binary data, or encoding issues that produce invalid byte sequences.

## Common Causes

```php
// Unescaped ampersand
$xml = '<?xml version="1.0"?><root>A & B</root>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_INVALID_TOKEN
```

```php
// Unescaped less-than or greater-than signs
$xml = '<?xml version="1.0"?><root>If x < 5 then</root>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_INVALID_TOKEN
```

```php
// Binary data in XML
$xml = '<?xml version="1.0"?><root>' . chr(0) . 'content' . chr(0) . '</root>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_INVALID_TOKEN
```

```php
// Invalid UTF-8 sequences
$xml = '<?xml version="1.0" encoding="UTF-8"?><root>' . chr(0xFF) . '</root>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_INVALID_TOKEN
```

```php
// Null bytes in content
$xml = '<?xml version="1.0"?><root>Content' . chr(0) . 'More</root>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_INVALID_TOKEN
```

## How to Fix

### Fix 1: Escape Special Characters

Properly escape all special XML characters:

```php
function escapeXmlContent($content) {
    $content = str_replace('&', '&amp;', $content);
    $content = str_replace('<', '&lt;', $content);
    $content = str_replace('>', '&gt;', $content);
    $content = str_replace("'", '&apos;', $content);
    $content = str_replace('"', '&quot;', $content);
    return $content;
}
```

### Fix 2: Check Encoding

Verify and fix encoding issues:

```php
function cleanXmlEncoding($xml) {
    // Remove null bytes
    $xml = str_replace(chr(0), '', $xml);
    
    // Ensure valid UTF-8
    if (!mb_check_encoding($xml, 'UTF-8')) {
        $xml = mb_convert_encoding($xml, 'UTF-8', 'ASCII');
    }
    
    return $xml;
}
```

### Fix 3: Validate XML Content

Check for invalid characters before parsing:

```php
function containsInvalidXmlChars($xml) {
    // Check for invalid characters (0x00-0x08, 0x0B-0x0C, 0x0E-0x1F)
    $pattern = '/[\x00-\x08\x0B\x0C\x0E-\x1F]/';
    return preg_match($pattern, $xml);
}

$xml = 'Your XML content';
if (containsInvalidXmlChars($xml)) {
    echo "XML contains invalid characters";
}
```

### Fix 4: Use CDATA for Special Content

Wrap content with special characters in CDATA sections:

```php
$content = 'If x < 5 then y > 10';
$xml = '<?xml version="1.0"?><root><data><![CDATA[' . $content . ']]></data></root>';
```

### Fix 5: Sanitize Input

Remove or replace problematic characters:

```php
function sanitizeForXml($input) {
    // Remove control characters except tab, newline, carriage return
    $input = preg_replace('/[\x00-\x08\x0B\x0C\x0E-\x1F]/', '', $input);
    
    // Encode ampersands
    $input = str_replace('&', '&amp;', $input);
    
    return $input;
}
```

## Examples

```php
// Basic invalid token detection
$xml = '<?xml version="1.0"?><root>A & B</root>';
$parser = xml_parser_create();
xml_parse($parser, $xml);
$error = xml_get_error_code($parser);
if ($error === XML_ERROR_INVALID_TOKEN) {
    echo "Invalid token at line " . xml_get_current_line_number($parser);
}
xml_parser_free($parser);
```

```php
// Comprehensive token validation
function validateXmlTokens($xml) {
    $invalidPatterns = [
        '/&(?!amp;|lt;|gt;|quot;|apos;|#\d+;|#x[0-9A-Fa-f]+;)/' => 'Unescaped ampersand',
        '/</' => 'Unescaped less-than',
        '/>/' => 'Unescaped greater-than',
        '/[\x00-\x08\x0B\x0C\x0E-\x1F]/' => 'Invalid control character'
    ];
    
    $errors = [];
    foreach ($invalidPatterns as $pattern => $message) {
        if (preg_match($pattern, $xml)) {
            $errors[] = $message;
        }
    }
    return $errors;
}
```

```php
// Fix common invalid tokens
function fixInvalidTokens($xml) {
    // Escape ampersands that aren't already escaped
    $xml = preg_replace('/&(?!amp;|lt;|gt;|quot;|apos;|#\d+;|#x[0-9A-Fa-f]+;)/', '&amp;', $xml);
    
    // Remove invalid control characters
    $xml = preg_replace('/[\x00-\x08\x0B\x0C\x0E-\x1F]/', '', $xml);
    
    return $xml;
}
```

```php
// Validate after fixing
$xml = '<?xml version="1.0"?><root>A & B</root>';
$xml = fixInvalidTokens($xml);
$parser = xml_parser_create();
xml_parse($parser, $xml);
if (xml_get_error_code($parser) === XML_ERROR_NONE) {
    echo "XML is now valid";
}
xml_parser_free($parser);
```

## Related Errors

- [XML_ERROR_SYNTAX](xml-error-syntax.md) - XML syntax error
- [XML_ERROR_BAD_CHAR_REF](xml-error-bad-char-ref.md) - Bad character reference
- [XML_ERROR_INCORRECT_ENCODING](xml-error-incorrect-encoding.md) - Incorrect encoding declaration