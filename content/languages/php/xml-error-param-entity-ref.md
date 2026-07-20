---
title: "[Solution] PHP XML_ERROR_PARAM_ENTITY_REF — Parameter Entity Reference Error"
description: "Fix PHP XML_ERROR_PARAM_ENTITY_REF by checking entity definition, verifying entity syntax, and using valid entity references. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 10
---

# PHP XML_ERROR_PARAM_ENTITY_REF — Parameter Entity Reference Error

XML_ERROR_PARAM_ENTITY_REF occurs when there is an error with a parameter entity reference in the XML document. Parameter entities are used in the DTD (Document Type Definition) and follow specific syntax rules. This error typically happens when entity references are malformed or used incorrectly.

## Common Causes

```php
// Undefined parameter entity
$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY % myentity "value">
    <!ELEMENT root (#PCDATA)>
]>
<root>&myentity;</root>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_PARAM_ENTITY_REF
```

```php
// Incorrect parameter entity syntax
$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY % myentity value>
]>
<root>&myentity;</root>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_PARAM_ENTITY_REF
```

```php
// Parameter entity reference in content
$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY % myentity "value">
]>
<root>%myentity;</root>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_PARAM_ENTITY_REF
```

```php
// Missing parameter entity definition
$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ELEMENT root (#PCDATA)>
]>
<root>&undefined;</root>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_PARAM_ENTITY_REF
```

```php
// Recursive parameter entity
$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY % entity1 "%entity2;">
    <!ENTITY % entity2 "%entity1;">
]>
<root>Content</root>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_PARAM_ENTITY_REF
```

## How to Fix

### Fix 1: Check Entity Definition

Ensure parameter entities are properly defined:

```php
// Proper parameter entity definition
$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY % myentity "value">
    <!ELEMENT root (#PCDATA)>
]>
<root>&myentity;</root>';
```

### Fix 2: Verify Entity Syntax

Validate entity reference syntax:

```php
function validateEntitySyntax($xml) {
    // Check for proper entity definition syntax
    $pattern = '/<!ENTITY\s+%\s+(\w+)\s+"([^"]*)">/';
    preg_match_all($pattern, $xml, $matches);
    
    $entities = [];
    foreach ($matches[1] as $index => $name) {
        $entities[$name] = $matches[2][$index];
    }
    
    return $entities;
}

$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY % myentity "value">
]>
<root>Content</root>';

$entities = validateEntitySyntax($xml);
print_r($entities);
```

### Fix 3: Use Valid Entity References

Ensure entity references are properly formatted:

```php
// Valid general entity reference
$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY myentity "value">
]>
<root>&myentity;</root>';
```

### Fix 4: Disable Parameter Entities

If not needed, simplify by removing parameter entities:

```php
// Instead of parameter entities, use direct content
$xml = '<?xml version="1.0"?><root>Direct content here</root>';
```

### Fix 5: Validate Entity Usage

Check that entities are used correctly:

```php
function validateEntityUsage($xml) {
    $issues = [];
    
    // Check for % in content (should only be in DTD)
    if (preg_match('/<root>.*%.*<\/root>/s', $xml)) {
        $issues[] = "Parameter entity reference in content";
    }
    
    // Check for undefined entities
    preg_match_all('/&(\w+);/', $xml, $refs);
    preg_match_all('/<!ENTITY\s+(\w+)/', $xml, $defs);
    
    foreach ($refs[1] as $ref) {
        if (!in_array($ref, $defs[1])) {
            $issues[] = "Undefined entity: $ref";
        }
    }
    
    return $issues;
}
```

## Examples

```php
// Basic parameter entity reference error detection
$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY % myentity "value">
]>
<root>&myentity;</root>';
$parser = xml_parser_create();
xml_parse($parser, $xml);
$error = xml_get_error_code($parser);
if ($error === XML_ERROR_PARAM_ENTITY_REF) {
    echo "Parameter entity reference error";
}
xml_parser_free($parser);
```

```php
// Safe entity handling
function safeEntityParse($xml) {
    // Remove all parameter entities for safety
    $xml = preg_replace('/<!ENTITY\s+%\s+\w+\s+"[^"]*">/', '', $xml);
    
    $parser = xml_parser_create();
    xml_parse($parser, $xml);
    $error = xml_get_error_code($parser);
    xml_parser_free($parser);
    
    return $error === XML_ERROR_NONE;
}

$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY % myentity "value">
]>
<root>Content</root>';

if (safeEntityParse($xml)) {
    echo "Parsed successfully";
}
```

```php
// Fix parameter entity issues
function fixParameterEntities($xml) {
    // Convert parameter entities to general entities
    $xml = preg_replace_callback('/<!ENTITY\s+%\s+(\w+)\s+"([^"]*)">/', function($matches) {
        return '<!ENTITY ' . $matches[1] . ' "' . $matches[2] . '">';
    }, $xml);
    
    return $xml;
}

$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY % myentity "value">
]>
<root>&myentity;</root>';

$xml = fixParameterEntities($xml);
```

```php
// Validate complete entity structure
function validateEntityStructure($xml) {
    libxml_use_internal_errors(true);
    $doc = new DOMDocument();
    $result = $doc->loadXML($xml);
    $errors = libxml_get_errors();
    libxml_clear_errors();
    
    $entityErrors = array_filter($errors, function($error) {
        return strpos($error->message, 'entity') !== false;
    });
    
    return empty($entityErrors);
}
```

## Related Errors

- [XML_ERROR_UNDEFINED_ENTITY](xml-error-undefined-entity.md) - Undefined entity reference
- [XML_ERROR_RECURSIVE_ENTITY_REF](xml-error-recursive-entity-ref.md) - Recursive entity reference
- [XML_ERROR_ASYNC_ENTITY](xml-error-async-entity.md) - Async entity reference