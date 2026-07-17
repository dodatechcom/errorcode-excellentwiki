---
title: "[Solution] C SSL: self-signed certificate"
description: "Fix C SSL self-signed certificate errors. Trust self-signed certificates or use proper CA-signed certs."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# SSL: self-signed certificate

A self-signed certificate is not signed by a trusted Certificate Authority. SSL libraries reject these certificates by default because they cannot be verified.

## Common Causes

```c
// Cause 1: Using self-signed cert in production
// Generated with openssl self-sign

// Cause 2: Testing with self-signed cert
// Dev environment using untrusted cert

// Cause 3: Missing CA certificate
// CA cert not in trust store
```

## How to Fix

### Fix 1: Trust the CA certificate

```c
SSL_CTX_load_verify_locations(ctx, "/path/to/ca.pem", NULL);
SSL_CTX_set_verify(ctx, SSL_VERIFY_PEER, NULL);
```

### Fix 2: Use a real CA

```bash
# Let's Encrypt (free)
certbot certonly --standalone -d example.com

# Commercial CA
# Purchase and follow CA's process
```

### Fix 3: Disable verification (testing only)

```c
SSL_CTX_set_verify(ctx, SSL_VERIFY_NONE, NULL); // NOT for production
```

## Examples

```bash
# Generate self-signed cert
openssl req -x509 -nodes -days 365 \
  -newkey rsa:2048 \
  -keyout server.key \
  -out server.crt

# Create CA-signed cert
openssl req -new -nodes -out server.csr \
  -newkey rsa:2048 -keyout server.key
openssl ca -in server.csr -out server.crt -cert ca.crt -keyfile ca.key
```

## Related Errors

- [Certificate expired]({{< relref "/languages/c/certificate-expired" >}}) — expired certificate.
- [Hostname mismatch]({{< relref "/languages/c/hostname-mismatch" >}}) — hostname error.
- [TLS handshake failure]({{< relref "/languages/c/tls-handshake-failure" >}}) — general TLS error.
