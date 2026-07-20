---
title: "[Solution] PHP XML_ERROR_UNCLOSED_TOKEN — Token Not Properly Closed"
description: "Fix PHP XML_ERROR_UNCLOSED_TOKEN by closing all tags, checking attribute quotes, and verifying tag nesting. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# PHP XML_ERROR_UNCLOSED_TOKEN — Token Not Properly Closed

XML_ERROR_UNCLOSED_TOKEN occurs when the XML parser encounters a token that was started but not properly closed. This commonly happens with unclosed tags, attributes with missing quotes, or incomplete CDATA sections. Every opening token must have a corresponding closing token.

## Common Causes

```php
// Unclosed opening tag
$xml = '<?xml version="1.0"?><root><child>Content';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_UNCLOSED_TOKEN
```

```php
// Missing closing quote on attribute
$xml = '<?xml version="1.0"?><root attr="value>Content</root>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_UNCLOSED_TOKEN
```

```php
// Unclosed CDATA section
$xml = '<?xml version="1.0"?><root><![CDATA[Content</root>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_UNCLOSED_TOKEN
```

```php
// Unclosed comment
$xml = '<?xml version="1.0"?><root><!-- comment</root>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_UNCLOSED_TOKEN
```

```php
// Missing closing tag entirely
$xml = '<?xml version="1.0"?><root><child>Content</child>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_UNCLOSED_TOKEN
```

## How to Fix

### Fix 1: Close All Tags

Ensure every opening tag has a corresponding closing tag:

```php
// Bad: Missing closing tag
$xml = '<root><child>Content</child>';

// Good: All tags closed
$xml = '<root><child>Content</child></root>';
```

### Fix 2: Check Attribute Quotes

Verify all attribute values are properly quoted:

```php
function validateAttributeQuotes($xml) {
    // Check for unclosed quotes
    $pattern = '/="[^"]*$/m';
    if (preg_match($pattern, $xml)) {
        return false;
    }
    return true;
}

$xml = '<?xml version="1.0"?><root attr="value">Content</root>';
if (!validateAttributeQuotes($xml)) {
    echo "Unclosed attribute quotes detected";
}
```

### Fix 3: Verify Tag Nesting

Check that tags are properly nested:

```php
function checkTagNesting($xml) {
    $tags = [];
    preg_match_all('/<(\w+)[^>]*>/', $xml, $matches);
    
    foreach ($matches[1] as $tag) {
        if (!in_array($tag, $tags)) {
            $tags[] = $tag;
        } else {
            // Remove tag when closing
            $index = array_search($tag, $tags);
            unset($tags[$index]);
            $tags = array_values($tags);
        }
    }
    
    return empty($tags);
}
```

### Fix 4: Fix CDATA Sections

Ensure CDATA sections are properly closed:

```php
$content = 'Content with <special> characters';
$xml = '<?xml version="1.0"?><root><![CDATA[' . $content . ']]></root>';
```

### Fix 5: Validate Complete Document

Check the entire document structure:

```php
function validateXmlComplete($xml) {
    libxml_use_internal_errors(true);
    $doc = new DOMDocument();
    $result = $doc->loadXML($xml);
    $errors = libxml_get_errors();
    libxml_clear_errors();
    
    return [
        'valid' => $result,
        'errors' => $errors
    ];
}
```

## Examples

```php
// Basic unclosed token detection
$xml = '<?xml version="1.0"?><root><child>Content';
$parser = xml_parser_create();
xml_parse($parser, $xml);
$error = xml_get_error_code($parser);
if ($error === XML_ERROR_UNCLOSED_TOKEN) {
    echo "Unclosed token at line " . xml_get_current_line_number($parser);
    echo " column " . xml_get_current_column_number($parser);
}
xml_parser_free($parser);
```

```php
// Auto-fix common unclosed token issues
function fixUnclosedTokens($xml) {
    // Add missing root closing tag
    if (preg_match('/<(\w+)[^>]*>.*$/s', $xml, $matches)) {
        $rootTag = $matches[1];
        if (strpos($xml, "</$rootTag>") === false) {
            $xml .= "</$rootTag>";
        }
    }
    
    return $xml;
}
```

```php
// Comprehensive token validation
function validateAllTokens($xml) {
    $issues = [];
    
    // Check for unclosed tags
    preg_match_all('/<(\w+)/', $xml, $openTags);
    preg_match_all('/<\/(\w+)/', $xml, $closeTags);
    
    foreach ($openTags[1] as $index => $tag) {
        if (!in_array($tag, $closeTags[1])) {
            $issues[] = "Unclosed tag: $tag";
        }
    }
    
    return $issues;
}
```

```php
// Fix attribute quotes
function fixAttributeQuotes($xml) {
    // Find attributes without quotes
    $xml = preg_replace('/(\w+)=([^\s"<>]+)/', '$1="$2"', $xml);
    return $xml;
}

$xml = '<?xml version="1.0"?><root attr=value>Content</root>';
$xml = fixAttributeQuotes($xml);
```

## Related Errors

- [XML_ERROR_SYNTAX](xml-error-syntax.md) - XML syntax error
- [XML_ERROR_TAG_MISMATCH](xml-error-tag-mismatch.md) - Opening and closing tags don't match
- [XML_ERROR_UNCLOSED_CDATA_SECTION](xml-error-unclosed-cdata-section.md) - CDATA section not properly closed