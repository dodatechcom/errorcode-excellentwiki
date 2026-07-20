---
title: "[Solution] PHP XML_ERROR_EXTERNAL_ENTITY_HANDLING — Error Handling External Entities"
description: "Fix PHP XML_ERROR_EXTERNAL_ENTITY_HANDLING by disabling external entities, using libxml_disable_entity_loader(), and validating input. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 21
---

# PHP XML_ERROR_EXTERNAL_ENTITY_HANDLING — Error Handling External Entities

XML_ERROR_EXTERNAL_ENTITY_HANDLING occurs when there is an error processing external entities in the XML document. This can happen when external entity loading is disabled, when the entity cannot be loaded, or when there are security restrictions preventing external entity access. Modern PHP versions disable external entity loading by default for security.

## Common Causes

```php
// External entity loading disabled (default in modern PHP)
$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY external SYSTEM "file:///etc/passwd">
]>
<root>&external;</root>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_EXTERNAL_ENTITY_HANDLING
```

```php
// Entity file not found
$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY external SYSTEM "nonexistent.xml">
]>
<root>&external;</root>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_EXTERNAL_ENTITY_HANDLING
```

```php
// Security restriction on file access
$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY external SYSTEM "file:///etc/shadow">
]>
<root>&external;</root>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_EXTERNAL_ENTITY_HANDLING
```

```php
// Remote entity with network issues
$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY external SYSTEM "http://unreachable.example.com/data.xml">
]>
<root>&external;</root>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_EXTERNAL_ENTITY_HANDLING
```

```php
// Parameter external entity
$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY % file SYSTEM "file:///etc/passwd">
    <!ENTITY % eval "<!ENTITY exfil SYSTEM '%file;'>">
]>
<root>&exfil;</root>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_EXTERNAL_ENTITY_HANDLING
```

## How to Fix

### Fix 1: Disable External Entities

Keep external entity loading disabled for security:

```php
// Modern PHP - external entities are disabled by default
$parser = xml_parser_create();
xml_parse($parser, $xml);
xml_parser_free($parser);
```

### Fix 2: Use libxml_disable_entity_loader()

Control entity loading explicitly:

```php
// Disable external entity loading (PHP < 8.0)
if (function_exists('libxml_disable_entity_loader')) {
    libxml_disable_entity_loader(true);
}

// Parse safely
$parser = xml_parser_create();
xml_parse($parser, $xml);
xml_parser_free($parser);
```

### Fix 3: Validate Input

Check for external entities before parsing:

```php
function containsExternalEntities($xml) {
    $patterns = [
        '/<!ENTITY\s+\w+\s+SYSTEM\s+/i',
        '/<!ENTITY\s+\w+\s+PUBLIC\s+/i',
        '/SYSTEM\s+"[^"]*"/',
        '/SYSTEM\s+\'[^\']*\'/'
    ];
    
    foreach ($patterns as $pattern) {
        if (preg_match($pattern, $xml)) {
            return true;
        }
    }
    
    return false;
}

$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY external SYSTEM "file.xml">
]>
<root>&external;</root>';

if (containsExternalEntities($xml)) {
    echo "External entities detected";
}
```

### Fix 4: Remove External Entities

Strip external entity declarations:

```php
function removeExternalEntities($xml) {
    // Remove external entity declarations
    $xml = preg_replace('/<!ENTITY\s+\w+\s+(SYSTEM|PUBLIC)\s+["\'][^"\']*["\']\s*>/i', '', $xml);
    
    // Remove parameter external entities
    $xml = preg_replace('/<!ENTITY\s+%\s+\w+\s+(SYSTEM|PUBLIC)\s+["\'][^"\']*["\']\s*>/i', '', $xml);
    
    return $xml;
}

$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY external SYSTEM "file.xml">
]>
<root>&external;</root>';

$xml = removeExternalEntities($xml);
```

### Fix 5: Use Safe Parser Configuration

Configure parser with security in mind:

```php
function safeExternalEntityParse($xml) {
    // Disable external entities
    if (function_exists('libxml_disable_entity_loader')) {
        libxml_disable_entity_loader(true);
    }
    
    // Remove external entities
    $xml = removeExternalEntities($xml);
    
    // Parse safely
    $parser = xml_parser_create();
    xml_parse($parser, $xml);
    $error = xml_get_error_code($parser);
    xml_parser_free($parser);
    
    return $error === XML_ERROR_NONE;
}

$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY external SYSTEM "file.xml">
]>
<root>&external;</root>';

if (safeExternalEntityParse($xml)) {
    echo "Parsed successfully";
}
```

## Examples

```php
// Basic external entity handling error detection
$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY external SYSTEM "file.xml">
]>
<root>&external;</root>';
$parser = xml_parser_create();
xml_parse($parser, $xml);
$error = xml_get_error_code($parser);
if ($error === XML_ERROR_EXTERNAL_ENTITY_HANDLING) {
    echo "External entity handling error";
}
xml_parser_free($parser);
```

```php
// Secure XML parsing
function secureXmlParse($xml) {
    // Disable external entities
    if (function_exists('libxml_disable_entity_loader')) {
        libxml_disable_entity_loader(true);
    }
    
    // Remove external entities
    $xml = removeExternalEntities($xml);
    
    // Parse safely
    libxml_use_internal_errors(true);
    $doc = new DOMDocument();
    $result = $doc->loadXML($xml);
    $errors = libxml_get_errors();
    libxml_clear_errors();
    
    return [
        'success' => $result,
        'errors' => $errors
    ];
}

$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY external SYSTEM "file.xml">
]>
<root>&external;</root>';

$result = secureXmlParse($xml);
print_r($result);
```

```php
// Validate no external entities
function validateNoExternalEntities($xml) {
    $patterns = [
        '/<!ENTITY\s+\w+\s+SYSTEM\s+/i',
        '/<!ENTITY\s+\w+\s+PUBLIC\s+/i',
        '/SYSTEM\s+"[^"]*"/',
        '/SYSTEM\s+\'[^\']*\'/'
    ];
    
    foreach ($patterns as $pattern) {
        if (preg_match($pattern, $xml)) {
            return false;
        }
    }
    
    return true;
}

$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY internal "safe content">
]>
<root>&internal;</root>';

if (validateNoExternalEntities($xml)) {
    echo "No external entities found - safe to parse";
}
```

```php
// Sanitize XML input
function sanitizeXmlInput($xml) {
    // Remove external entities
    $xml = removeExternalEntities($xml);
    
    // Disable external entity loading
    if (function_exists('libxml_disable_entity_loader')) {
        libxml_disable_entity_loader(true);
    }
    
    // Validate
    if (!validateNoExternalEntities($xml)) {
        throw new RuntimeException("External entities detected");
    }
    
    return $xml;
}

$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY external SYSTEM "file.xml">
]>
<root>&external;</root>';

try {
    $xml = sanitizeXmlInput($xml);
    echo "XML sanitized successfully";
} catch (RuntimeException $e) {
    echo "Error: " . $e->getMessage();
}
```

## Related Errors

- [XML_ERROR_ATTRIBUTE_EXTERNAL_ENTITY_REF](xml-error-attribute-external-entity-ref.md) - External entity in attribute
- [XML_ERROR_PARAM_ENTITY_REF](xml-error-param-entity-ref.md) - Parameter entity reference error
- [XML_ERROR_UNDEFINED_ENTITY](xml-error-undefined-entity.md) - Undefined entity reference