---
title: "[Solution] PHP http_response_code() — Invalid Status Code or Headers Already Sent"
description: "Fix PHP http_response_code() issues: invalid status code, headers already sent. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 1100
---

# PHP http_response_code() — Invalid Status Code or Headers Already Sent

The `http_response_code()` function sets or returns the HTTP response code for the current request. Errors occur when you pass an invalid status code or attempt to set it after output has already been sent to the client.

## Common Causes

```php
<?php
// Passing an invalid status code
http_response_code(999); // Warning: invalid status code

// Trying to set after output has been sent
echo "Hello";
http_response_code(404); // Warning: headers already sent

// Passing a non-integer value
http_response_code("not-a-number"); // Warning: expects int

// Negative status code
http_response_code(-1); // Warning: invalid status code
```

## How to Fix

### Fix 1: Use Valid HTTP Status Codes

```php
<?php
// Valid 1xx informational
http_response_code(100); // Continue
http_response_code(101); // Switching Protocols

// Valid 2xx success
http_response_code(200); // OK
http_response_code(201); // Created
http_response_code(204); // No Content

// Valid 3xx redirection
http_response_code(301); // Moved Permanently
http_response_code(302); // Found
http_response_code(304); // Not Modified

// Valid 4xx client errors
http_response_code(400); // Bad Request
http_response_code(401); // Unauthorized
http_response_code(403); // Forbidden
http_response_code(404); // Not Found

// Valid 5xx server errors
http_response_code(500); // Internal Server Error
http_response_code(502); // Bad Gateway
http_response_code(503); // Service Unavailable
```

### Fix 2: Set Response Code Before Any Output

```php
<?php
// Correct order: headers first, then output
http_response_code(200);
header('Content-Type: application/json');
echo json_encode(['status' => 'success']);

// For API responses, always set code first
http_response_code(201);
header('Content-Type: application/json');
echo json_encode(['id' => 123, 'message' => 'Created']);
```

### Fix 3: Use Output Buffering When Order Cannot Be Guaranteed

```php
<?php
ob_start();

// Code that may or may not produce output
echo "Processing...";

// Later, change the response code
if ($error) {
    http_response_code(500);
    echo json_encode(['error' => 'Something went wrong']);
}

// Output is buffered, so headers are still modifiable
ob_end_flush();
```

### Fix 4: Check Return Value for Debugging

```php
<?php
$previousCode = http_response_code(404);

if ($previousCode === false) {
    // http_response_code() returned false — invalid code or headers already sent
    error_log("Failed to set HTTP response code");
    // Check: was the code valid? Were headers already sent?
    if (headers_sent()) {
        error_log("Headers already sent at " . headers_list());
    }
}

// Verify the code was set
$currentCode = http_response_code();
// $currentCode should now be 404
```

## Examples

```php
<?php
// Example 1: REST API response codes
function handleApiRequest(array $request): void
{
    if (!isset($request['id'])) {
        http_response_code(400);
        echo json_encode(['error' => 'Missing required parameter: id']);
        return;
    }

    $user = findUser($request['id']);

    if ($user === null) {
        http_response_code(404);
        echo json_encode(['error' => 'User not found']);
        return;
    }

    http_response_code(200);
    echo json_encode($user);
}

// Example 2: Conditional response codes
function streamFile(string $path): void
{
    if (!file_exists($path)) {
        http_response_code(404);
        echo 'File not found';
        return;
    }

    http_response_code(200);
    header('Content-Type: application/octet-stream');
    header('Content-Disposition: attachment; filename="' . basename($path) . '"');
    readfile($path);
}

// Example 3: Chaining with header()
function redirectToLogin(): void
{
    http_response_code(302);
    header('Location: /login');
    exit;
}
```

## Related Errors

- [PHP Headers Already Sent]({{< relref "/languages/php/headers-sent" >}})
- [PHP Warning: Cannot Modify Header Information]({{< relref "/languages/php/warning-header-sent" >}})
- [PHP cURL HTTP Error]({{< relref "/languages/php/curl-http-error" >}})
