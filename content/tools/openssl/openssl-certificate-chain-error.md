---
title: "[Solution] OpenSSL Certificate Chain Error"
description: "Fix OpenSSL certificate chain errors when intermediate certificates are missing"
tools: ["openssl"]
error-types: ["tool-error"]
severities: ["error"]
---

# OpenSSL Certificate Chain Error

Certificate chain errors occur when the complete certificate chain cannot be built.

## Common Causes

- Missing intermediate CA certificate
- Self-signed certificate not in trust store
- Chain order incorrect in bundle
- Cross-signed certificate confusion

## Common Error Messages

```
verify error:num=20:unable to get local issuer certificate
```

## How to Fix

### 1. Build Certificate Chain

```bash
cat server.pem intermediate.pem ca.pem > fullchain.pem
```

### 2. Verify Chain

```bash
openssl verify -CAfile ca.pem -untrusted intermediate.pem server.pem
```

### 3. Check Chain Depth

```bash
openssl s_client -connect example.com:443 -showcerts 2>&1 | grep "s:" | head -5
```

## Examples

```bash
openssl s_client -connect example.com:443 -showcerts | openssl x509 -noout -issuer -subject
```
