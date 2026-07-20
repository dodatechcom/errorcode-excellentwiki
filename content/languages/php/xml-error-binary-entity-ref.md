---
title: "[Solution] PHP XML_ERROR_BINARY_ENTITY_REF — Binary Entity Reference"
description: "Fix PHP XML_ERROR_BINARY_ENTITY_REF by using text entities, avoiding binary data, and encoding properly. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 15
---

# PHP XML_ERROR_BINARY_ENTITY_REF — Binary Entity Reference

XML_ERROR_BINARY_ENTITY_REF occurs when the XML parser encounters a reference to a binary entity. XML is a text-based format and does not support binary data directly. Binary entities cannot be referenced in XML content and must be encoded using base64 or other text-based encoding methods.

## Common Causes

```php
// Binary data in entity
$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY binarydata "' . chr(0) . chr(1) . chr(2) . '">
]>
<root>&binarydata;</root>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_BINARY_ENTITY_REF
```

```php
// Image data in entity
$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY image "' . base64_decode('iVBORw0KGgoAAAANSUhEUg==') . '">
]>
<root>&image;</root>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_BINARY_ENTITY_REF
```

```php
// File content with binary
$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY filedata "' . file_get_contents('binary.dat') . '">
]>
<root>&filedata;</root>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_BINARY_ENTITY_REF
```

```php
// Null bytes in entity value
$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY binary "Content' . chr(0) . 'More">
]>
<root>&binary;</root>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_BINARY_ENTITY_REF
```

```php
// Encoded binary without proper encoding
$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY data "0x89PNG...">
]>
<root>&data;</root>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_BINARY_ENTITY_REF
```

## How to Fix

### Fix 1: Use Text Entities

Convert binary data to text-based format:

```php
// Bad: Binary data
$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY binary "' . chr(0) . chr(1) . '">
]>
<root>&binary;</root>';

// Good: Base64 encoded
$binaryData = chr(0) . chr(1);
$encoded = base64_encode($binaryData);
$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY binary "' . $encoded . '">
]>
<root>&binary;</root>';
```

### Fix 2: Avoid Binary Data in XML

Store binary data separately and reference it:

```php
// Store binary data in file
$binaryData = file_get_contents('image.png');
file_put_contents('image.base64', base64_encode($binaryData));

// Reference in XML
$xml = '<?xml version="1.0"?>
<root>
    <image ref="image.base64"/>
</root>';
```

### Fix 3: Encode Properly

Use proper encoding for all content:

```php
function encodeForXml($binaryData) {
    // Base64 encode
    $encoded = base64_encode($binaryData);
    
    // Verify no binary characters remain
    if (preg_match('/[\x00-\x08\x0B\x0C\x0E-\x1F]/', $encoded)) {
        return false;
    }
    
    return $encoded;
}

$binaryData = file_get_contents('data.bin');
$encoded = encodeForXml($binaryData);
if ($encoded) {
    $xml = '<?xml version="1.0"?>
<root><data>' . $encoded . '</data></root>';
}
```

### Fix 4: Use CDATA for Special Content

Wrap problematic content in CDATA sections:

```php
$content = 'Content with special chars';
$xml = '<?xml version="1.0"?><root><![CDATA[' . $content . ']]></root>';
```

### Fix 5: Validate Binary Content

Check for binary data before creating entities:

```php
function containsBinaryData($data) {
    return preg_match('/[\x00-\x08\x0B\x0C\x0E-\x1F]/', $data);
}

$content = file_get_contents('file.txt');
if (containsBinaryData($content)) {
    $content = base64_encode($content);
}
```

## Examples

```php
// Basic binary entity reference detection
$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY binary "' . chr(0) . '">
]>
<root>&binary;</root>';
$parser = xml_parser_create();
xml_parse($parser, $xml);
$error = xml_get_error_code($parser);
if ($error === XML_ERROR_BINARY_ENTITY_REF) {
    echo "Binary entity reference found";
}
xml_parser_free($parser);
```

```php
// Safe binary data handling
function handleBinaryData($data, $name) {
    if (containsBinaryData($data)) {
        // Encode to base64
        $encoded = base64_encode($data);
        
        // Create entity with encoded data
        $entity = '<!ENTITY ' . $name . ' "' . $encoded . '">';
        
        return $entity;
    }
    
    return '<!ENTITY ' . $name . ' "' . htmlspecialchars($data) . '">';
}

$binaryData = chr(0) . chr(1) . chr(2);
$entity = handleBinaryData($binaryData, 'data');
$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    ' . $entity . '
]>
<root>&data;</root>';
```

```php
// Fix binary entities in XML
function fixBinaryEntities($xml) {
    preg_match_all('/<!ENTITY\s+(\w+)\s+"([^"]*)">/', $xml, $matches);
    
    foreach ($matches[1] as $index => $name) {
        $value = $matches[2][$index];
        
        if (containsBinaryData($value)) {
            $encoded = base64_encode($value);
            $newEntity = '<!ENTITY ' . $name . ' "' . $encoded . '">';
            $xml = str_replace($matches[0][$index], $newEntity, $xml);
        }
    }
    
    return $xml;
}

$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY binary "' . chr(0) . '">
]>
<root>&binary;</root>';

$xml = fixBinaryEntities($xml);
```

```php
// Validate no binary in entities
function validateNoBinaryEntities($xml) {
    preg_match_all('/<!ENTITY\s+(\w+)\s+"([^"]*)">/', $xml, $matches);
    
    foreach ($matches[2] as $value) {
        if (containsBinaryData($value)) {
            return false;
        }
    }
    
    return true;
}

$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY text "safe content">
]>
<root>&text;</root>';

if (validateNoBinaryEntities($xml)) {
    echo "No binary entities found";
}
```

## Related Errors

- [XML_ERROR_INVALID_TOKEN](xml-error-invalid-token.md) - Invalid token in XML
- [XML_ERROR_BAD_CHAR_REF](xml-error-bad-char-ref.md) - Bad character reference
- [XML_ERROR_ATTRIBUTE_EXTERNAL_ENTITY_REF](xml-error-attribute-external-entity-ref.md) - External entity in attribute