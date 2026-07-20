---
title: "[Solution] PHP Warning: json_decode() — Invalid JSON"
description: "Fix PHP Warning: json_decode() Invalid JSON. Validate JSON format, check encoding, use json_last_error()."
languages: ["php"]
severities: ["warning"]
error-types: ["runtime-error"]
weight: 103
---

# PHP Warning: json_decode() — Invalid JSON

This warning indicates that `json_decode()` received a string that is not valid JSON. The function returns `null` when parsing fails, and in PHP 8.3+ a warning is emitted. Invalid JSON typically results from malformed data, incorrect encoding, or unescaped characters.

## Common Causes

```php
// Cause 1: Malformed JSON string
<?php
$json = '{name: "Alice"}'; // Missing quotes around key
$data = json_decode($json);
// Warning: json_decode(): Invalid JSON
?>
```

```php
// Cause 2: Trailing commas in JSON
<?php
$json = '{"name": "Alice", "age": 30,}';
$data = json_decode($json);
// Invalid — trailing comma is not allowed
?>
```

```php
// Cause 3: Encoding issues with non-UTF-8 characters
<?php
$json = '{"name": "Jos\xe9"}'; // Latin-1 encoded
$data = json_decode($json);
// Encoding mismatch causes failure
?>
```

```php
// Cause 4: Double-encoded JSON
<?php
$json = '{"data": "{\\"name\\": \\"Alice\\"}"}';
$data = json_decode($json);
// Outer layer decodes fine but inner string is still JSON
?>
```

```php
// Cause 5: Single quotes instead of double quotes
<?php
$json = "{'name': 'Alice'}"; // PHP strings allow single quotes
$data = json_decode($json);
// JSON spec requires double quotes
?>
```

## How to Fix

### Fix 1: Validate JSON Before Decoding

Check the format of the JSON string before calling `json_decode()`.

```php
<?php
$jsonString = '{"name": "Alice", "age": 30}';

// Validate using json_decode + json_last_error
$result = json_decode($jsonString, true);
if (json_last_error() !== JSON_ERROR_NONE) {
    die("Invalid JSON: " . json_last_error_msg());
}

// Use $result safely
echo $result['name'];
?>
```

### Fix 2: Check and Handle Encoding

Ensure the JSON string is valid UTF-8 before decoding.

```php
<?php
function safeJsonDecode(string $json, bool $assoc = true): mixed
{
    // Check for valid UTF-8 encoding
    if (mb_check_encoding($json, 'UTF-8') === false) {
        $json = mb_convert_encoding($json, 'UTF-8', 'ISO-8859-1');
    }

    // Remove BOM if present
    $json = preg_replace('/^\xEF\xBB\xBF/', '', $json);

    $data = json_decode($json, $assoc);
    if (json_last_error() !== JSON_ERROR_NONE) {
        throw new \RuntimeException(
            "JSON decode error: " . json_last_error_msg()
        );
    }

    return $data;
}

try {
    $data = safeJsonDecode($responseBody);
} catch (\RuntimeException $e) {
    echo "Parse failed: " . $e->getMessage();
}
?>
```

### Fix 3: Use json_last_error() for Detailed Diagnostics

Always check the last JSON error after decoding.

```php
<?php
$json = '{"incomplete": "data"';

$data = json_decode($json, true);

switch (json_last_error()) {
    case JSON_ERROR_NONE:
        echo "No error\n";
        break;
    case JSON_ERROR_SYNTAX:
        echo "Syntax error in JSON\n";
        break;
    case JSON_ERROR_UTF8:
        echo "Malformed UTF-8 characters\n";
        break;
    case JSON_ERROR_DEPTH:
        echo "Maximum stack depth exceeded\n";
        break;
    case JSON_ERROR_STATE_MISMATCH:
        echo "Underflow or mismatch of state\n";
        break;
    case JSON_ERROR_CTRL_CHAR:
        echo "Unexpected control character\n";
        break;
    case JSON_ERROR_RECURSION:
        echo "Recursion detected\n";
        break;
    case JSON_ERROR_INF_OR_NAN:
        echo "INF or NaN values\n";
        break;
    case JSON_ERROR_UNSUPPORTED_TYPE:
        echo "Unsupported type\n";
        break;
    case JSON_ERROR_INVALID_PROPERTY_NAME:
        echo "Invalid property name\n";
        break;
    case JSON_ERROR_SYNTAX:
        echo "Syntax error\n";
        break;
    default:
        echo "Unknown error: " . json_last_error() . "\n";
        break;
}
?>
```

### Fix 4: Fix Trailing Commas and Malformed Structures

Sanitize JSON strings to remove common formatting issues.

```php
<?php
function sanitizeJson(string $json): string
{
    // Remove single-line comments (not part of JSON spec)
    $json = preg_replace('/\/\/[^\n]*/', '', $json);

    // Remove multi-line comments
    $json = preg_replace('/\/\*.*?\*\//s', '', $json);

    // Remove trailing commas before } or ]
    $json = preg_replace('/,\s*([\]}])/', '$1', $json);

    return $json;
}

$messyJson = '{"name": "Alice", /* comment */ "age": 30,}';
$cleanJson = sanitizeJson($messyJson);
$data = json_decode($cleanJson, true);
// Now decodes successfully
?>
```

## Examples

```php
<?php
// Complete JSON handling for API responses
function parseApiJson(string $response): array
{
    if (empty(trim($response))) {
        throw new \InvalidArgumentException("Empty response body");
    }

    $data = json_decode($response, true, 512, JSON_THROW_ON_ERROR);
    return $data;
}

try {
    $response = file_get_contents("https://api.example.com/data");
    $parsed = parseApiJson($response);
    print_r($parsed);
} catch (\JsonException $e) {
    echo "JSON Error: " . $e->getMessage();
}
?>
```

```php
<?php
// JSON encoding with error handling
$data = ['name' => 'Alice', 'active' => true];
$json = json_encode($data, JSON_THROW_ON_ERROR | JSON_UNESCAPED_UNICODE);

// Validate round-trip
$decoded = json_decode($json, true);
if (json_last_error() !== JSON_ERROR_NONE) {
    echo "Round-trip validation failed";
}
?>
```

## Related Errors

- [PHP JSON Encode Error](/languages/php/json-encode-error)
- [PHP JSON Decode Error](/languages/php/json-decode-error)
- [PHP Warning: Undefined Index](/languages/php/notice-undefined-index)
