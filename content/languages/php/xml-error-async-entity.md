---
title: "[Solution] PHP XML_ERROR_ASYNC_ENTITY — Async Entity Reference"
description: "Fix PHP XML_ERROR_ASYNC_ENTITY by defining entities before use, checking entity placement, and using proper entity definitions. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 13
---

# PHP XML_ERROR_ASYNC_ENTITY — Async Entity Reference

XML_ERROR_ASYNC_ENTITY occurs when an entity is referenced before it is defined in the DTD. XML requires that all entity definitions appear before any references to those entities. This error typically happens when entity definitions are placed after the content that uses them.

## Common Causes

```php
// Entity referenced before definition
$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <root>&myentity;</root>
    <!ENTITY myentity "value">
]>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_ASYNC_ENTITY
```

```php
// Entity definition in wrong order
$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ELEMENT root (#PCDATA)>
    <!ENTITY myentity "value">
]>
<root>&myentity;</root>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_ASYNC_ENTITY
```

```php
// Entity defined after use in content
$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <root>&myentity;</root>
    <!ENTITY myentity "value">
]>
<root>&myentity;</root>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_ASYNC_ENTITY
```

```php
// Parameter entity referenced before definition
$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY % myparam "value">
    <!ELEMENT root (#PCDATA)>
]>
<root>Content</root>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_ASYNC_ENTITY
```

```php
// Circular entity reference through async placement
$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY a "&b;">
    <!ENTITY b "value">
]>
<root>&a;</root>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_ASYNC_ENTITY
```

## How to Fix

### Fix 1: Define Entities Before Use

Move entity definitions to before any references:

```php
// Bad: Entity after reference
$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <root>&myentity;</root>
    <!ENTITY myentity "value">
]>';

// Good: Entity before reference
$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY myentity "value">
]>
<root>&myentity;</root>';
```

### Fix 2: Check Entity Placement

Validate entity definition order:

```php
function validateEntityOrder($xml) {
    preg_match_all('/&(\w+);/', $xml, $refs);
    preg_match_all('/<!ENTITY\s+(\w+)/', $xml, $defs);
    
    $defined = [];
    $issues = [];
    
    foreach ($refs[1] as $ref) {
        if (!in_array($ref, $defined)) {
            $issues[] = "Entity &$ref; used before definition";
        }
    }
    
    return $issues;
}

$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <root>&myentity;</root>
    <!ENTITY myentity "value">
]>';
$issues = validateEntityOrder($xml);
print_r($issues);
```

### Fix 3: Use Proper Entity Definitions

Ensure entities are properly declared:

```php
// Proper entity definition structure
$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY myentity "value">
    <!ELEMENT root (#PCDATA)>
]>
<root>&myentity;</root>';
```

### Fix 4: Reorder DTD Content

Reorganize the DTD to have entities first:

```php
function reorderDtd($xml) {
    preg_match_all('/<!DOCTYPE\s+\w+\s+\[(.*?)\]>/s', $xml, $dtdMatches);
    
    if (isset($dtdMatches[1][0])) {
        $dtd = $dtdMatches[1][0];
        
        // Extract entities and other declarations
        preg_match_all('/<!ENTITY\s+[^>]+>/', $dtd, $entities);
        preg_match_all('/<!ELEMENT\s+[^>]+>/', $dtd, $elements);
        preg_match_all('/<!ATTLIST\s+[^>]+>/', $dtd, $attributes);
        
        // Reorder: entities first
        $newDtd = implode("\n    ", $entities[0]) . "\n";
        $newDtd .= implode("\n    ", $elements[0]) . "\n";
        $newDtd .= implode("\n    ", $attributes[0]);
        
        $xml = str_replace($dtdMatches[1][0], $newDtd, $xml);
    }
    
    return $xml;
}
```

### Fix 5: Validate Complete Structure

Use DOM to validate entity order:

```php
function validateDtdStructure($xml) {
    libxml_use_internal_errors(true);
    $doc = new DOMDocument();
    $result = $doc->loadXML($xml);
    $errors = libxml_get_errors();
    libxml_clear_errors();
    
    $asyncErrors = array_filter($errors, function($error) {
        return strpos($error->message, 'async') !== false ||
               strpos($error->message, 'before') !== false;
    });
    
    return empty($asyncErrors);
}
```

## Examples

```php
// Basic async entity detection
$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <root>&myentity;</root>
    <!ENTITY myentity "value">
]>';
$parser = xml_parser_create();
xml_parse($parser, $xml);
$error = xml_get_error_code($parser);
if ($error === XML_ERROR_ASYNC_ENTITY) {
    echo "Async entity reference found";
}
xml_parser_free($parser);
```

```php
// Fix async entity ordering
function fixAsyncEntities($xml) {
    preg_match_all('/<!DOCTYPE\s+\w+\s+\[(.*?)\]>/s', $xml, $dtdMatches);
    
    if (isset($dtdMatches[1][0])) {
        $dtd = $dtdMatches[1][0];
        
        // Extract all declarations
        preg_match_all('/<!ENTITY\s+[^>]+>/', $dtd, $entities);
        preg_match_all('/<!ELEMENT\s+[^>]+>/', $dtd, $elements);
        preg_match_all('/<!ATTLIST\s+[^>]+>/', $dtd, $attributes);
        
        // Rebuild DTD with entities first
        $newDtd = '';
        if (!empty($entities[0])) {
            $newDtd .= implode("\n    ", $entities[0]) . "\n";
        }
        if (!empty($elements[0])) {
            $newDtd .= implode("\n    ", $elements[0]) . "\n";
        }
        if (!empty($attributes[0])) {
            $newDtd .= implode("\n    ", $attributes[0]);
        }
        
        $xml = str_replace($dtdMatches[1][0], $newDtd, $xml);
    }
    
    return $xml;
}

$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <root>&myentity;</root>
    <!ENTITY myentity "value">
]>';

$xml = fixAsyncEntities($xml);
```

```php
// Validate entity order
function validateEntityOrderStrict($xml) {
    preg_match_all('/&(\w+);/', $xml, $refs);
    preg_match_all('/<!ENTITY\s+(\w+)/', $xml, $defs);
    
    $defined = [];
    
    foreach ($defs[1] as $def) {
        $defined[] = $def;
    }
    
    foreach ($refs[1] as $ref) {
        if (!in_array($ref, $defined)) {
            return false;
        }
    }
    
    return true;
}

$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY myentity "value">
]>
<root>&myentity;</root>';

if (validateEntityOrderStrict($xml)) {
    echo "Entity order is valid";
}
```

## Related Errors

- [XML_ERROR_PARAM_ENTITY_REF](xml-error-param-entity-ref.md) - Parameter entity reference error
- [XML_ERROR_UNDEFINED_ENTITY](xml-error-undefined-entity.md) - Undefined entity reference
- [XML_ERROR_RECURSIVE_ENTITY_REF](xml-error-recursive-entity-ref.md) - Recursive entity reference