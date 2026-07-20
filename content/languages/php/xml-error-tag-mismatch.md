---
title: "[Solution] PHP XML_ERROR_TAG_MISMATCH — Opening and Closing Tags Don't Match"
description: "Fix PHP XML_ERROR_TAG_MISMATCH by checking tag names, verifying nesting, and fixing typos. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 7
---

# PHP XML_ERROR_TAG_MISMATCH — Opening and Closing Tags Don't Match

XML_ERROR_TAG_MISMATCH occurs when an opening tag doesn't have a matching closing tag, or vice versa. This is a common XML parsing error that indicates malformed document structure. Every opening tag must have a corresponding closing tag with the exact same name.

## Common Causes

```php
// Tag name typo
$xml = '<?xml version="1.0"?><root><child>Content</Child></root>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_TAG_MISMATCH
```

```php
// Missing closing tag
$xml = '<?xml version="1.0"?><root><child>Content</child>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_TAG_MISMATCH
```

```php
// Wrong nesting order
$xml = '<?xml version="1.0"?><root><child><subchild>Content</child></subchild></root>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_TAG_MISMATCH
```

```php
// Self-closing tag mismatch
$xml = '<?xml version="1.0"?><root><child/>Content</root>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_TAG_MISMATCH
```

```php
// Case sensitivity issues
$xml = '<?xml version="1.0"?><Root><child>Content</child></root>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_TAG_MISMATCH
```

## How to Fix

### Fix 1: Check Tag Names

Verify opening and closing tags have identical names:

```php
function checkTagNames($xml) {
    preg_match_all('/<(\w+)[^>]*>/', $xml, $openTags);
    preg_match_all('/<\/(\w+)>/', $xml, $closeTags);
    
    foreach ($openTags[1] as $index => $tag) {
        if (!isset($closeTags[1][$index]) || $closeTags[1][$index] !== $tag) {
            return false;
        }
    }
    return true;
}
```

### Fix 2: Verify Nesting Order

Ensure tags are properly nested:

```php
function verifyNesting($xml) {
    $stack = [];
    preg_match_all('/<(\w+)[^>]*\/?>|<\/(\w+)>/', $xml, $matches, PREG_SET_ORDER);
    
    foreach ($matches as $match) {
        if (isset($match[1])) {
            // Opening tag (or self-closing)
            if (!preg_match('/\/$/', $match[0])) {
                $stack[] = $match[1];
            }
        } elseif (isset($match[2])) {
            // Closing tag
            if (empty($stack) || end($stack) !== $match[2]) {
                return false;
            }
            array_pop($stack);
        }
    }
    
    return empty($stack);
}
```

### Fix 3: Fix Typos in Tag Names

Review and correct any typos:

```php
// Common typos to check
$typoPairs = [
    'child' => 'Child',
    'root' => 'Root',
    'item' => 'Item',
    'data' => 'Data'
];

$xml = '<?xml version="1.0"?><root><child>Content</Child></root>';
foreach ($typoPairs as $correct => $wrong) {
    $xml = str_replace("</$wrong>", "</$correct>", $xml);
}
```

### Fix 4: Use DOM Parser for Validation

Let PHP's DOM parser identify mismatches:

```php
function validateTagMatching($xml) {
    libxml_use_internal_errors(true);
    $doc = new DOMDocument();
    $result = $doc->loadXML($xml);
    $errors = libxml_get_errors();
    libxml_clear_errors();
    
    $tagErrors = array_filter($errors, function($error) {
        return strpos($error->message, 'mismatch') !== false;
    });
    
    return empty($tagErrors);
}
```

### Fix 5: Auto-fix Common Mismatches

Automatically correct common tag mismatches:

```php
function fixCommonTagMismatches($xml) {
    // Fix case sensitivity
    $xml = preg_replace('/<\/([A-Z]\w+)>/', function($matches) {
        return '</' . strtolower($matches[1]) . '>';
    }, $xml);
    
    // Add missing closing tags
    preg_match_all('/<(\w+)[^>]*>/', $xml, $matches);
    foreach ($matches[1] as $tag) {
        if (strpos($xml, "</$tag>") === false && 
            strpos($xml, "/>") === false) {
            $xml .= "</$tag>";
        }
    }
    
    return $xml;
}
```

## Examples

```php
// Basic tag mismatch detection
$xml = '<?xml version="1.0"?><root><child>Content</Child></root>';
$parser = xml_parser_create();
xml_parse($parser, $xml);
$error = xml_get_error_code($parser);
if ($error === XML_ERROR_TAG_MISMATCH) {
    echo "Tag mismatch at line " . xml_get_current_line_number($parser);
}
xml_parser_free($parser);
```

```php
// Complete tag validation function
function validateAllTags($xml) {
    $issues = [];
    
    // Extract all tags
    preg_match_all('/<(\w+)[^>]*\/?>|<\/(\w+)>/', $xml, $matches, PREG_SET_ORDER);
    
    $stack = [];
    foreach ($matches as $match) {
        if (isset($match[1])) {
            // Opening tag
            $stack[] = ['tag' => $match[1], 'position' => $match[0]];
        } elseif (isset($match[2])) {
            // Closing tag
            if (empty($stack)) {
                $issues[] = "Unexpected closing tag: </{$match[2]}>";
            } elseif (end($stack)['tag'] !== $match[2]) {
                $issues[] = "Mismatched tags: <" . end($stack)['tag'] . "> vs </{$match[2]}>";
            } else {
                array_pop($stack);
            }
        }
    }
    
    while (!empty($stack)) {
        $tag = array_pop($stack);
        $issues[] = "Unclosed tag: <{$tag['tag']}>";
    }
    
    return $issues;
}
```

```php
// Fix tag mismatches
function fixTagMismatches($xml) {
    // Normalize tag names to lowercase
    $xml = preg_replace_callback('/<\/([A-Z]\w+)>/', function($matches) {
        return '</' . strtolower($matches[1]) . '>';
    }, $xml);
    
    // Fix common typos
    $xml = str_replace('</Chid>', '</child>', $xml);
    $xml = str_replace('</rot>', '</root>', $xml);
    
    return $xml;
}

$xml = '<?xml version="1.0"?><root><child>Content</Child></root>';
$xml = fixTagMismatches($xml);
```

## Related Errors

- [XML_ERROR_SYNTAX](xml-error-syntax.md) - XML syntax error
- [XML_ERROR_NO_ELEMENTS](xml-error-no-elements.md) - No elements found in XML
- [XML_ERROR_UNCLOSED_TOKEN](xml-error-unclosed-token.md) - Token not properly closed