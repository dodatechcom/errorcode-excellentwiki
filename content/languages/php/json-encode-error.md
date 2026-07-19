---
title: "[Solution] PHP JSON Encode Error — Malformed UTF-8 Characters"
description: "Fix PHP JSON encode errors caused by malformed UTF-8 characters. Resolve encoding issues with json_encode and multibyte strings."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "php"
tags: ["php", "json", "encoding"]
severity: "error"
---

# PHP JSON Encode Error

## Error Message

```
json_encode(): Malformed UTF-8 characters, possibly incorrectly encoded
```

## Common Causes

- The data contains byte sequences that are not valid UTF-8 (e.g., from Latin-1 or Windows-1252 sources)
- Database columns with mixed encodings or binary data stored in text fields
- User input submitted from forms using a non-UTF-8 charset

## Solutions

### Solution 1: Sanitize Input with mb_convert_encoding

Convert invalid byte sequences to their closest UTF-8 equivalents before encoding.

```php
<?php
function sanitizeUtf8(mixed $data): mixed {
    if (is_string($data)) {
        // Replace invalid UTF-8 sequences with the Unicode replacement character
        return mb_convert_encoding($data, 'UTF-8', 'UTF-8');
    }
    if (is_array($data)) {
        return array_map('sanitizeUtf8', $data);
    }
    return $data;
}

// Usage
$dirtyData = ['name' => "Café", 'notes' => "Price: 10 EUR"];
$sanitized = sanitizeUtf8($dirtyData);
$json = json_encode($sanitized, JSON_THROW_ON_ERROR);
echo $json;
// {"name":"Café","notes":"Price: 10 EUR"}
?>
```

### Solution 2: Use JSON_THROW_ON_ERROR for Explicit Error Handling

Enable the JSON_THROW_ON_ERROR flag to catch encoding failures immediately instead of silently returning null.

```php
<?php
function safeJsonEncode(mixed $data): string {
    $json = json_encode($data, JSON_THROW_ON_ERROR | JSON_UNESCAPED_UNICODE);
    return $json;
}

// Usage with error handling
try {
    $response = safeJsonEncode([
        'status'  => 'ok',
        'payload' => $userInput,
    ]);
    header('Content-Type: application/json; charset=utf-8');
    echo $response;
} catch (JsonException $e) {
    error_log("JSON encode failed: " . $e->getMessage());
    http_response_code(500);
    echo json_encode(['error' => 'Invalid data encoding']);
}
?>
```

## Prevention Tips

- Set the database connection charset to UTF-8 (e.g., `SET NAMES utf8mb4`)
- Validate and sanitize user input before storing or encoding it
- Use JSON_THROW_ON_ERROR in PHP 7.3+ to catch issues early

## Related Errors

- [Json Decode Error]({{< relref "/languages/php/json-decode-error" >}})
- [Mbstring Error]({{< relref "/languages/php/mbstring-error" >}})
