---
title: "[Solution] C Certificate has expired"
description: "Fix C certificate has expired. Update expired SSL/TLS certificates."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Certificate has expired

An expired certificate means the X.509 certificate's validity period has passed. SSL/TLS libraries will reject connections using expired certificates.

## Common Causes

```c
// Cause 1: Server certificate expired
// Certificate not renewed before expiry

// Cause 2: System clock wrong
// Clock set to wrong date

// Cause 3: Certificate authority expired
// Intermediate CA certificate expired
```

## How to Fix

### Fix 1: Renew the certificate

```bash
# Let's Encrypt
certbot renew

# Self-signed
openssl x509 -in old.pem -out new.pem -days 365
```

### Fix 2: Check system clock

```bash
date
timedatectl status
```

### Fix 3: Bypass check (testing only)

```c
SSL_CTX_set_verify(ctx, SSL_VERIFY_NONE, NULL); // NOT for production
```

## Examples

```bash
# Check certificate expiry
openssl s_client -connect example.com:443 </dev/null 2>/dev/null | \
  openssl x509 -noout -dates

# Check local certificate
openssl x509 -in cert.pem -noout -dates
```

## Related Errors

- [TLS handshake failure]({{< relref "/languages/c/tls-handshake-failure" >}}) — general TLS error.
- [Certificate revoked]({{< relref "/languages/c/certificate-revoked" >}}) — revoked certificate.
- [Hostname mismatch]({{< relref "/languages/c/hostname-mismatch" >}}) — hostname error.
