---
title: "[Solution] PHP XML_ERROR_UNDEFINED_ENTITY — Undefined Entity Reference"
description: "Fix PHP XML_ERROR_UNDEFINED_ENTITY by defining entity, checking entity name, and using numeric references. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 11
---

# PHP XML_ERROR_UNDEFINED_ENTITY — Undefined Entity Reference

XML_ERROR_UNDEFINED_ENTITY occurs when the XML parser encounters an entity reference that hasn't been defined. Entity references start with `&` and end with `;`, but must be properly declared in the DTD or use predefined XML entities. This error is common when using custom entities without defining them.

## Common Causes

```php
// Undefined custom entity
$xml = '<?xml version="1.0"?><root>&myentity;</root>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_UNDEFINED_ENTITY
```

```php
// Typo in entity name
$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY myentity "value">
]>
<root>&myentty;</root>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_UNDEFINED_ENTITY
```

```php
// Missing entity definition
$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ELEMENT root (#PCDATA)>
]>
<root>&undefined;</root>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_UNDEFINED_ENTITY
```

```php
// Using parameter entity syntax incorrectly
$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY % myentity "value">
]>
<root>&myentity;</root>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_UNDEFINED_ENTITY
```

```php
// Case sensitivity mismatch
$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY MyEntity "value">
]>
<root>&myentity;</root>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_UNDEFINED_ENTITY
```

## How to Fix

### Fix 1: Define Entity

Add entity definition to the DTD:

```php
// Define entity before use
$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY myentity "value">
]>
<root>&myentity;</root>';
```

### Fix 2: Check Entity Name

Verify entity name matches definition:

```php
function findUndefinedEntities($xml) {
    preg_match_all('/&(\w+);/', $xml, $refs);
    preg_match_all('/<!ENTITY\s+(\w+)/', $xml, $defs);
    
    $undefined = [];
    foreach ($refs[1] as $ref) {
        if (!in_array($ref, $defs[1])) {
            $undefined[] = $ref;
        }
    }
    
    return $undefined;
}

$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY myentity "value">
]>
<root>&myentity;&undefined;</root>';

$undefined = findUndefinedEntities($xml);
print_r($undefined); // ["undefined"]
```

### Fix 3: Use Numeric References

Replace undefined entities with numeric character references:

```php
// Instead of &myentity;, use:
$xml = '<?xml version="1.0"?><root>&#x0041;</root>'; // A
$xml = '<?xml version="1.0"?><root>&#65;</root>'; // A
```

### Fix 4: Use Predefined XML Entities

Use standard XML entities that don't need definition:

```php
// Predefined entities
$xml = '<?xml version="1.0"?><root>&amp; &lt; &gt; &quot; &apos;</root>';
```

### Fix 5: Auto-define Missing Entities

Automatically define missing entities:

```php
function autoDefineEntities($xml, $defaultValues = []) {
    $undefined = findUndefinedEntities($xml);
    
    foreach ($undefined as $entity) {
        $value = isset($defaultValues[$entity]) ? $defaultValues[$entity] : '';
        $dtd = '<!ENTITY ' . $entity . ' "' . $value . '">';
        $xml = str_replace('<!DOCTYPE', "<!DOCTYPE\n    " . $dtd, $xml);
    }
    
    return $xml;
}

$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ELEMENT root (#PCDATA)>
]>
<root>&myentity;</root>';

$xml = autoDefineEntities($xml, ['myentity' => 'default value']);
```

## Examples

```php
// Basic undefined entity detection
$xml = '<?xml version="1.0"?><root>&undefined;</root>';
$parser = xml_parser_create();
xml_parse($parser, $xml);
$error = xml_get_error_code($parser);
if ($error === XML_ERROR_UNDEFINED_ENTITY) {
    echo "Undefined entity reference found";
}
xml_parser_free($parser);
```

```php
// Complete entity validation
function validateAllEntities($xml) {
    $issues = [];
    
    // Find all entity references
    preg_match_all('/&(\w+);/', $xml, $refs);
    
    // Find all entity definitions
    preg_match_all('/<!ENTITY\s+(\w+)\s+"([^"]*)">/', $xml, $defs);
    
    $defined = array_combine($defs[1], $defs[2]);
    
    foreach (array_unique($refs[1]) as $ref) {
        if (!isset($defined[$ref])) {
            $issues[] = "Undefined entity: &$ref;";
        }
    }
    
    return $issues;
}

$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY defined "value">
]>
<root>&defined;&undefined;</root>';

$issues = validateAllEntities($xml);
print_r($issues);
```

```php
// Fix undefined entities
function fixUndefinedEntities($xml) {
    // Find undefined entities
    preg_match_all('/&(\w+);/', $xml, $refs);
    preg_match_all('/<!ENTITY\s+(\w+)/', $xml, $defs);
    
    $defined = array_flip($defs[1]);
    
    foreach (array_unique($refs[1]) as $ref) {
        if (!isset($defined[$ref])) {
            // Replace with empty or remove
            $xml = str_replace("&$ref;", '', $xml);
        }
    }
    
    return $xml;
}

$xml = '<?xml version="1.0"?><root>&undefined;</root>';
$xml = fixUndefinedEntities($xml);
```

```php
// Use predefined entities safely
function usePredefinedEntities($content) {
    $content = str_replace('&', '&amp;', $content);
    $content = str_replace('<', '&lt;', $content);
    $content = str_replace('>', '&gt;', $content);
    $content = str_replace('"', '&quot;', $content);
    $content = str_replace("'", '&apos;', $content);
    
    return $content;
}

$content = 'Use & < > " \' safely';
$xml = '<?xml version="1.0"?><root>' . usePredefinedEntities($content) . '</root>';
```

## Related Errors

- [XML_ERROR_PARAM_ENTITY_REF](xml-error-param-entity-ref.md) - Parameter entity reference error
- [XML_ERROR_RECURSIVE_ENTITY_REF](xml-error-recursive-entity-ref.md) - Recursive entity reference
- [XML_ERROR_BAD_CHAR_REF](xml-error-bad-char-ref.md) - Bad character reference