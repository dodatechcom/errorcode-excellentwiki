---
title: "[Solution] PHP libxml Schema Validation Error"
description: "Fix PHP libxml schema validation error by validating against correct schema, checking schema syntax, and fixing XML structure. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 16
---

# PHP libxml Schema Validation Error

XML schema validation failed because the document does not conform to the specified XML Schema (XSD) or Relax NG schema. This occurs when required elements are missing, data types don't match, or the schema itself is invalid.

## Common Causes

```php
// Cause 1: Missing required element
$xml = '<root><name>John</name></root>';
// Schema requires <root><name/><age/></root>
$doc = new DOMDocument();
$doc->loadXML($xml);
$doc->schemaValidate('schema.xsd'); // Missing <age> element

// Cause 2: Invalid data type
$xml = '<root><age>not-a-number</age></root>';
// Schema defines <age> as xs:integer
$doc = new DOMDocument();
$doc->loadXML($xml);
$doc->schemaValidate('schema.xsd'); // Type mismatch

// Cause 3: Invalid schema file
$doc->newDOMDocument();
$doc->schemaValidate('nonexistent.xsd'); // Schema not found

// Cause 4: Namespace mismatch
$xml = '<ns:root xmlns:ns="http://wrong-ns.com"><ns:child/></ns:root>';
// Schema expects xmlns="http://correct-ns.com"

// Cause 5: Schema syntax error
// Invalid XSD file
```

## How to Fix

### Fix 1: Validate XML Against Schema with Error Details

```php
function validateAgainstSchema(string $xml, string $schemaPath): array {
    libxml_use_internal_errors(true);

    $doc = new DOMDocument();
    if (!$doc->loadXML($xml)) {
        $errors = libxml_get_errors();
        libxml_clear_errors();
        libxml_use_internal_errors(false);
        return ['valid' => false, 'errors' => ['XML parse failed']];
    }

    if (!file_exists($schemaPath)) {
        libxml_use_internal_errors(false);
        return ['valid' => false, 'errors' => ["Schema not found: {$schemaPath}"]];
    }

    $valid = $doc->schemaValidate($schemaPath);
    $errors = [];

    if (!$valid) {
        foreach (libxml_get_errors() as $error) {
            $errors[] = trim($error->message);
        }
    }

    libxml_clear_errors();
    libxml_use_internal_errors(false);

    return ['valid' => $valid, 'errors' => $errors];
}

// Usage
$result = validateAgainstSchema($xml, '/path/to/schema.xsd');
if (!$result['valid']) {
    print_r($result['errors']);
}
```

### Fix 2: Validate Schema File Itself

```php
function isSchemaValid(string $xsdPath): array {
    libxml_use_internal_errors(true);

    $doc = new DOMDocument();
    $valid = $doc->load($xsdPath);

    $errors = [];
    if (!$valid) {
        foreach (libxml_get_errors() as $error) {
            $errors[] = trim($error->message);
        }
    }

    libxml_clear_errors();
    libxml_use_internal_errors(false);

    return ['valid' => $valid, 'errors' => $errors];
}
```

### Fix 3: Use Relax NG as Alternative

```php
function validateWithRelaxNg(string $xml, string $rngPath): array {
    libxml_use_internal_errors(true);

    $doc = new DOMDocument();
    if (!$doc->loadXML($xml)) {
        libxml_clear_errors();
        libxml_use_internal_errors(false);
        return ['valid' => false, 'errors' => ['XML parse failed']];
    }

    $rngDoc = new DOMDocument();
    if (!$rngDoc->load($rngPath)) {
        libxml_clear_errors();
        libxml_use_internal_errors(false);
        return ['valid' => false, 'errors' => ['RNG schema not found']];
    }

    $valid = $doc->relaxNGValidate($rngDoc);
    $errors = [];

    if (!$valid) {
        foreach (libxml_get_errors() as $error) {
            $errors[] = trim($error->message);
        }
    }

    libxml_clear_errors();
    libxml_use_internal_errors(false);

    return ['valid' => $valid, 'errors' => $errors];
}
```

## Examples

```php
// Example: Complete schema validation workflow
function validateXmlDocument(string $xml, string $schemaPath): array {
    $result = [
        'valid' => false,
        'errors' => [],
        'warnings' => [],
    ];

    libxml_use_internal_errors(true);

    // Step 1: Check schema exists
    if (!file_exists($schemaPath)) {
        $result['errors'][] = "Schema file not found: {$schemaPath}";
        libxml_use_internal_errors(false);
        return $result;
    }

    // Step 2: Parse XML
    $doc = new DOMDocument();
    if (!$doc->loadXML($xml)) {
        foreach (libxml_get_errors() as $error) {
            $result['errors'][] = "Parse error at line {$error->line}: " . trim($error->message);
        }
        libxml_clear_errors();
        libxml_use_internal_errors(false);
        return $result;
    }

    // Step 3: Validate against schema
    $valid = $doc->schemaValidate($schemaPath);

    if (!$valid) {
        foreach (libxml_get_errors() as $error) {
            $msg = trim($error->message);
            if ($error->level === LIBXML_ERR_WARNING) {
                $result['warnings'][] = $msg;
            } else {
                $result['errors'][] = "Validation at line {$error->line}: {$msg}";
            }
        }
    } else {
        $result['valid'] = true;
    }

    libxml_clear_errors();
    libxml_use_internal_errors(false);

    return $result;
}

// Usage
$xml = '<root><name>John</name><age>30</age></root>';
$result = validateXmlDocument($xml, 'schema.xsd');
if ($result['valid']) {
    echo 'XML is valid';
} else {
    print_r($result['errors']);
}
```

## Related Errors

- [libxml error](/languages/php/libxml-error/)
- [libxml parsing error](/languages/php/libxml-parse-error/)
- [libxml entity error](/languages/php/libxml-entity-error/)
