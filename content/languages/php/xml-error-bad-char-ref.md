---
title: "[Solution] PHP XML_ERROR_BAD_CHAR_REF — Bad Character Reference"
description: "Fix PHP XML_ERROR_BAD_CHAR_REF by using valid character references, checking numeric codes, and verifying hex/decimal syntax. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 14
---

# PHP XML_ERROR_BAD_CHAR_REF — Bad Character Reference

XML_ERROR_BAD_CHAR_REF occurs when the XML parser encounters an invalid character reference. Character references can be numeric (decimal or hexadecimal) or named, but must follow strict syntax rules. Invalid references include malformed numeric codes, invalid named references, or references to prohibited characters.

## Common Causes

```php
// Invalid hex reference
$xml = '<?xml version="1.0"?><root>&#xGGG;</root>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_BAD_CHAR_REF
```

```php
// Invalid decimal reference
$xml = '<?xml version="1.0"?><root>&#9999999;</root>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_BAD_CHAR_REF
```

```php
// Missing semicolon
$xml = '<?xml version="1.0"?><root>&#x41</root>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_BAD_CHAR_REF
```

```php
// Reference to prohibited character
$xml = '<?xml version="1.0"?><root>&#x0;</root>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_BAD_CHAR_REF
```

```php
// Invalid named reference
$xml = '<?xml version="1.0"?><root>&invalid;</root>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_BAD_CHAR_REF
```

## How to Fix

### Fix 1: Use Valid Character References

Ensure character references follow correct syntax:

```php
// Valid hex reference
$xml = '<?xml version="1.0"?><root>&#x41;</root>'; // A

// Valid decimal reference
$xml = '<?xml version="1.0"?><root>&#65;</root>'; // A

// Valid named reference
$xml = '<?xml version="1.0"?><root>&amp;</root>'; // &
```

### Fix 2: Check Numeric Codes

Validate numeric character references:

```php
function validateCharacterRef($ref) {
    // Check hex reference
    if (preg_match('/&#x([0-9A-Fa-f]+);/', $ref, $matches)) {
        $code = hexdec($matches[1]);
        return $code >= 1 && $code <= 0xD7FF ||
               ($code >= 0xE000 && $code <= 0xFFFD) ||
               ($code >= 0x10000 && $code <= 0x10FFFF);
    }
    
    // Check decimal reference
    if (preg_match('/&#(\d+);/', $ref, $matches)) {
        $code = intval($matches[1]);
        return $code >= 1 && $code <= 0xD7FF ||
               ($code >= 0xE000 && $code <= 0xFFFD) ||
               ($code >= 0x10000 && $code <= 0x10FFFF);
    }
    
    return false;
}

$refs = ['&#x41;', '&#65;', '&#x0;', '&#9999999;'];
foreach ($refs as $ref) {
    echo "$ref: " . (validateCharacterRef($ref) ? "Valid" : "Invalid") . "\n";
}
```

### Fix 3: Verify Hex/Decimal Syntax

Check that references use proper syntax:

```php
function fixCharacterRefSyntax($xml) {
    // Fix missing semicolons
    $xml = preg_replace('/&#x([0-9A-Fa-f]+)([^;])/', '&#x$1;$2', $xml);
    $xml = preg_replace('/&#(\d+)([^;])/', '&#$1;$2', $xml);
    
    // Fix invalid hex characters
    $xml = preg_replace('/&#x([^0-9A-Fa-f]+);/', '', $xml);
    
    return $xml;
}

$xml = '<?xml version="1.0"?><root>&#x41&#x42</root>';
$xml = fixCharacterRefSyntax($xml);
```

### Fix 4: Use Named References

Replace numeric references with named references where possible:

```php
function useNamedReferences($xml) {
    $namedRefs = [
        '&#38;' => '&amp;',
        '&#60;' => '&lt;',
        '&#62;' => '&gt;',
        '&#34;' => '&quot;',
        '&#39;' => '&apos;'
    ];
    
    return str_replace(array_keys($namedRefs), array_values($namedRefs), $xml);
}

$xml = '<?xml version="1.0"?><root>&#38;</root>';
$xml = useNamedReferences($xml);
```

### Fix 5: Validate All References

Check all character references in the document:

```php
function findAllCharacterRefs($xml) {
    $refs = [];
    
    // Find hex references
    preg_match_all('/&#x([0-9A-Fa-f]+);/', $xml, $hexRefs);
    foreach ($hexRefs[1] as $hex) {
        $refs[] = ['type' => 'hex', 'value' => $hex, 'code' => hexdec($hex)];
    }
    
    // Find decimal references
    preg_match_all('/&#(\d+);/', $xml, $decRefs);
    foreach ($decRefs[1] as $dec) {
        $refs[] = ['type' => 'decimal', 'value' => $dec, 'code' => intval($dec)];
    }
    
    return $refs;
}

$xml = '<?xml version="1.0"?><root>&#x41; &#65; &#x0;</root>';
$refs = findAllCharacterRefs($xml);
print_r($refs);
```

## Examples

```php
// Basic bad character reference detection
$xml = '<?xml version="1.0"?><root>&#xGGG;</root>';
$parser = xml_parser_create();
xml_parse($parser, $xml);
$error = xml_get_error_code($parser);
if ($error === XML_ERROR_BAD_CHAR_REF) {
    echo "Bad character reference found";
}
xml_parser_free($parser);
```

```php
// Fix all bad character references
function fixAllBadRefs($xml) {
    // Remove invalid hex references
    $xml = preg_replace('/&#x[^0-9A-Fa-f]+;/', '', $xml);
    
    // Remove references to invalid code points
    $xml = preg_replace('/&#x0;/', '', $xml);
    $xml = preg_replace('/&#0;/', '', $xml);
    
    // Fix references > 0x10FFFF
    $xml = preg_replace('/&#x[0-9A-Fa-f]{6,};/', '', $xml);
    
    return $xml;
}

$xml = '<?xml version="1.0"?><root>&#xGGG; &#x0; &#xFFFFFFFF;</root>';
$xml = fixAllBadRefs($xml);
```

```php
// Comprehensive reference validator
function validateAllCharacterRefs($xml) {
    $issues = [];
    
    // Find all character references
    preg_match_all('/&#x([0-9A-Fa-f]*);|&#(\d*);/', $xml, $matches, PREG_SET_ORDER);
    
    foreach ($matches as $match) {
        if (isset($match[1]) && $match[1] !== '') {
            // Hex reference
            $code = hexdec($match[1]);
            if ($code < 1 || ($code > 0xD7FF && $code < 0xE000)) {
                $issues[] = "Invalid hex reference: " . $match[0];
            }
        } elseif (isset($match[2]) && $match[2] !== '') {
            // Decimal reference
            $code = intval($match[2]);
            if ($code < 1 || ($code > 0xD7FF && $code < 0xE000)) {
                $issues[] = "Invalid decimal reference: " . $match[0];
            }
        }
    }
    
    return $issues;
}

$xml = '<?xml version="1.0"?><root>&#x0; &#xGGG;</root>';
$issues = validateAllCharacterRefs($xml);
print_r($issues);
```

## Related Errors

- [XML_ERROR_INVALID_TOKEN](xml-error-invalid-token.md) - Invalid token in XML
- [XML_ERROR_UNDEFINED_ENTITY](xml-error-undefined-entity.md) - Undefined entity reference
- [XML_ERROR_BINARY_ENTITY_REF](xml-error-binary-entity-ref.md) - Binary entity reference