---
title: "[Solution] Laravel HTTP Client Connection Error"
description: "Fix Laravel HTTP client Guzzle connection errors. Resolve cURL error 60 SSL certificate problems in Laravel."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

This error occurs when the `Http` facade or Guzzle HTTP client fails to connect to an external API due to network, SSL, or configuration issues.

## Common Causes

- SSL certificate verification fails (self-signed cert, missing CA bundle)
- DNS resolution failure for the target host
- Firewall or proxy blocking outbound requests
- cURL extension not installed or outdated
- Request timeout is too short for slow APIs

## How to Fix

1. Install or update the cURL extension:

```bash
# Ubuntu/Debian
sudo apt-get install php-curl

# Verify installation
php -m | grep curl
```

2. For self-signed certificates in development:

```php
$response = Http::withOptions([
    'verify' => false, // disable only in development
])->get('https://internal-api.example.com/data');
```

3. Set appropriate timeouts:

```php
$response = Http::timeout(30)
    ->retry(3, 1000)
    ->post('https://api.example.com/webhook', $payload);
```

4. Configure a proxy if needed:

```php
$response = Http::withOptions([
    'proxy' => 'http://proxy.example.com:8080',
])->get('https://api.example.com/data');
```

## Examples

```php
// SSL error with self-signed certificate
Http::get('https://dev-api.internal/v1/users');
// cURL error 60: SSL certificate problem: self-signed certificate

// Timeout when API is slow
Http::timeout(5)->post('https://api.slow.com/process', $data);
// ConnectionException: cURL error 28: Operation timed out
```
