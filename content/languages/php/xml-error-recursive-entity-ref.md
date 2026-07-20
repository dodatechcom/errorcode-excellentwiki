---
title: "[Solution] PHP XML_ERROR_RECURSIVE_ENTITY_REF — Recursive Entity Reference"
description: "Fix PHP XML_ERROR_RECURSIVE_ENTITY_REF by breaking recursion, redefining entities, and simplifying entity structure. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 12
---

# PHP XML_ERROR_RECURSIVE_ENTITY_REF — Recursive Entity Reference

XML_ERROR_RECURSIVE_ENTITY_REF occurs when an entity references itself directly or indirectly through a chain of other entities. This creates an infinite loop that would cause the parser to expand entities forever. XML parsers must detect and reject recursive entity definitions.

## Common Causes

```php
// Direct self-reference
$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY myentity "&myentity;">
]>
<root>&myentity;</root>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_RECURSIVE_ENTITY_REF
```

```php
// Indirect recursion through two entities
$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY entity1 "&entity2;">
    <!ENTITY entity2 "&entity1;">
]>
<root>&entity1;</root>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_RECURSIVE_ENTITY_REF
```

```php
// Longer recursion chain
$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY a "&b;">
    <!ENTITY b "&c;">
    <!ENTITY c "&a;">
]>
<root>&a;</root>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_RECURSIVE_ENTITY_REF
```

```php
// Self-referencing parameter entity
$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY % self "&self;">
]>
<root>Content</root>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_RECURSIVE_ENTITY_REF
```

```php
// Indirect self-reference
$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY entity1 "&entity2;">
    <!ENTITY entity2 "&entity1;">
]>
<root>&entity2;</root>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_RECURSIVE_ENTITY_REF
```

## How to Fix

### Fix 1: Break Recursion

Remove or modify one entity in the recursive chain:

```php
// Bad: Recursive
$xml = '<!DOCTYPE root [
    <!ENTITY entity1 "&entity2;">
    <!ENTITY entity2 "&entity1;">
]>';

// Good: Break recursion
$xml = '<!DOCTYPE root [
    <!ENTITY entity1 "value1">
    <!ENTITY entity2 "value2">
]>';
```

### Fix 2: Redefine Entities

Replace recursive entities with concrete values:

```php
function fixRecursiveEntities($xml) {
    // Find all entity definitions
    preg_match_all('/<!ENTITY\s+(\w+)\s+"([^"]*)">/', $xml, $matches);
    
    $entities = array_combine($matches[1], $matches[2]);
    
    // Check for recursion
    foreach ($entities as $name => $value) {
        if (strpos($value, '&' . $name . ';') !== false) {
            // Replace self-reference with empty or default
            $xml = str_replace(
                '<!ENTITY ' . $name . ' "' . $value . '">',
                '<!ENTITY ' . $name . ' "">',
                $xml
            );
        }
    }
    
    return $xml;
}

$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY myentity "&myentity;">
]>
<root>&myentity;</root>';

$xml = fixRecursiveEntities($xml);
```

### Fix 3: Simplify Entity Structure

Replace complex entity chains with direct content:

```php
// Instead of entities, use direct content
$xml = '<?xml version="1.0"?><root>Direct content here</root>';
```

### Fix 4: Detect Recursion Before Parsing

Check for recursive references:

```php
function detectEntityRecursion($xml) {
    preg_match_all('/<!ENTITY\s+(\w+)\s+"([^"]*)">/', $xml, $matches);
    
    $entities = array_combine($matches[1], $matches[2]);
    
    foreach ($entities as $name => $value) {
        // Check for direct self-reference
        if (strpos($value, '&' . $name . ';') !== false) {
            return true;
        }
        
        // Check for indirect references
        $visited = [$name];
        $current = $value;
        
        while (preg_match('/&(\w+);/', $current, $match)) {
            $ref = $match[1];
            if (in_array($ref, $visited)) {
                return true;
            }
            $visited[] = $ref;
            
            if (isset($entities[$ref])) {
                $current = $entities[$ref];
            } else {
                break;
            }
        }
    }
    
    return false;
}

$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY entity1 "&entity2;">
    <!ENTITY entity2 "&entity1;">
]>
<root>&entity1;</root>';

if (detectEntityRecursion($xml)) {
    echo "Recursive entity reference detected";
}
```

### Fix 5: Use Safe Entity Definitions

Create entities that don't reference other entities:

```php
function createSafeEntities($xml) {
    preg_match_all('/<!ENTITY\s+(\w+)\s+"([^"]*)">/', $xml, $matches);
    
    $fixed = $xml;
    foreach ($matches[1] as $index => $name) {
        $value = $matches[2][$index];
        
        // Remove any entity references from value
        $safeValue = preg_replace('/&\w+;/', '', $value);
        
        $fixed = str_replace(
            '<!ENTITY ' . $name . ' "' . $value . '">',
            '<!ENTITY ' . $name . ' "' . $safeValue . '">',
            $fixed
        );
    }
    
    return $fixed;
}
```

## Examples

```php
// Basic recursive entity detection
$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY myentity "&myentity;">
]>
<root>&myentity;</root>';
$parser = xml_parser_create();
xml_parse($parser, $xml);
$error = xml_get_error_code($parser);
if ($error === XML_ERROR_RECURSIVE_ENTITY_REF) {
    echo "Recursive entity reference found";
}
xml_parser_free($parser);
```

```php
// Fix recursive entities
function fixAllRecursion($xml) {
    preg_match_all('/<!ENTITY\s+(\w+)\s+"([^"]*)">/', $xml, $matches);
    
    $entities = array_combine($matches[1], $matches[2]);
    $fixed = $xml;
    
    foreach ($entities as $name => $value) {
        // Check for any reference
        if (preg_match('/&\w+;/', $value)) {
            // Replace with empty string
            $fixed = str_replace(
                '<!ENTITY ' . $name . ' "' . $value . '">',
                '<!ENTITY ' . $name . ' "">',
                $fixed
            );
        }
    }
    
    return $fixed;
}

$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY a "&b;">
    <!ENTITY b "&a;">
]>
<root>&a;</root>';

$xml = fixAllRecursion($xml);
```

```php
// Validate no recursion exists
function validateNoRecursion($xml) {
    preg_match_all('/<!ENTITY\s+(\w+)\s+"([^"]*)">/', $xml, $matches);
    
    $entities = array_combine($matches[1], $matches[2]);
    
    foreach ($entities as $name => $value) {
        $visited = [$name];
        $current = $value;
        
        while (preg_match('/&(\w+);/', $current, $match)) {
            $ref = $match[1];
            
            if (in_array($ref, $visited)) {
                return false;
            }
            
            $visited[] = $ref;
            
            if (isset($entities[$ref])) {
                $current = str_replace("&$ref;", $entities[$ref], $current);
            } else {
                break;
            }
        }
    }
    
    return true;
}

$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY a "value">
    <!ENTITY b "another value">
]>
<root>&a;&b;</root>';

if (validateNoRecursion($xml)) {
    echo "No recursion detected";
}
```

## Related Errors

- [XML_ERROR_PARAM_ENTITY_REF](xml-error-param-entity-ref.md) - Parameter entity reference error
- [XML_ERROR_UNDEFINED_ENTITY](xml-error-undefined-entity.md) - Undefined entity reference
- [XML_ERROR_ASYNC_ENTITY](xml-error-async-entity.md) - Async entity reference