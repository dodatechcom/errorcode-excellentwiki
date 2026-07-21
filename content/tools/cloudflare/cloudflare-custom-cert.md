---
title: "[Solution] Cloudflare Custom Certificate Error"
description: "Fix Cloudflare custom certificate upload errors. Resolve certificate format and validation issues."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
---

Cloudflare Custom Certificate Error can prevent your application from working correctly.

## Common Causes

- Certificate format is not PEM
- Certificate chain is incomplete
- Private key is encrypted with passphrase
- Certificate does not match domain

## How to Fix

### Verify Format

```bash
openssl x509 -in certificate.pem -text -noout
```

### Full Chain

```bash
cat your-cert.pem intermediate.pem > fullchain.pem
```

### Remove Passphrase

```bash
openssl rsa -in encrypted-key.pem -out decrypted-key.pem
```

