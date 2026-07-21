---
title: "[Solution] Laravel Guzzle Request Exception Error"
description: "Fix Laravel Guzzle ClientException and ServerException errors. Resolve HTTP request failures with Guzzle in Laravel."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

This error is thrown when Guzzle (or Laravel's `Http` facade) receives a 4xx or 5xx response and throws a `RequestException`.

## Common Causes

- Target API returns 400 Bad Request due to malformed payload
- API key or authorization token is invalid or expired
- Rate limit exceeded (429 Too Many Requests)
- Server error (500) on the remote API
- Content-Type header missing or incorrect

## How to Fix

1. Wrap requests in try-catch blocks:

```php
use GuzzleHttp\Exception\ClientException;
use GuzzleHttp\Exception\ServerException;

try {
    $response = Http::post('https://api.example.com/orders', $data);
} catch (ClientException $e) {
    $status = $e->getResponse()->getStatusCode();
    $body = $e->getResponse()->getBody()->getContents();
    Log::error("API client error {$status}: {$body}");
} catch (ServerException $e) {
    Log::error('Remote server error: ' . $e->getMessage());
}
```

2. Check the response before processing:

```php
$response = Http::post('https://api.example.com/orders', $data);

if ($response->failed()) {
    Log::error('Order API failed', [
        'status' => $response->status(),
        'body' => $response->body(),
    ]);
}
```

3. Implement exponential backoff for transient errors:

```php
Http::retry(3, function ($exception) {
    return $exception->response->status() >= 500;
})->post('https://api.example.com/orders', $data);
```

## Examples

```php
// 401 Unauthorized from external API
Http::withToken('expired-token')
    ->get('https://api.example.com/account');
// ClientException: 401 Unauthorized

// 422 Validation error from API
Http::post('https://api.example.com/customers', $invalidData);
// ClientException: 422 Unprocessable Entity {"errors":{"email":["required"]}}
```
