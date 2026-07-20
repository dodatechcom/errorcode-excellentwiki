---
title: "[Solution] PHP XML_ERROR_NO_MEMORY — Parser Out of Memory"
description: "Fix PHP XML_ERROR_NO_MEMORY by increasing memory_limit, freeing memory, and simplifying XML. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 1
---

# PHP XML_ERROR_NO_MEMORY — Parser Out of Memory

XML_ERROR_NO_MEMORY occurs when the XML parser runs out of memory during parsing. This typically happens when processing very large XML documents or when the PHP memory limit is too low for the parser's requirements. The parser needs memory for both the input string and internal data structures.

## Common Causes

```php
// Insufficient memory_limit for large XML
$xml = file_get_contents('huge_file.xml'); // Large file
$parser = xml_parser_create();
xml_parse($parser, $xml); // May fail with XML_ERROR_NO_MEMORY
```

```php
// Memory leak from not freeing parser
for ($i = 0; $i < 1000; $i++) {
    $parser = xml_parser_create();
    xml_parse($parser, $xml);
    // Missing xml_parser_free() causes memory accumulation
}
```

```php
// Extremely complex nested XML structure
$xml = str_repeat('<level>', 10000) . 'content' . str_repeat('</level>', 10000);
$parser = xml_parser_create();
xml_parse($parser, $xml); // Deep nesting exhausts memory
```

```php
// Loading entire file into memory at once
$xml = file_get_contents('large_document.xml');
$parser = xml_parser_create();
xml_parse($parser, $xml);
```

```php
// XML with many entities or attributes
$xml = '<?xml version="1.0"?><root>' . str_repeat('<item attr="' . str_repeat('x', 1000) . '"/>', 100000) . '</root>';
```

## How to Fix

### Fix 1: Increase Memory Limit

Increase PHP's memory limit before parsing:

```php
ini_set('memory_limit', '512M');
$xml = file_get_contents('large_file.xml');
$parser = xml_parser_create();
xml_parse($parser, $xml);
xml_parser_free($parser);
```

### Fix 2: Free Parser After Each Use

Always free the parser to prevent memory leaks:

```php
foreach ($xmlDocuments as $xml) {
    $parser = xml_parser_create();
    xml_parse($parser, $xml);
    xml_parser_free($parser); // Critical for memory management
}
```

### Fix 3: Use Streaming Parser for Large Files

Process XML in chunks instead of loading the entire document:

```php
$parser = xml_parser_create();
$fp = fopen('large_file.xml', 'r');
while ($data = fread($fp, 8192)) {
    xml_parse($parser, $data, feof($fp));
}
fclose($fp);
xml_parser_free($parser);
```

### Fix 4: Simplify XML Structure

Reduce complexity by flattening deeply nested structures:

```php
// Instead of deeply nested XML, use flat structure
$xml = '<?xml version="1.0"?><items>';
for ($i = 0; $i < 1000; $i++) {
    $xml .= "<item id='$i'>$i</item>";
}
$xml .= '</items>';
```

### Fix 5: Optimize Memory Usage

Clear unused variables and use unset strategically:

```php
$xml = file_get_contents('document.xml');
$parser = xml_parser_create();
xml_parse($parser, $xml);
unset($xml); // Free the XML string from memory
xml_parser_free($parser);
```

## Examples

```php
// Basic memory error handling
$parser = xml_parser_create();
xml_parse($parser, $xml);
$error = xml_get_error_code($parser);
if ($error === XML_ERROR_NO_MEMORY) {
    echo "Out of memory. Current limit: " . ini_get('memory_limit');
}
xml_parser_free($parser);
```

```php
// Memory-safe parsing with chunking
function safeXmlParse($filename, $chunkSize = 8192) {
    $parser = xml_parser_create();
    $fp = fopen($filename, 'r');
    if (!$fp) {
        return false;
    }
    while ($data = fread($fp, $chunkSize)) {
        $result = xml_parse($parser, $data, feof($fp));
        if (!$result) {
            $error = xml_get_error_code($parser);
            if ($error === XML_ERROR_NO_MEMORY) {
                fclose($fp);
                xml_parser_free($parser);
                return false;
            }
        }
    }
    fclose($fp);
    xml_parser_free($parser);
    return true;
}
```

```php
// Memory monitoring during parsing
$memBefore = memory_get_usage();
$parser = xml_parser_create();
xml_parse($parser, $xml);
$memAfter = memory_get_usage();
$xmlError = xml_get_error_code($parser);
xml_parser_free($parser);

if ($xmlError === XML_ERROR_NO_MEMORY) {
    echo "Memory exhausted. Used: " . ($memAfter - $memBefore) . " bytes\n";
    echo "Peak usage: " . memory_get_peak_usage() . " bytes\n";
}
```

## Related Errors

- [XML_ERROR_SYNTAX](xml-error-syntax.md) - XML syntax error
- [XML_ERROR_NO_ELEMENTS](xml-error-no-elements.md) - No elements found in XML
- [XML_ERROR_UNCLOSED_TOKEN](xml-error-unclosed-token.md) - Token not properly closed