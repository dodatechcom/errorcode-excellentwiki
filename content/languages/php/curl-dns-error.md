---
title: "[Solution] PHP cURL Could Not Resolve Host"
description: "Fix cURL error 6: Could not resolve host. Learn to troubleshoot DNS resolution issues in PHP cURL requests."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "php"
tags: ["php", "curl", "dns", "network", "hostname"]
severity: "error"
---

# cURL Error 6: Could Not Resolve Host

## Error Message

```
cURL error 6: Could not resolve host: api.example.com
```

## Common Causes

- The hostname in the URL is misspelled
- The DNS server configured on the system is unavailable
- The domain has expired or DNS records are not propagated
- Local /etc/hosts file does not contain the required entry

## Solutions

### Solution 1: Verify DNS Resolution

Confirm the hostname resolves correctly before making cURL requests.

```php
<?php
$hostname = 'api.example.com';

// Check if DNS resolves
$ip = gethostbyname($hostname);
if ($ip === $hostname) {
    echo "DNS resolution failed for $hostname";
} else {
    echo "Resolved $hostname to $ip";
}

// Use IP directly if DNS is unreliable
$ch = curl_init("https://$ip/api/data");
curl_setopt($ch, CURLOPT_HTTPHEADER, ["Host: $hostname"]);
$response = curl_exec($ch);
curl_close($ch);
?>
```

### Solution 2: Use a Custom DNS Server

Override the system DNS resolver by specifying a custom DNS server in cURL.

```php
<?php
$ch = curl_init('https://api.example.com/data');

// Use Google's public DNS resolver
curl_setopt($ch, CURLOPT_RESOLVE, [
    'api.example.com:443:142.250.80.46',
]);

// Or use a custom DNS server via the resolve option
curl_setopt($ch, CURLOPT_DNS_CACHE_TIMEOUT, 300);

$response = curl_exec($ch);
if (curl_errno($ch)) {
    echo 'DNS Error: ' . curl_error($ch);
}
curl_close($ch);
?>
```

## Prevention Tips

- Run `dig` or `nslookup` to verify DNS records from the server
- Consider using a reliable DNS provider like Cloudflare or Google DNS
- Cache DNS lookups locally for frequently accessed hosts

## Related Errors

- [cURL Connection Error]({{< relref "/languages/php/curl-connection-error" >}})
- [cURL Timeout Error]({{< relref "/languages/php/curl-timeout-error" >}})
