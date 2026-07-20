---
title: "[Solution] Nginx Key File Mismatch Error"
description: "The SSL certificate and private key do not match each other."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The SSL certificate and private key do not match each other.

## Common Causes

- **Mixed up certificate files** from different domains
- **Certificate regenerated** without updating key
- **Copied wrong key** during migration
- **Overwritten key** during renewal

## How to Fix

1. Verify match:
```bash
openssl x509 -noout -modulus -in cert.pem | md5sum
openssl rsa -noout -modulus -in key.pem | md5sum
# Both must be identical
```
2. Regenerate key pair if needed
3. Obtain new certificate
4. Validate: `sudo nginx -t && sudo nginx -s reload`

## Examples

**Verify match:**
```bash
openssl x509 -noout -modulus -in cert.pem | openssl md5
openssl rsa -noout -modulus -in key.pem | openssl md5
# If different -> files don't match
```