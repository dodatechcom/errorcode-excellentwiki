---
title: "[Solution] PHP cURL Connection Timed Out"
description: "Fix cURL error 28: Connection timed out. Learn to set proper timeouts and handle slow connections in PHP cURL requests."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "php"
tags: ["php", "curl", "timeout", "network", "connection"]
severity: "error"
---

# cURL Error 28: Connection Timed Out

## Error Message

```
cURL error 28: Operation timed out after 30001 milliseconds with 0 bytes received
```

## Common Causes

- The remote server is unreachable or overloaded
- Network firewall rules block the outgoing connection
- No timeout is configured and the default limit is reached
- DNS resolution is slow or the host is temporarily unavailable

## Solutions

### Solution 1: Set Explicit Timeout Values

Configure both connection and total timeout values so cURL does not hang indefinitely.

```php
<?php
$ch = curl_init('https://api.example.com/data');

// Maximum time in seconds the request is allowed to take
curl_setopt($ch, CURLOPT_TIMEOUT, 30);

// Time in seconds to wait while trying to connect
curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 10);

$response = curl_exec($ch);
if (curl_errno($ch)) {
    echo 'Error: ' . curl_error($ch);
}
curl_close($ch);
?>
```

### Solution 2: Implement Retry Logic with Exponential Backoff

Automatically retry failed requests with increasing delays to handle transient network issues.

```php
<?php
function curlRequestWithRetry(string $url, int $maxRetries = 3): string|false
{
    $delay = 1;

    for ($attempt = 1; $attempt <= $maxRetries; $attempt++) {
        $ch = curl_init($url);
        curl_setopt_array($ch, [
            CURLOPT_TIMEOUT         => 30,
            CURLOPT_CONNECTTIMEOUT  => 10,
            CURLOPT_RETURNTRANSFER  => true,
        ]);

        $response = curl_exec($ch);
        $errno = curl_errno($ch);
        curl_close($ch);

        if (!$errno) {
            return $response;
        }

        if ($attempt < $maxRetries) {
            sleep($delay);
            $delay *= 2;
        }
    }

    return false;
}

$result = curlRequestWithRetry('https://api.example.com/data');
?>
```

## Prevention Tips

- Always set CURLOPT_CONNECTTIMEOUT to prevent indefinite blocking
- Use CURLOPT_TIMEOUT for the total request duration including data transfer
- Monitor slow endpoints and consider caching responses locally

## Related Errors

- [cURL Connection Error]({{< relref "/languages/php/curl-connection-error" >}})
- [cURL DNS Resolution Error]({{< relref "/languages/php/curl-dns-error" >}})
