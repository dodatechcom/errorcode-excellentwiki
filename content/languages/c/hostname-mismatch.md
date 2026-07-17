---
title: "[Solution] C SSL: hostname mismatch"
description: "Fix C SSL hostname mismatch. Ensure certificate matches the connecting hostname."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["hostname-mismatch", "ssl", "tls", "certificate", "cn", "sni"]
weight: 5
---

# SSL: hostname mismatch

A hostname mismatch occurs when the certificate's Subject Alternative Name (SAN) or Common Name (CN) does not match the hostname being connected to.

## Common Causes

```c
// Cause 1: Wrong hostname in SNI
// Certificate for example.com, connecting to test.com

// Cause 2: IP address vs hostname
// Certificate for hostname, connecting via IP

// Cause 3: Wildcard mismatch
// Cert for *.example.com, connecting to sub.test.com
```

## How to Fix

### Fix 1: Set correct hostname

```c
SSL_set_tlsext_host_name(ssl, "example.com");
```

### Fix 2: Add SAN to certificate

```bash
# Add SAN when generating certificate
openssl req -x509 -nodes -days 365 \
  -subj "/CN=example.com" \
  -addext "subjectAltName=DNS:example.com,DNS:*.example.com" \
  -newkey rsa:2048 -keyout server.key -out server.crt
```

### Fix 3: Use IP if certificate includes IP SAN

```c
// Certificate must have IP SAN
SSL_set1_host(ssl, "192.168.1.1");
```

## Examples

```bash
# Check certificate SANs
openssl x509 -in cert.pem -noout -text | grep -A1 "Subject Alternative"

# Check hostname match
openssl s_client -connect example.com:443 </dev/null 2>/dev/null | \
  openssl x509 -noout -ext subjectAltName
```

## Related Errors

- [Certificate expired]({{< relref "/languages/c/certificate-expired" >}}) — expired certificate.
- [TLS handshake failure]({{< relref "/languages/c/tls-handshake-failure" >}}) — general TLS error.
- [Self-signed certificate]({{< relref "/languages/c/self-signed-certificate" >}}) — untrusted cert.
