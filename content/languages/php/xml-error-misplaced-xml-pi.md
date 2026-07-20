---
title: "[Solution] PHP XML_ERROR_MISPLACED_XML_PI — XML Processing Instruction Misplaced"
description: "Fix PHP XML_ERROR_MISPLACED_XML_PI by moving PI to correct position, checking XML structure, and placing before root element. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 17
---

# PHP XML_ERROR_MISPLACED_XML_PI — XML Processing Instruction Misplaced

XML_ERROR_MISPLACED_XML_PI occurs when an XML processing instruction (PI) is placed in the wrong location. The XML declaration (`<?xml ...?>`) must be the first thing in the document, and other PIs should be placed before the root element or at specific allowed positions.

## Common Causes

```php
// XML declaration after content
$xml = '<root>Content</root><?xml version="1.0"?>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_MISPLACED_XML_PI
```

```php
// XML declaration not first
$xml = ' <?xml version="1.0"?><root/>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_MISPLACED_XML_PI
```

```php
// Processing instruction inside element
$xml = '<?xml version="1.0"?><root><?php echo "test"; ?>Content</root>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_MISPLACED_XML_PI
```

```php
// Multiple XML declarations
$xml = '<?xml version="1.0"?><?xml version="1.1"?><root/>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_MISPLACED_XML_PI
```

```php
// XML declaration after BOM
$xml = "\xEF\xBB\xBF<?xml version=\"1.0\"?><root/>";
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_MISPLACED_XML_PI
```

## How to Fix

### Fix 1: Move PI to Correct Position

Ensure XML declaration is first in the document:

```php
// Bad: PI after content
$xml = '<root>Content</root><?xml version="1.0"?>';

// Good: PI first
$xml = '<?xml version="1.0"?><root>Content</root>';
```

### Fix 2: Check XML Structure

Validate PI placement:

```php
function validatePiPlacement($xml) {
    $xml = ltrim($xml);
    
    // XML declaration must be first
    if (strpos($xml, '<?xml') === 0) {
        return true;
    }
    
    // Allow BOM before XML declaration
    if (strpos($xml, "\xEF\xBB\xBF<?xml") === 0) {
        return true;
    }
    
    return false;
}

$xml = '<?xml version="1.0"?><root/>';
if (!validatePiPlacement($xml)) {
    echo "XML declaration misplaced";
}
```

### Fix 3: Place Before Root Element

Move PIs to before the root element:

```php
// Correct PI placement
$xml = '<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="style.xsl"?>
<root>Content</root>';
```

### Fix 4: Remove Extra Declarations

Ensure only one XML declaration exists:

```php
function fixMultipleDeclarations($xml) {
    // Find first XML declaration
    if (preg_match('/<\?xml[^?]*\?>/', $xml, $matches)) {
        // Remove all other XML declarations
        $xml = preg_replace('/<\?xml[^?]*\?>/', '', $xml);
        
        // Re-add only the first one at the beginning
        $xml = $matches[0] . $xml;
    }
    
    return $xml;
}

$xml = '<?xml version="1.0"?><?xml version="1.1"?><root/>';
$xml = fixMultipleDeclarations($xml);
```

### Fix 5: Handle BOM Correctly

Process or remove BOM characters:

```php
function handleBom($xml) {
    // Remove BOM if present
    if (substr($xml, 0, 3) === "\xEF\xBB\xBF") {
        $xml = substr($xml, 3);
    }
    
    // Ensure XML declaration follows
    if (strpos($xml, '<?xml') !== 0) {
        $xml = '<?xml version="1.0"?>' . $xml;
    }
    
    return $xml;
}

$xml = "\xEF\xBB\xBF<root/>";
$xml = handleBom($xml);
```

## Examples

```php
// Basic misplaced PI detection
$xml = '<root>Content</root><?xml version="1.0"?>';
$parser = xml_parser_create();
xml_parse($parser, $xml);
$error = xml_get_error_code($parser);
if ($error === XML_ERROR_MISPLACED_XML_PI) {
    echo "XML processing instruction misplaced";
}
xml_parser_free($parser);
```

```php
// Fix all PI placement issues
function fixAllPiIssues($xml) {
    // Remove BOM
    $xml = handleBom($xml);
    
    // Remove extra XML declarations
    $xml = fixMultipleDeclarations($xml);
    
    // Ensure XML declaration is first
    if (strpos($xml, '<?xml') !== 0) {
        $xml = '<?xml version="1.0"?>' . $xml;
    }
    
    return $xml;
}

$xml = ' <?xml version="1.0"?>';
$xml = fixAllPiIssues($xml);
```

```php
// Validate complete PI structure
function validatePiStructure($xml) {
    $issues = [];
    
    // Check for XML declaration position
    $xml = ltrim($xml);
    if (strpos($xml, '<?xml') !== 0 && strpos($xml, "\xEF\xBB\xBF<?xml") !== 0) {
        $issues[] = "XML declaration not at start of document";
    }
    
    // Check for multiple XML declarations
    preg_match_all('/<\?xml[^?]*\?>/', $xml, $matches);
    if (count($matches[0]) > 1) {
        $issues[] = "Multiple XML declarations found";
    }
    
    // Check for PI inside elements
    if (preg_match('/>.*<\?[^x].*\?>.*</s', $xml)) {
        $issues[] = "Processing instruction inside element";
    }
    
    return $issues;
}

$xml = '<?xml version="1.0"?><root><?test?>Content</root>';
$issues = validatePiStructure($xml);
print_r($issues);
```

```php
// Clean XML input
function cleanXmlInput($xml) {
    // Remove BOM
    if (substr($xml, 0, 3) === "\xEF\xBB\xBF") {
        $xml = substr($xml, 3);
    }
    
    // Remove leading whitespace
    $xml = ltrim($xml);
    
    // Remove extra XML declarations
    $xml = fixMultipleDeclarations($xml);
    
    // Ensure proper XML declaration
    if (strpos($xml, '<?xml') !== 0) {
        $xml = '<?xml version="1.0"?>' . $xml;
    }
    
    return $xml;
}

$xml = '  <?xml version="1.0"?><?xml version="1.1"?><root/>';
$xml = cleanXmlInput($xml);
```

## Related Errors

- [XML_ERROR_SYNTAX](xml-error-syntax.md) - XML syntax error
- [XML_ERROR_NO_ELEMENTS](xml-error-no-elements.md) - No elements found in XML
- [XML_ERROR_UNKNOWN_ENCODING](xml-error-unknown-encoding.md) - Unknown character encoding