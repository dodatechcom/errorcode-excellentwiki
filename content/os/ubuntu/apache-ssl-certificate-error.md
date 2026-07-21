---
title: "Apache SSL Certificate Configuration Error"
description: "Apache fails to start due to SSL certificate issues"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Apache SSL Certificate Configuration Error

Apache fails to start due to SSL certificate issues

## Common Causes

- SSLCertificateFile points to non-existent file
- Private key does not match certificate
- Certificate file permissions too restrictive
- Intermediate certificates not concatenated

## How to Fix

1. Verify certificate: `openssl x509 -in cert.pem -text -noout`
2. Check key match: `openssl x509 -noout -modulus -in cert.pem | md5sum`
3. Concatenate chain: `cat cert.pem chain.pem > fullchain.pem`
4. Test config: `apachectl configtest`

## Examples

```bash
# Verify certificate and key match
openssl x509 -noout -modulus -in /etc/ssl/certs/site.pem | md5sum
openssl rsa -noout -modulus -in /etc/ssl/private/site.key | md5sum

# Test Apache config
sudo apachectl configtest
```
