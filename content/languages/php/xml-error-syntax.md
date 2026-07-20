---
title: "[Solution] PHP XML_ERROR_SYNTAX — XML Syntax Error"
description: "Fix PHP XML_ERROR_SYNTAX by validating XML structure, checking for typos, and using XML validators. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 2
---

# PHP XML_ERROR_SYNTAX — XML Syntax Error

XML_ERROR_SYNTAX indicates a syntax error in the XML document. This is one of the most common XML parsing errors and can occur due to malformed tags, missing closing tags, incorrect attribute syntax, or other structural issues. The parser cannot process the XML until the syntax is corrected.

## Common Causes

```php
// Missing closing tag
$xml = '<?xml version="1.0"?><root><child>Content</root>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_SYNTAX
```

```php
// Incorrect attribute syntax
$xml = '<?xml version="1.0"?><root attr=value>Content</root>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_SYNTAX
```

```php
// Missing quotes around attribute values
$xml = '<?xml version="1.0"?><root attr=value>Content</root>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_SYNTAX
```

```php
// Nested XML declaration
$xml = '<?xml version="1.0"?><?xml version="1.1"?><root/>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_SYNTAX
```

```php
// Invalid character in tag name
$xml = '<?xml version="1.0"?><root-tag>Content</root-tag>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_SYNTAX
```

## How to Fix

### Fix 1: Validate XML Structure

Use XML validation to identify syntax errors:

```php
$xml = '<?xml version="1.0"?><root><child>Content</child></root>';
$doc = new DOMDocument();
if (!$doc->loadXML($xml)) {
    echo "XML syntax error found";
}
```

### Fix 2: Check for Typos in Tags

Review all opening and closing tags for typos:

```php
$xml = '<?xml version="1.0"?><root><child>Content</child></root>';
$parser = xml_parser_create();
xml_parse($parser, $xml);
if (xml_get_error_code($parser) === XML_ERROR_SYNTAX) {
    echo "Line: " . xml_get_current_line_number($parser);
    echo "Column: " . xml_get_current_column_number($parser);
}
xml_parser_free($parser);
```

### Fix 3: Use XML Lint for Validation

Use PHP's DOM extension for comprehensive validation:

```php
function validateXml($xml) {
    libxml_use_internal_errors(true);
    $doc = new DOMDocument();
    $result = $doc->loadXML($xml);
    $errors = libxml_get_errors();
    libxml_clear_errors();
    return ['valid' => $result, 'errors' => $errors];
}
```

### Fix 4: Fix Attribute Syntax

Ensure all attributes have proper quotes:

```php
// Bad: <root attr=value>
// Good: <root attr="value">
$xml = '<?xml version="1.0"?><root attr="value">Content</root>';
```

### Fix 5: Remove Duplicate XML Declarations

Ensure only one XML declaration exists:

```php
// Remove any extra XML declarations
$xml = preg_replace('/<\?xml[^?]*\?>/', '', $xml, -1, $count);
if ($count > 1) {
    $xml = '<?xml version="1.0"?>' . preg_replace('/<\?xml[^?]*\?>/', '', $xml);
}
```

## Examples

```php
// Basic syntax error detection
$xml = '<?xml version="1.0"?><root><child>Content</child></root>';
$parser = xml_parser_create();
xml_parse($parser, $xml);
$error = xml_get_error_code($parser);
if ($error === XML_ERROR_SYNTAX) {
    echo "Syntax error at line " . xml_get_current_line_number($parser);
    echo " column " . xml_get_current_column_number($parser);
}
xml_parser_free($parser);
```

```php
// Common syntax fixes
function fixCommonSyntaxErrors($xml) {
    // Fix missing quotes on attributes
    $xml = preg_replace('/(\w+)=([^\s"<>]+)/', '$1="$2"', $xml);
    
    // Fix unclosed tags (basic fix)
    if (substr_count($xml, '<root>') > substr_count($xml, '</root>')) {
        $xml .= '</root>';
    }
    return $xml;
}
```

```php
// Comprehensive XML validation
function validateXmlDocument($xml) {
    $errors = [];
    
    // Check for XML declaration
    if (strpos($xml, '<?xml') === false) {
        $errors[] = "Missing XML declaration";
    }
    
    // Check for root element
    if (preg_match('/<(\w+)/', $xml, $matches)) {
        $rootTag = $matches[1];
        if (strpos($xml, "</$rootTag>") === false) {
            $errors[] = "Missing closing tag for root element: $rootTag";
        }
    }
    
    return $errors;
}
```

```php
// Using SimpleXML for validation
$xml = '<?xml version="1.0"?><root><child>Content</child></root>';
libxml_use_internal_errors(true);
$result = simplexml_load_string($xml);
if ($result === false) {
    foreach (libxml_get_errors() as $error) {
        echo "Error: " . trim($error->message) . "\n";
    }
    libxml_clear_errors();
}
```

## Related Errors

- [XML_ERROR_NO_ELEMENTS](xml-error-no-elements.md) - No elements found in XML
- [XML_ERROR_INVALID_TOKEN](xml-error-invalid-token.md) - Invalid token in XML
- [XML_ERROR_TAG_MISMATCH](xml-error-tag-mismatch.md) - Opening and closing tags don't match