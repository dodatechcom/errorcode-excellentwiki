---
title: "[Solution] PHP XML_ERROR_UNCLOSED_CDATA_SECTION — CDATA Section Not Properly Closed"
description: "Fix PHP XML_ERROR_UNCLOSED_CDATA_SECTION by closing CDATA with ]]>, checking nesting, and verifying syntax. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 20
---

# PHP XML_ERROR_UNCLOSED_CDATA_SECTION — CDATA Section Not Properly Closed

XML_ERROR_UNCLOSED_CDATA_SECTION occurs when a CDATA section is opened with `<![CDATA[` but not properly closed with `]]>`. CDATA sections allow content to contain special characters without escaping, but they must be properly closed. The closing sequence `]]>` cannot appear within the CDATA content itself.

## Common Causes

```php
// Missing closing ]]>
$xml = '<?xml version="1.0"?><root><![CDATA[Content</root>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_UNCLOSED_CDATA_SECTION
```

```php
// Unclosed CDATA in attribute
$xml = '<?xml version="1.0"?><root attr="<![CDATA[Content">Text</root>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_UNCLOSED_CDATA_SECTION
```

```php
// Nested CDATA sections
$xml = '<?xml version="1.0"?><root><![CDATA[<![CDATA[Content]]]]><![CDATA[>]]></root>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_UNCLOSED_CDATA_SECTION
```

```php
// Truncated content
$xml = '<?xml version="1.0"?><root><![CDATA[Content here';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_UNCLOSED_CDATA_SECTION
```

```php
// CDATA with ]> inside
$xml = '<?xml version="1.0"?><root><![CDATA[Content] More]]></root>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_UNCLOSED_CDATA_SECTION
```

## How to Fix

### Fix 1: Close CDATA with ]]>

Ensure every CDATA section is properly closed:

```php
// Bad: Missing closing
$xml = '<root><![CDATA[Content</root>';

// Good: Properly closed
$xml = '<root><![CDATA[Content]]></root>';
```

### Fix 2: Check Nesting

Verify CDATA sections are not nested:

```php
function validateCdataNesting($xml) {
    preg_match_all('/<!\[CDATA\[(.*?)\]\]>/s', $xml, $matches);
    
    foreach ($matches[1] as $content) {
        if (strpos($content, '<![CDATA[') !== false) {
            return false;
        }
    }
    
    return true;
}

$xml = '<?xml version="1.0"?><root><![CDATA[Content]]></root>';
if (!validateCdataNesting($xml)) {
    echo "Nested CDATA sections detected";
}
```

### Fix 3: Verify Syntax

Check CDATA syntax is correct:

```php
function validateCdataSyntax($xml) {
    $issues = [];
    
    // Find all CDATA sections
    preg_match_all('/<!\[CDATA\[(.*?)\]\]>/s', $matches);
    
    // Check for ]> inside CDATA
    foreach ($matches[1] as $content) {
        if (strpos($content, ']>') !== false) {
            $issues[] = "Invalid sequence ']'>' inside CDATA";
        }
    }
    
    return $issues;
}

$xml = '<?xml version="1.0"?><root><![CDATA[Content]]></root>';
$issues = validateCdataSyntax($xml);
print_r($issues);
```

### Fix 4: Fix CDATA Content

Remove or escape problematic content:

```php
function fixCdataContent($content) {
    // Replace ]> with escaped version
    $content = str_replace(']]>', ']]]]><![CDATA[>', $content);
    return $content;
}

$content = 'Content with ]> inside';
$fixed = fixCdataContent($content);
$xml = '<?xml version="1.0"?><root><![CDATA[' . $fixed . ']]></root>';
```

### Fix 5: Use DOM for Safe Handling

Let DOM handle CDATA sections safely:

```php
function safeCdataHandling($content) {
    $doc = new DOMDocument();
    $root = $doc->createElement('root');
    $cdata = $doc->createCDATASection($content);
    $root->appendChild($cdata);
    $doc->appendChild($root);
    
    return $doc->saveXML();
}

$content = 'Content with <special> & "characters"';
$xml = safeCdataHandling($content);
```

## Examples

```php
// Basic unclosed CDATA detection
$xml = '<?xml version="1.0"?><root><![CDATA[Content</root>';
$parser = xml_parser_create();
xml_parse($parser, $xml);
$error = xml_get_error_code($parser);
if ($error === XML_ERROR_UNCLOSED_CDATA_SECTION) {
    echo "Unclosed CDATA section detected";
}
xml_parser_free($parser);
```

```php
// Fix unclosed CDATA sections
function fixUnclosedCdata($xml) {
    // Find all CDATA sections
    preg_match_all('/<!\[CDATA\[(.*?)\]\]>/s', $xml, $matches, PREG_OFFSET_CAPTURE);
    
    // Find all opening CDATA tags
    preg_match_all('/<!\[CDATA\[/', $xml, $openMatches, PREG_OFFSET_CAPTURE);
    
    // If more opening than closing, add closing
    if (count($openMatches[0]) > count($matches[0])) {
        $xml .= ']]></root>';
    }
    
    return $xml;
}

$xml = '<?xml version="1.0"?><root><![CDATA[Content</root>';
$xml = fixUnclosedCdata($xml);
```

```php
// Validate all CDATA sections
function validateAllCdata($xml) {
    $issues = [];
    
    $openCount = substr_count($xml, '<![CDATA[');
    $closeCount = substr_count($xml, ']]>');
    
    if ($openCount !== $closeCount) {
        $issues[] = "Mismatched CDATA tags: $openCount opens, $closeCount closes";
    }
    
    // Check for ]> inside CDATA
    preg_match_all('/<!\[CDATA\[(.*?)\]\]>/s', $xml, $matches);
    foreach ($matches[1] as $content) {
        if (strpos($content, ']>') !== false) {
            $issues[] = "Invalid sequence inside CDATA";
        }
    }
    
    return $issues;
}

$xml = '<?xml version="1.0"?><root><![CDATA[Content]]></root>';
$issues = validateAllCdata($xml);
print_r($issues);
```

```php
// Safe CDATA creation
function createSafeCdata($content) {
    // Escape any ]> sequences
    $content = str_replace(']]>', ']]]]><![CDATA[>', $content);
    
    return '<![CDATA[' . $content . ']]>';
}

$content = 'Content with ]> inside';
$cdata = createSafeCdata($content);
$xml = '<?xml version="1.0"?><root>' . $cdata . '</root>';
```

## Related Errors

- [XML_ERROR_SYNTAX](xml-error-syntax.md) - XML syntax error
- [XML_ERROR_UNCLOSED_TOKEN](xml-error-unclosed-token.md) - Token not properly closed
- [XML_ERROR_INVALID_TOKEN](xml-error-invalid-token.md) - Invalid token in XML