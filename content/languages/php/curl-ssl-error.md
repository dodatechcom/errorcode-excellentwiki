---
title: "[Solution] PHP cURL SSL Certificate Error"
description: "Fix cURL error 60: SSL certificate problem: unable to get local issuer certificate. Learn to configure CA certificates and SSL verification in PHP cURL."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "php"
tags: ["php", "curl", "ssl", "certificate", "https"]
severity: "error"
---

# cURL Error 60: SSL Certificate Problem

## Error Message

```
cURL error 60: SSL certificate problem: unable to get local issuer certificate
```

## Common Causes

- The CA certificate bundle is missing or not configured in PHP
- The server uses a self-signed or intermediate SSL certificate
- The `curl.cainfo` setting in php.ini points to an outdated or incorrect CA bundle
- Corporate proxy or firewall performs SSL interception (MITM)

## Solutions

### Solution 1: Set the CA Certificate Bundle Path

Point cURL to a valid CA certificate bundle. You can download the latest bundle from the cURL website or use the one bundled with your system.

```php
<?php
$ch = curl_init('https://api.example.com/data');

// Point to a valid CA certificate bundle
curl_setopt($ch, CURLOPT_CAINFO, '/etc/ssl/certs/ca-certificates.crt');

// Alternatively, set it globally in php.ini:
// curl.cainfo = "/etc/ssl/certs/ca-certificates.crt"

$response = curl_exec($ch);
if (curl_errno($ch)) {
    echo 'SSL Error: ' . curl_error($ch);
}
curl_close($ch);
?>
```

### Solution 2: Disable SSL Verification (Not Recommended for Production)

Temporarily disable SSL certificate verification for debugging. Never use this in production environments.

```php
<?php
$ch = curl_init('https://api.example.com/data');

// Disable SSL verification — use only for testing!
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0);

$response = curl_exec($ch);
curl_close($ch);
?>
```

### Solution 3: Add the CA Certificate Inline

Embed the CA certificate directly in your cURL request when you cannot modify server-level configuration.

```php
<?php
$caCertificate = file_get_contents('/path/to/certificate.pem');

$ch = curl_init('https://api.example.com/data');
curl_setopt($ch, CURLOPT_SSLCERT, '/path/to/client.pem');
curl_setopt($ch, CURLOPT_SSLKEY, '/path/to/client-key.pem');
curl_setopt($ch, CURLOPT_CAINFO, '/path/to/ca-cert.pem');

$response = curl_exec($ch);
curl_close($ch);
?>
```

## Prevention Tips

- Always use a valid CA certificate bundle in production environments
- Keep your CA certificate bundle updated regularly
- Test SSL connections with `openssl s_client` before integrating into PHP code

## Related Errors

- [cURL Connection Error]({{< relref "/languages/php/curl-connection-error" >}})
- [cURL HTTP Error]({{< relref "/languages/php/curl-http-error" >}})
