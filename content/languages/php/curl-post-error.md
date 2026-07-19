---
title: "[Solution] PHP cURL URL Using Bad/Illegal Format"
description: "Fix cURL error 3: URL using bad/illegal format. Learn to validate and sanitize URLs before making PHP cURL requests."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "php"
tags: ["php", "curl", "url", "post", "validation"]
severity: "error"
---

# cURL Error 3: URL Using Bad/Illegal Format

## Error Message

```
cURL error 3: URL using bad/illegal format or no URL was supplied
```

## Common Causes

- The URL contains illegal characters or unencoded spaces
- The URL is missing the scheme (http:// or https://)
- The URL string was constructed from user input without sanitization
- CURLOPT_URL was set to an empty string or null value

## Solutions

### Solution 1: Validate and Sanitize URLs Before Use

Always validate the URL format and ensure it contains a valid scheme before passing it to cURL.

```php
<?php
function validateUrl(string $url): string
{
    $url = trim($url);

    if (empty($url)) {
        throw new InvalidArgumentException('URL cannot be empty');
    }

    if (!filter_var($url, FILTER_VALIDATE_URL)) {
        throw new InvalidArgumentException("Invalid URL format: $url");
    }

    $parsed = parse_url($url);
    if (!isset($parsed['scheme']) || !in_array($parsed['scheme'], ['http', 'https'], true)) {
        throw new InvalidArgumentException("URL must use http or https scheme: $url");
    }

    return $url;
}

$userInput = 'https://api.example.com/search?q=test&page=1';
$safeUrl = validateUrl($userInput);

$ch = curl_init($safeUrl);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
$response = curl_exec($ch);
curl_close($ch);
?>
```

### Solution 2: Build URLs Safely with http_build_query

Construct URLs with query parameters using PHP's built-in functions to avoid illegal character issues.

```php
<?php
$baseUrl = 'https://api.example.com/search';

$params = [
    'q'    => 'php cURL error',
    'page' => 1,
    'limit' => 20,
];

$url = $baseUrl . '?' . http_build_query($params);

$ch = curl_init($url);
curl_setopt_array($ch, [
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_TIMEOUT        => 30,
]);

$response = curl_exec($ch);
if (curl_errno($ch)) {
    echo 'Error: ' . curl_error($ch);
}
curl_close($ch);
?>
```

## Prevention Tips

- Always use http_build_query() to encode query parameters
- Validate URLs with filter_var() before passing to cURL
- Never concatenate user input directly into URLs without encoding

## Related Errors

- [cURL HTTP Error]({{< relref "/languages/php/curl-http-error" >}})
- [cURL Connection Error]({{< relref "/languages/php/curl-connection-error" >}})
