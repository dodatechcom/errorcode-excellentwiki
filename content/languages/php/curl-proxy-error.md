---
title: "[Solution] PHP cURL Couldn't Resolve Proxy"
description: "Fix cURL error 5: Couldn't resolve proxy. Learn to configure proxy settings correctly in PHP cURL requests."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "php"
tags: ["php", "curl", "proxy", "network", "firewall"]
severity: "error"
---

# cURL Error 5: Couldn't Resolve Proxy

## Error Message

```
cURL error 5: Couldn't resolve proxy 'proxy.example.com:8080'
```

## Common Causes

- The proxy hostname is misspelled or the DNS cannot resolve it
- The proxy server is offline or unreachable
- The proxy configuration contains an invalid port number
- HTTP_PROXY or HTTPS_PROXY environment variables contain incorrect values

## Solutions

### Solution 1: Verify Proxy Configuration

Ensure the proxy hostname and port are correct and reachable before configuring cURL.

```php
<?php
// Verify proxy is reachable
$proxyHost = 'proxy.example.com';
$proxyPort = 8080;

$connection = @fsockopen($proxyHost, $proxyPort, $errno, $errstr, 5);
if (!$connection) {
    throw new RuntimeException("Proxy unreachable: $errstr ($errno)");
}
fclose($connection);

// Now make the request through the proxy
$ch = curl_init('https://api.example.com/data');
curl_setopt_array($ch, [
    CURLOPT_PROXY           => "$proxyHost:$proxyPort",
    CURLOPT_PROXYTYPE       => CURLPROXY_HTTP,
    CURLOPT_RETURNTRANSFER  => true,
]);

$response = curl_exec($ch);
curl_close($ch);
?>
```

### Solution 2: Skip Proxy for Specific Hosts

Bypass the proxy for internal or local resources that should be accessed directly.

```php
<?php
$ch = curl_init('https://api.example.com/data');

curl_setopt_array($ch, [
    CURLOPT_PROXY       => 'proxy.example.com:8080',
    CURLOPT_PROXYTYPE   => CURLPROXY_HTTP,
    CURLOPT_NOPROXY     => 'localhost,127.0.0.1,10.0.0.0/8,.internal.example.com',
    CURLOPT_RETURNTRANSFER => true,
]);

$response = curl_exec($ch);
if (curl_errno($ch)) {
    echo 'Proxy Error: ' . curl_error($ch);
}
curl_close($ch);
?>
```

## Prevention Tips

- Check environment variables HTTP_PROXY, HTTPS_PROXY, and NO_PROXY
- Use `curl -v` from the command line to test proxy connectivity
- Consider using SOCKS5 proxy with CURLOPT_PROXYTYPE for better performance

## Related Errors

- [cURL Connection Error]({{< relref "/languages/php/curl-connection-error" >}})
- [cURL DNS Resolution Error]({{< relref "/languages/php/curl-dns-error" >}})
