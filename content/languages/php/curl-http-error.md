---
title: "[Solution] PHP cURL HTTP Error Response"
description: "Fix cURL error 22: HTTP error response. Learn to handle non-2xx HTTP status codes and error responses in PHP cURL."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "php"
tags: ["php", "curl", "http", "status-code", "api"]
severity: "error"
---

# cURL Error 22: HTTP Error

## Error Message

```
cURL error 22: The requested URL returned error: 403 Forbidden
```

## Common Causes

- The server returned a non-2xx HTTP status code (4xx or 5xx)
- CURLOPT_FAILONERROR is enabled and the server returned an error page
- Missing or incorrect authentication headers (API key, token)
- The server requires specific Content-Type or Accept headers

## Solutions

### Solution 1: Handle HTTP Errors Manually

Disable CURLOPT_FAILONERROR so you can inspect the full response body and handle errors programmatically.

```php
<?php
$ch = curl_init('https://api.example.com/data');
curl_setopt_array($ch, [
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_FAILONERROR    => false,
    CURLOPT_TIMEOUT        => 30,
    CURLOPT_HTTPHEADER     => [
        'Authorization: Bearer your-api-token',
        'Accept: application/json',
    ],
]);

$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

if ($httpCode >= 400) {
    echo "HTTP Error $httpCode: $response";
} else {
    $data = json_decode($response, true);
    // Process the data
}
?>
```

### Solution 2: Create a Robust cURL Wrapper

Build a reusable cURL wrapper that handles HTTP errors, retries, and logging consistently.

```php
<?php
class HttpClient
{
    public static function request(
        string $method,
        string $url,
        array $headers = [],
        string $body = ''
    ): array {
        $ch = curl_init($url);
        curl_setopt_array($ch, [
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_FAILONERROR    => false,
            CURLOPT_TIMEOUT        => 30,
            CURLOPT_CUSTOMREQUEST  => $method,
            CURLOPT_HTTPHEADER     => $headers,
        ]);

        if ($body !== '') {
            curl_setopt($ch, CURLOPT_POSTFIELDS, $body);
        }

        $response = curl_exec($ch);
        $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
        $error = curl_error($ch);
        curl_close($ch);

        return [
            'status' => $httpCode,
            'body'   => $response,
            'error'  => $error,
        ];
    }
}

$result = HttpClient::request('GET', 'https://api.example.com/data', [
    'Authorization: Bearer token',
    'Accept: application/json',
]);

if ($result['status'] >= 400) {
    error_log("API returned HTTP {$result['status']}");
}
?>
```

## Prevention Tips

- Always check the HTTP status code after curl_exec()
- Log both the status code and response body for debugging
- Implement exponential backoff for 5xx server errors

## Related Errors

- [cURL SSL Certificate Error]({{< relref "/languages/php/curl-ssl-error" >}})
- [cURL POST Error]({{< relref "/languages/php/curl-post-error" >}})
