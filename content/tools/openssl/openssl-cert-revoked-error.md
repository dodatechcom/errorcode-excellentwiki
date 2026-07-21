---
title: "[Solution] OpenSSL Certificate Revoked Error"
description: "Fix OpenSSL certificate revoked errors when CRL check detects revoked certificate"
tools: ["openssl"]
error-types: ["tool-error"]
severities: ["error"]
---

# OpenSSL Certificate Revoked Error

Certificate revoked errors occur when OpenSSL detects that a certificate has been revoked via CRL.

## Common Causes

- Certificate was revoked by CA
- CRL check enabled in verification
- CRL is outdated and missing recent revocations
- OCSP responder confirms revocation

## Common Error Messages

```
error:10000041:SSL routines:OPENSSL_internal:certificate revoked
```

## How to Fix

### 1. Check CRL Status

```bash
openssl crl -in crl.pem -text -noout
```

### 2. Skip CRL Check (Test Only)

```bash
openssl verify -no_check_time -partial_chain cert.pem
```

### 3. Get Latest CRL

```bash
openssl s_client -connect example.com:443 -crl_check -CAfile ca.pem
```

## Examples

```bash
openssl x509 -in cert.pem -text | grep -A2 "CRL Distribution"
```
