---
title: "[Solution] PHP XML_ERROR_ATTRIBUTE_EXTERNAL_ENTITY_REF — External Entity in Attribute"
description: "Fix PHP XML_ERROR_ATTRIBUTE_EXTERNAL_ENTITY_REF by disabling external entities, using internal entities, and validating input. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 16
---

# PHP XML_ERROR_ATTRIBUTE_EXTERNAL_ENTITY_REF — External Entity in Attribute

XML_ERROR_ATTRIBUTE_EXTERNAL_ENTITY_REF occurs when an external entity is referenced within an XML attribute. External entities can load content from files or URLs, which is a security risk (XXE attack). Many XML parsers disable external entity loading by default for security reasons.

## Common Causes

```php
// External entity in attribute
$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY external SYSTEM "file:///etc/passwd">
]>
<root attr="&external;"/>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_ATTRIBUTE_EXTERNAL_ENTITY_REF
```

```php
// URL-based external entity
$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY remote SYSTEM "http://example.com/data.xml">
]>
<root attr="&remote;"/>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_ATTRIBUTE_EXTERNAL_ENTITY_REF
```

```php
// Parameter external entity
$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY % file SYSTEM "file:///etc/passwd">
    <!ENTITY % eval "<!ENTITY exfil SYSTEM '%file;'>">
]>
<root attr="&exfil;"/>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_ATTRIBUTE_EXTERNAL_ENTITY_REF
```

```php
// FTP-based external entity
$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY ftpdata SYSTEM "ftp://example.com/data.txt">
]>
<root attr="&ftpdata;"/>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_ATTRIBUTE_EXTERNAL_ENTITY_REF
```

```php
// File path in attribute
$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY localfile SYSTEM "file:///tmp/data.xml">
]>
<root attr="&localfile;"/>';
$parser = xml_parser_create();
xml_parse($parser, $xml); // XML_ERROR_ATTRIBUTE_EXTERNAL_ENTITY_REF
```

## How to Fix

### Fix 1: Disable External Entities

Configure the parser to reject external entities:

```php
$parser = xml_parser_create();
xml_parser_set_option($parser, XML_OPTION_CASE_FOLDING, false);

// Disable external entity loading
xml_set_object($parser, $parser);

// For libxml-based parsers
libxml_disable_entity_loader(true);
```

### Fix 2: Use Internal Entities

Replace external entities with internal definitions:

```php
// Bad: External entity
$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY external SYSTEM "file:///etc/passwd">
]>
<root attr="&external;"/>';

// Good: Internal entity
$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY internal "safe content">
]>
<root attr="&internal;"/>';
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
    <!ENTITY external SYSTEM "file:///etc/passwd">
]>
<root attr="&external;"/>';

if (containsExternalEntities($xml)) {
    echo "External entities detected - security risk";
}
```

### Fix 4: Remove External Entity Definitions

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
    <!ENTITY external SYSTEM "file:///etc/passwd">
]>
<root attr="&external;"/>';

$xml = removeExternalEntities($xml);
```

### Fix 5: Use Safe Parser Configuration

Configure parser with security in mind:

```php
function safeXmlParse($xml) {
    // Disable external entities
    libxml_disable_entity_loader(true);
    
    // Remove external entities
    $xml = removeExternalEntities($xml);
    
    $parser = xml_parser_create();
    xml_parse($parser, $xml);
    $error = xml_get_error_code($parser);
    xml_parser_free($parser);
    
    return $error === XML_ERROR_NONE;
}
```

## Examples

```php
// Basic external entity detection
$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY external SYSTEM "file:///etc/passwd">
]>
<root attr="&external;"/>';
$parser = xml_parser_create();
xml_parse($parser, $xml);
$error = xml_get_error_code($parser);
if ($error === XML_ERROR_ATTRIBUTE_EXTERNAL_ENTITY_REF) {
    echo "External entity in attribute detected";
}
xml_parser_free($parser);
```

```php
// Secure XML parsing
function secureXmlParse($xml) {
    // Disable external entities
    libxml_disable_entity_loader(true);
    
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
    <!ENTITY external SYSTEM "file:///etc/passwd">
]>
<root attr="&external;"/>';

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
<root attr="&internal;"/>';

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
    libxml_disable_entity_loader(true);
    
    // Validate
    if (!validateNoExternalEntities($xml)) {
        throw new RuntimeException("External entities detected");
    }
    
    return $xml;
}

$xml = '<?xml version="1.0"?>
<!DOCTYPE root [
    <!ENTITY external SYSTEM "file:///etc/passwd">
]>
<root attr="&external;"/>';

try {
    $xml = sanitizeXmlInput($xml);
    echo "XML sanitized successfully";
} catch (RuntimeException $e) {
    echo "Error: " . $e->getMessage();
}
```

## Related Errors

- [XML_ERROR_PARAM_ENTITY_REF](xml-error-param-entity-ref.md) - Parameter entity reference error
- [XML_ERROR_UNDEFINED_ENTITY](xml-error-undefined-entity.md) - Undefined entity reference
- [XML_ERROR_EXTERNAL_ENTITY_HANDLING](xml-error-external-entity-handling.md) - Error handling external entities