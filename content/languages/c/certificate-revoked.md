---
title: "[Solution] C Certificate has been revoked"
description: "Fix C certificate has been revoked. Handle revoked SSL/TLS certificates."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Certificate has been revoked

A revoked certificate is one that has been invalidated before its expiry date. The certificate authority has explicitly marked it as no longer trustworthy.

## Common Causes

```c
// Cause 1: Private key compromised
// Server admin revoked cert after key leak

// Cause 2: CA policy violation
// Certificate found to violate CA policy

// Cause 3: Domain ownership change
// Certificate revoked when domain changed hands
```

## How to Fix

### Fix 1: Get a new certificate

```bash
# Generate new CSR and get signed
openssl req -new -key server.key -out server.csr
```

### Fix 2: Check CRL (Certificate Revocation List)

```bash
openssl s_client -connect example.com:443 -crl_check
```

### Fix 3: Handle in application

```c
long verify_result = SSL_get_verify_result(ssl);
if (verify_result == X509_V_ERR_CERT_REVOKED) {
    fprintf(stderr, "Certificate has been revoked\n");
    SSL_shutdown(ssl);
}
```

## Related Errors

- [Certificate expired]({{< relref "/languages/c/certificate-expired" >}}) — expired certificate.
- [TLS handshake failure]({{< relref "/languages/c/tls-handshake-failure" >}}) — general TLS error.
- [Self-signed certificate]({{< relref "/languages/c/self-signed-certificate" >}}) — untrusted cert.
