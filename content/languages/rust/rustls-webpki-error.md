---
title: "[Solution] rustls-webpki Verification Error Fix"
description: "Fix rustls-webpki verification errors. Handle certificate validation, CRL checking, and trust stores."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Rustls Webpki Error

Rustls webpki errors occur when using `rustls-webpki` for certificate verification — untrusted roots and name mismatch.

## Common Causes

```rust
// Certificate not signed by trusted root
// Server name does not match certificate CN/SAN
// Certificate expired
```

## How to Fix

1. **Verify certificate chain**

```rust
use rustls_webpki::{VerifyServerCert, CertDer};

let end_entity = CertDer::from_pem(cert_pem)?;
let intermediate = CertDer::from_pem(intermediate_pem)?;

end_entity.verify_is_valid_tls_server_cert(
    &[&intermediate],
    &roots,
    &server_name,
    now,
)?;
```

2. **Check name matching**

```rust
use rustls_webpki::SubjectNameRef;

let name = SubjectNameRef::try_from("example.com")?;
// Verify SAN or CN matches
```

3. **Handle certificate expiry**

```rust
// Check not_before and not_after
```

## Examples

```rust
use rustls_webpki::{verify_tls_cert, CertDer};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let cert = CertDer::from_pem(include_bytes!("cert.pem"))?;
    println!("Certificate loaded successfully");
    Ok(())
}
```

## Related Errors

- [Rustls Error]({{< relref "/languages/rust/rustls-error" >}}) — Rustls TLS
- [Ring Error]({{< relref "/languages/rust/ring-error" >}}) — crypto
- [X509 Cert Error]({{< relref "/languages/rust/x509-cert-error" >}}) — X.509
