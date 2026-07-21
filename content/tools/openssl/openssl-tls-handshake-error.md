---
title: "[Solution] OpenSSL TLS Handshake Error"
description: "Fix OpenSSL TLS handshake errors when establishing encrypted connections fails"
tools: ["openssl"]
error-types: ["tool-error"]
severities: ["error"]
---

# OpenSSL TLS Handshake Error

TLS handshake errors occur when OpenSSL cannot complete the TLS negotiation.

## Common Causes

- Protocol version mismatch between client and server
- Cipher suite not supported by either side
- Certificate not matching hostname
- Client certificate required but not provided

## Common Error Messages

```
error:14094418:SSL routines:ssl3_read_bytes:tlsv1 alert unknown ca
```

## How to Fix

### 1. Check Supported Protocols

```bash
openssl s_client -connect example.com:443 -tls1_2
```

### 2. List Available Ciphers

```bash
openssl ciphers -v 'HIGH:!aNULL:!MD5'
```

### 3. Force Specific Protocol

```bash
openssl s_client -connect example.com:443 -tls1_3
```

## Examples

```bash
openssl s_client -connect example.com:443 -showcerts 2>&1 | grep "Protocol\|Cipher"
```
