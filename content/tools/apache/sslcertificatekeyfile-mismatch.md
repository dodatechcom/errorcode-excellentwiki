---
title: "[Solution] Apache SSLCertificateKeyFile Mismatch"
description: "The private key file does not match the SSL certificate."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The private key file does not match the SSL certificate.

## Common Causes

- Key and certificate were generated separately
- Wrong key file referenced
- Key file is corrupted or incomplete

## How to Fix

- Ensure key and certificate share the same key pair
- Verify with: openssl x509 -noout -modulus -in cert.pem | md5sum
- Regenerate a matching pair if needed

## Examples

```
['# Verify match\nopenssl x509 -noout -modulus -in cert.pem | md5sum\nopenssl rsa -noout -modulus -in key.pem | md5sum']
```
