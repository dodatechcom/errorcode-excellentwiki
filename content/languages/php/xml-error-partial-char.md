---
title: "[Solution] PHP XML_ERROR_PARTIAL_CHAR — Partial Character Sequence"
description: "Fix PHP XML_ERROR_PARTIAL_CHAR by checking UTF-8 encoding, validating character boundaries, and using proper encoding. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 6
---

# PHP XML_ERROR_PARTIAL_CHAR — Partial Character Sequence

XML_ERROR_PARTIAL_CHAR occurs when the XML parser encounters an incomplete character sequence. This typically happens when a multi-byte UTF-8 character is truncated due to improper chunking, encoding mismatches, or binary data corruption. UTF-8 characters can be 1-4 bytes long.

## Common Causes

```php
// Splitting XML in the middle of a multi-byte character
$xml = '<?xml version="1.0" encoding="UTF-8"?><root>Ü</root>';
// Split at byte 10 (in the middle of Ü)
$chunk1 = substr($xml, 0, 10);
$chunk2 = substr($xml, 10);
$parser = xml_parser_create('UTF-8');
xml_parse($parser, $chunk1);
xml_parse($parser, $chunk2); // XML_ERROR_PARTIAL_CHAR
```

```php
// Reading partial file content
$fp = fopen('document.xml', 'r');
$chunk = fread($fp, 100); // May cut in middle of character
$parser = xml_parser_create('UTF-8');
xml_parse($parser, $chunk); // XML_ERROR_PARTIAL_CHAR
```

```php
// Encoding mismatch
$xml = '<?xml version="1.0" encoding="UTF-8"?><root>À</root>';
// File actually contains Latin-1 encoded content
$parser = xml_parser_create('UTF-8');
xml_parse($parser, $xml); // XML_ERROR_PARTIAL_CHAR
```

```php
// Binary data corruption
$xml = '<?xml version="1.0"?><root>' . chr(0xC3) . '</root>';
// Missing second byte of UTF-8 sequence
$parser = xml_parser_create('UTF-8');
xml_parse($parser, $xml); // XML_ERROR_PARTIAL_CHAR
```

```php
// Truncated download or network issue
$xml = file_get_contents('http://example.com/data.xml');
if ($xml === false || strlen($xml) < 10) {
    // Possible truncation
}
```

## How to Fix

### Fix 1: Check UTF-8 Encoding

Validate that the input is valid UTF-8:

```php
function isValidUtf8($string) {
    return mb_check_encoding($string, 'UTF-8');
}

$xml = file_get_contents('document.xml');
if (!isValidUtf8($xml)) {
    $xml = mb_convert_encoding($xml, 'UTF-8', 'auto');
}
```

### Fix 2: Validate Character Boundaries

When chunking, ensure you don't split multi-byte characters:

```php
function safeChunk($string, $chunkSize) {
    $chunks = [];
    $length = strlen($string);
    $position = 0;
    
    while ($position < $length) {
        $chunk = substr($string, $position, $chunkSize);
        
        // Check if we're in the middle of a UTF-8 character
        $lastByte = ord(substr($chunk, -1));
        while (($lastByte & 0x80) && !($lastByte & 0x40)) {
            $chunk = substr($chunk, 0, -1);
            $position--;
            if (empty($chunk)) {
                break;
            }
            $lastByte = ord(substr($chunk, -1));
        }
        
        $chunks[] = $chunk;
        $position += strlen($chunk);
    }
    
    return $chunks;
}
```

### Fix 3: Use Proper Encoding Declaration

Match encoding declaration with actual content:

```php
// If file is UTF-8, declare it
$xml = '<?xml version="1.0" encoding="UTF-8"?>' . 
       substr($xml, strpos($xml, '?>') + 2);
```

### Fix 4: Handle Partial Reads

Accumulate partial reads until complete:

```php
function readCompleteXml($filename) {
    $fp = fopen($filename, 'r');
    $xml = '';
    
    while (!feof($fp)) {
        $chunk = fread($fp, 8192);
        if ($chunk === false) {
            break;
        }
        $xml .= $chunk;
        
        // Verify we have complete content
        if (!mb_check_encoding($xml, 'UTF-8')) {
            continue; // Read more to complete the character
        }
    }
    
    fclose($fp);
    return $xml;
}
```

### Fix 5: Convert Encoding

Convert from other encodings to UTF-8:

```php
function convertToUtf8($xml) {
    // Try to detect encoding
    $encoding = mb_detect_encoding($xml, ['UTF-8', 'ISO-8859-1', 'Windows-1252']);
    
    if ($encoding !== 'UTF-8') {
        $xml = mb_convert_encoding($xml, 'UTF-8', $encoding);
    }
    
    return $xml;
}
```

## Examples

```php
// Basic partial character detection
$xml = '<?xml version="1.0" encoding="UTF-8"?><root>Ü</root>';
$parser = xml_parser_create('UTF-8');
xml_parse($parser, $xml);
$error = xml_get_error_code($parser);
if ($error === XML_ERROR_PARTIAL_CHAR) {
    echo "Partial character detected";
}
xml_parser_free($parser);
```

```php
// Safe chunked parsing
function safeChunkedParse($xml, $chunkSize = 8192) {
    $parser = xml_parser_create('UTF-8');
    $chunks = safeChunk($xml, $chunkSize);
    
    foreach ($chunks as $index => $chunk) {
        $isLast = ($index === count($chunks) - 1);
        $result = xml_parse($parser, $chunk, $isLast);
        
        if (!$result) {
            $error = xml_get_error_code($parser);
            if ($error === XML_ERROR_PARTIAL_CHAR) {
                // Reassemble and try with smaller chunks
                return safeChunkedParse($xml, $chunkSize / 2);
            }
        }
    }
    
    xml_parser_free($parser);
    return true;
}
```

```php
// Fix partial character issues
function fixPartialCharacters($xml) {
    // Remove invalid byte sequences
    $xml = preg_replace('/[\x80-\xBF]+/', '', $xml);
    
    // Ensure valid UTF-8
    $xml = mb_convert_encoding($xml, 'UTF-8', 'UTF-8');
    
    return $xml;
}

$xml = '<?xml version="1.0" encoding="UTF-8"?><root>Content</root>';
$xml = fixPartialCharacters($xml);
```

```php
// Validate complete UTF-8 sequences
function validateUtf8Sequences($xml) {
    // Check for orphaned bytes
    $pattern = '/[\xC0-\xDF][^\x80-\xBF]|[\xE0-\xEF][^\x80-\xBF]{2}|[\xF0-\xF7][^\x80-\xBF]{3}/';
    
    if (preg_match($pattern, $xml)) {
        return false;
    }
    
    return true;
}
```

## Related Errors

- [XML_ERROR_UNKNOWN_ENCODING](xml-error-unknown-encoding.md) - Unknown character encoding
- [XML_ERROR_INCORRECT_ENCODING](xml-error-incorrect-encoding.md) - Incorrect encoding declaration
- [XML_ERROR_INVALID_TOKEN](xml-error-invalid-token.md) - Invalid token in XML