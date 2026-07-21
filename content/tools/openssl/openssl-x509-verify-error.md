---
title: "[Solution] OpenSSL X509 Verify Error"
description: "Fix OpenSSL X509 verification errors when certificate chain validation fails"
tools: ["openssl"]
error-types: ["tool-error"]
severities: ["error"]
---

# OpenSSL X509 Verify Error

X509 verify errors occur when OpenSSL cannot validate a certificate chain.

## Common Causes

- Certificate signed by unknown CA
- Certificate expired or not yet valid
- Key usage does not match intended purpose
- Name constraints violated

## Common Error Messages

```
Verify return code: 20 (unable to get local issuer certificate)
```

## How to Fix

### 1. Verify Certificate Chain

```bash
openssl verify -CAfile ca.pem -untrusted intermediate.pem cert.pem
```

### 2. Check Certificate Details

```bash
openssl x509 -in cert.pem -text -noout
```

### 3. Add Missing CA Certificate

```bash
openssl s_client -connect example.com:443 -CAfile /etc/ssl/certs/ca-certificates.crt
```

## Examples

```bash
openssl verify -verbose -CAfile root.pem intermediate.pem cert.pem
```
