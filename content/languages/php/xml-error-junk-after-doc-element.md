---
title: "[Solution] PHP XML_ERROR_JUNK_AFTER_DOC_ELEMENT — Content After Root Element"
description: "Fix PHP XML_ERROR_JUNK_AFTER_DOC_ELEMENT by moving content inside root, checking document structure, and removing extra content. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 9
---

# PHP XML_ERROR_JUNK_AFTER_DOC_ELEMENT — Content After Root Element

XML_ERROR_JUNK_AFTER_DOC_ELEMENT occurs when there is content, processing instructions, or comments after the closing tag of the root element. A valid XML document must have exactly one root element, and all content must be contained within it.

## Common Causes

```php
// Extra content after root element
$xml = '<?xml version="1.0"?><root>Content</root>Extra';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_JUNK_AFTER_DOC_ELEMENT
```

```php
// Multiple root elements
$xml = '<?xml version="1.0"?><root1>Content</root1><root2>More</root2>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_JUNK_AFTER_DOC_ELEMENT
```

```php
// Processing instruction after root
$xml = '<?xml version="1.0"?><root>Content</root><?php echo "test"; ?>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_JUNK_AFTER_DOC_ELEMENT
```

```php
// Comment after root
$xml = '<?xml version="1.0"?><root>Content</root><!-- comment -->';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_JUNK_AFTER_DOC_ELEMENT
```

```php
// Whitespace after root (in some parsers)
$xml = '<?xml version="1.0"?>   <root>Content</root>   ';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_JUNK_AFTER_DOC_ELEMENT
```

## How to Fix

### Fix 1: Move Content Inside Root

Ensure all content is within the root element:

```php
// Bad: Content outside root
$xml = '<root>Content</root>Extra';

// Good: All content inside root
$xml = '<root>ContentExtra</root>';
```

### Fix 2: Check Document Structure

Validate that only one root element exists:

```php
function validateSingleRoot($xml) {
    preg_match_all('/<(\w+)[^>]*>/', $xml, $matches);
    $rootTags = array_unique($matches[1]);
    
    return count($rootTags) <= 1;
}

$xml = '<?xml version="1.0"?><root1>Content</root1><root2>More</root2>';
if (!validateSingleRoot($xml)) {
    echo "Multiple root elements detected";
}
```

### Fix 3: Remove Extra Content

Strip any content after the root element closes:

```php
function removeJunkAfterRoot($xml) {
    // Find the root element
    if (preg_match('/<(\w+)[^>]*>.*<\/\1>/s', $xml, $matches)) {
        $rootTag = $matches[1];
        $rootEnd = strpos($xml, "</$rootTag>") + strlen("</$rootTag>");
        $xml = substr($xml, 0, $rootEnd);
    }
    return $xml;
}

$xml = '<?xml version="1.0"?><root>Content</root>Extra';
$xml = removeJunkAfterRoot($xml);
```

### Fix 4: Use DOM to Clean XML

Leverage PHP's DOM to automatically clean the document:

```php
function cleanXmlDocument($xml) {
    $doc = new DOMDocument();
    $doc->loadXML($xml);
    
    // DOM will only keep the root element and its content
    return $doc->saveXML();
}
```

### Fix 5: Validate and Fix Programmatically

Create a comprehensive validation function:

```php
function validateAndFixXml($xml) {
    $xml = trim($xml);
    
    // Find root element
    if (preg_match('/<(\w+)[^>]*>/', $xml, $matches)) {
        $rootTag = $matches[1];
        $rootStart = strpos($xml, $matches[0]);
        $rootEnd = strrpos($xml, "</$rootTag>");
        
        if ($rootEnd !== false) {
            $rootContent = substr($xml, $rootStart, $rootEnd - $rootStart + strlen("</$rootTag>"));
            return $rootContent;
        }
    }
    
    return $xml;
}
```

## Examples

```php
// Basic junk after document element detection
$xml = '<?xml version="1.0"?><root>Content</root>Extra';
$parser = xml_parser_create();
xml_parse($parser, $xml);
$error = xml_get_error_code($parser);
if ($error === XML_ERROR_JUNK_AFTER_DOC_ELEMENT) {
    echo "Content found after root element";
}
xml_parser_free($parser);
```

```php
// Clean XML document
function cleanXmlInput($xml) {
    // Remove everything after the root element closes
    if (preg_match('/<(\w+)[^>]*>.*<\/\1>/s', $xml, $matches)) {
        $rootTag = $matches[1];
        $xml = $matches[0];
        
        // Re-add XML declaration if present
        if (strpos($xml, '<?xml') !== 0) {
            $xml = '<?xml version="1.0"?>' . $xml;
        }
    }
    
    return $xml;
}

$xml = '<?xml version="1.0"?><root>Content</root>Invalid content';
$xml = cleanXmlInput($xml);
```

```php
// Validate document structure
function validateDocumentStructure($xml) {
    $issues = [];
    
    // Check for single root
    preg_match_all('/<(\w+)[^>]*>/', $xml, $matches);
    $rootCount = count(array_unique($matches[1]));
    
    if ($rootCount > 1) {
        $issues[] = "Multiple root elements found";
    }
    
    // Check for content after root
    if (preg_match('/<\/(\w+)>.*\w/s', $xml, $matches)) {
        $issues[] = "Content found after closing root tag";
    }
    
    return $issues;
}

$xml = '<?xml version="1.0"?><root>Content</root>Extra';
$issues = validateDocumentStructure($xml);
print_r($issues);
```

```php
// Fix multiple root elements
function fixMultipleRoots($xml) {
    preg_match_all('/<(\w+)[^>]*>.*?<\/\1>/s', $xml, $matches);
    
    if (count($matches[0]) > 1) {
        $xml = '<?xml version="1.0"?><root>';
        foreach ($matches[0] as $element) {
            $xml .= $element;
        }
        $xml .= '</root>';
    }
    
    return $xml;
}

$xml = '<?xml version="1.0"?><item>1</item><item>2</item>';
$xml = fixMultipleRoots($xml);
```

## Related Errors

- [XML_ERROR_SYNTAX](xml-error-syntax.md) - XML syntax error
- [XML_ERROR_NO_ELEMENTS](xml-error-no-elements.md) - No elements found in XML
- [XML_ERROR_TAG_MISMATCH](xml-error-tag-mismatch.md) - Opening and closing tags don't match