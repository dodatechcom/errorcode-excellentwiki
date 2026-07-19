---
title: "[Solution] PHP JSON Decode Error — Syntax Error, Malformed JSON"
description: "Fix PHP JSON decode errors. Resolve 'Syntax error, malformed JSON' with proper validation and error handling."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "php"
tags: ["php", "json", "parsing"]
severity: "error"
---

# PHP JSON Decode Error

## Error Message

```
json_decode(): Syntax error, malformed JSON
```

## Common Causes

- The JSON string contains trailing commas, which are not valid in strict JSON
- The input is empty, null, or not a JSON string at all
- Double-quoted strings contain unescaped special characters (backslashes, quotes)

## Solutions

### Solution 1: Validate JSON Before Decoding

Check whether the string is valid JSON before attempting to decode it.

```php
<?php
function safeJsonDecode(string $json): mixed {
    $decoded = json_decode($json, null, 512, JSON_THROW_ON_ERROR);
    return $decoded;
}

// Usage
$input = file_get_contents('php://input');

try {
    $data = safeJsonDecode($input);
    // Process $data
    header('Content-Type: application/json');
    echo json_encode(['status' => 'ok', 'received' => $data]);
} catch (JsonException $e) {
    http_response_code(400);
    echo json_encode([
        'error'   => 'Invalid JSON',
        'message' => $e->getMessage(),
    ]);
}
?>
```

### Solution 2: Handle Common Malformed JSON Patterns

Attempt to fix common JSON issues like trailing commas before decoding.

```php
<?php
function lenientJsonDecode(string $json): mixed {
    // Strip trailing commas before ] or }
    $cleaned = preg_replace('/,\s*([\]\}])/', '$1', $json);

    // Strip BOM and whitespace
    $cleaned = ltrim($cleaned, "\x{FEFF}");

    $result = json_decode($cleaned, true, 512, JSON_THROW_ON_ERROR);
    return $result;
}

// Usage
$raw = '{"users": [{"name": "Alice",}, {"name": "Bob",},]}';
try {
    $data = lenientJsonDecode($raw);
    print_r($data);
} catch (JsonException $e) {
    echo "Still invalid after cleanup: " . $e->getMessage();
}
?>
```

## Prevention Tips

- Always validate JSON input from external APIs and user submissions
- Use JSON_THROW_ON_ERROR to convert decode failures into exceptions
- Return HTTP 400 Bad Request for invalid JSON in API endpoints

## Related Errors

- [Json Encode Error]({{< relref "/languages/php/json-encode-error" >}})
- [Pcre Error]({{< relref "/languages/php/pcre-error" >}})
