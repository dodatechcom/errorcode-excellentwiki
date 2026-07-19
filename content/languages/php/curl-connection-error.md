---
title: "[Solution] PHP cURL Failed to Connect"
description: "Fix cURL error 7: Failed to connect to host. Learn to diagnose and resolve connection failures in PHP cURL requests."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "php"
tags: ["php", "curl", "connection", "network", "firewall"]
severity: "error"
---

# cURL Error 7: Failed to Connect

## Error Message

```
cURL error 7: Failed to connect to api.example.com port 443 after 10002 milliseconds: Connection refused
```

## Common Causes

- The remote server is not running or the port is closed
- A firewall or security group blocks the outgoing connection
- The hostname resolves to an incorrect IP address
- The server is listening on a different port than expected

## Solutions

### Solution 1: Verify the Target Host and Port

Confirm the server is reachable and listening on the expected port before debugging PHP code.

```php
<?php
$url = 'https://api.example.com/data';

// Test connectivity first
$parsedUrl = parse_url($url);
$host = $parsedUrl['host'];
$port = $parsedUrl['port'] ?? ($parsedUrl['scheme'] === 'https' ? 443 : 80);

$connection = @fsockopen($host, $port, $errno, $errstr, 5);
if ($connection) {
    fclose($connection);
    echo "Connection to $host:$port successful";
} else {
    echo "Cannot connect to $host:$port — $errstr ($errno)";
}
?>
```

### Solution 2: Set cURL Options for Reliable Connections

Configure cURL with proper options to handle connection issues gracefully.

```php
<?php
$ch = curl_init('https://api.example.com/data');

curl_setopt_array($ch, [
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_CONNECTTIMEOUT => 10,
    CURLOPT_TIMEOUT        => 30,
    CURLOPT_FOLLOWLOCATION => true,
    CURLOPT_MAXREDIRS      => 5,
    CURLOPT_HTTPHEADER     => [
        'Connection: keep-alive',
        'Accept: application/json',
    ],
]);

$response = curl_exec($ch);
if (curl_errno($ch)) {
    $error = curl_error($ch);
    $errno = curl_errno($ch);
    error_log("cURL Error $errno: $error");
}
curl_close($ch);
?>
```

## Prevention Tips

- Use `telnet` or `nc` to verify port connectivity from the server
- Check cloud provider security group and firewall rules
- Ensure the server DNS resolves to a routable IP address

## Related Errors

- [cURL DNS Resolution Error]({{< relref "/languages/php/curl-dns-error" >}})
- [cURL Timeout Error]({{< relref "/languages/php/curl-timeout-error" >}})
