---
title: "[Solution] PHP RequestParseBodyException — Request Body Parse Failed"
description: "Fix PHP RequestParseBodyException by checking Content-Type headers, validating POST data, and handling malformed input."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 63
---

# RequestParseBodyException — Request Body Parse Failed

RequestParseBodyException is thrown when PHP cannot parse the incoming request body. This typically occurs with malformed JSON, invalid form-encoded data, or missing/mismatched Content-Type headers. This exception is commonly seen in frameworks like Symfony and PSR-based applications.

## Common Causes

```php
<?php
// Cause 1: Invalid JSON in request body
$json = '{"name": "test", "value": }'; // Trailing comma
$data = json_decode($json, true); // Returns null, may trigger exception in frameworks

// Cause 2: Content-Type header mismatch
// Header says application/json but body is form-encoded
$headers = $_SERVER['CONTENT_TYPE'] ?? '';
$body = file_get_contents('php://input');
$data = json_decode($body, true); // Fails if body is not JSON

// Cause 3: Malformed form data
// Body: "key1=value1&key2=" (incomplete encoding)
parse_str(file_get_contents('php://input'), $data); // May throw in strict mode

// Cause 4: Oversized request body
// upload_max_filesize or post_max_size exceeded

// Cause 5: Binary data in text expected body
$rawData = file_get_contents('php://input');
$json = json_decode($rawData, true); // JSON_ERROR_SYNTAX
?>
```

## How to Fix

### Fix 1: Validate Content-Type header

```php
<?php
function parseRequestBody(): array {
    $contentType = $_SERVER['CONTENT_TYPE'] ?? '';

    if (strpos($contentType, 'application/json') !== false) {
        $raw = file_get_contents('php://input');
        $data = json_decode($raw, true);

        if (json_last_error() !== JSON_ERROR_NONE) {
            throw new \InvalidArgumentException(
                "Invalid JSON: " . json_last_error_msg()
            );
        }

        return $data ?? [];
    }

    if (strpos($contentType, 'application/x-www-form-urlencoded') !== false) {
        parse_str(file_get_contents('php://input'), $data);
        return $data;
    }

    throw new \InvalidArgumentException("Unsupported Content-Type: $contentType");
}
?>
```

### Fix 2: Handle malformed JSON gracefully

```php
<?php
function safeJsonDecode(string $json): mixed {
    $data = json_decode($json, true);

    switch (json_last_error()) {
        case JSON_ERROR_NONE:
            return $data;
        case JSON_ERROR_SYNTAX:
            throw new \InvalidArgumentException("JSON syntax error");
        case JSON_ERROR_DEPTH:
            throw new \InvalidArgumentException("JSON nesting too deep");
        case JSON_ERROR_STATE_MISMATCH:
            throw new \InvalidArgumentException("JSON underflow or mode mismatch");
        case JSON_ERROR_CTRL_CHAR:
            throw new \InvalidArgumentException("JSON control character error");
        case JSON_ERROR_SYNTAX:
        default:
            throw new \InvalidArgumentException(
                "JSON error: " . json_last_error_msg()
            );
    }
}

try {
    $body = file_get_contents('php://input');
    $data = safeJsonDecode($body);
} catch (\InvalidArgumentException $e) {
    http_response_code(400);
    echo json_encode(['error' => $e->getMessage()]);
}
?>
```

### Fix 3: Configure PHP for request limits

```ini
; php.ini
upload_max_filesize = 10M
post_max_size = 12M
max_input_vars = 3000
max_execution_time = 30
```

```php
<?php
// Check if request body was truncated
if ($_SERVER['REQUEST_METHOD'] === 'POST' && empty(file_get_contents('php://input'))) {
    if (error_get_last()) {
        http_response_code(413);
        echo json_encode(['error' => 'Request body too large']);
    }
}
?>
```

## Examples

```php
<?php
// Complete request body parser with validation
function handleApiRequest(): array {
    $method = $_SERVER['REQUEST_METHOD'];
    $contentType = $_SERVER['CONTENT_TYPE'] ?? '';

    if ($method === 'GET') {
        return $_GET;
    }

    if (!in_array($method, ['POST', 'PUT', 'PATCH', 'DELETE'])) {
        throw new \RuntimeException("Unsupported method: $method");
    }

    if (strpos($contentType, 'application/json') === false) {
        throw new \InvalidArgumentException("Content-Type must be application/json");
    }

    $rawBody = file_get_contents('php://input');
    if (empty($rawBody)) {
        throw new \InvalidArgumentException("Empty request body");
    }

    $data = json_decode($rawBody, true);
    if (json_last_error() !== JSON_ERROR_NONE) {
        throw new \InvalidArgumentException(
            "JSON parse error: " . json_last_error_msg()
        );
    }

    return $data;
}

try {
    $request = handleApiRequest();
    http_response_code(200);
    echo json_encode(['status' => 'ok', 'data' => $request]);
} catch (\InvalidArgumentException $e) {
    http_response_code(400);
    echo json_encode(['error' => $e->getMessage()]);
}
?>
```

## Related Errors

- [PHP Warning]({{< relref "/languages/php/e-warning" >}}) — warning
- [PHP TypeError]({{< relref "/languages/php/typeerror" >}}) — type mismatch
- [PHP ValueError]({{< relref "/languages/php/valueerror" >}}) — invalid value
