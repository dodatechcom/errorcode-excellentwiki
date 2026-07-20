---
title: "[Solution] webpki Certificate Error Fix"
description: "Fix webpki certificate errors. Handle trust anchor loading, chain verification, and name constraints."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# webpki Certificate Error

The `webpki` crate (used internally by `rustls`) validates X.509 certificates against trust anchors using WebPKI rules. Errors occur when the certificate chain is incomplete, the server name doesn't match the certificate's Subject Alternative Name (SAN), the certificate is expired, or the trust anchor store is empty. The error type is `webpki::Error` with variants like `UnknownIssuer`, `Expired`, `NameMismatch`, and `BadSignature`.

## Common Causes

```rust
use webpki::{CertDer, TrustAnchor, EndEntityCert};
use std::time::SystemTime;

// 1. Empty or missing trust anchor store
let anchors: Vec<TrustAnchor> = vec![];
// No roots to validate against → UnknownIssuer

// 2. Server name doesn't match certificate SAN
let cert = CertDer::from_pem(cert_bytes)?;
// Cert is for "example.com" but we check "evil.com" → NameMismatch

// 3. Certificate expired
// notAfter < current time → Expired

// 4. Incomplete chain — missing intermediate certificate
// Only end-entity cert provided, intermediate not included
```

## How to Fix

1. **Load webpki root certificates properly**

```rust
use webpki::{TrustAnchor, CertDer, EndEntityCert};
use std::time::SystemTime;

// Use webpki-roots for Mozilla's root CA bundle
let trust_roots: Vec<TrustAnchor> = webpki_roots::TLS_SERVER_ROOTS
    .iter()
    .map(|ta| TrustAnchor {
        subject: ta.subject.as_ref(),
        spki: ta.spki.as_ref(),
        name_constraints: ta.name_constraints.as_ref().map(|nc| nc.as_ref()),
    })
    .collect();

let end_entity = CertDer::try_from(cert_bytes)?;
let intermediates = vec![CertDer::try_from(intermediate_bytes)?];

end_entity.verify_is_valid_tls_server_cert(
    &webpki::ring::ALL_VERIFICATION_ALGS,
    &trust_roots,
    &intermediates,
    SystemTime::now(),
)?;
```

2. **Validate the server name correctly**

```rust
use webpki::ServerName;

// The server name must match a SAN or CN in the certificate
let server_name = ServerName::try_from("example.com")?;

// For IP addresses
let server_name = ServerName::try_from(IpAddr::V4(Ipv4Addr::new(192, 168, 1, 1)))?;
```

3. **Check certificate expiry before using it**

```rust
use webpki::CertDer;
use std::time::SystemTime;

let cert = CertDer::try_from(cert_bytes)?;
let now = SystemTime::now();

// webpki verifies expiry internally, but you can check manually
// by examining the certificate's notBefore/notAfter fields
```

4. **Build complete certificate chains**

```rust
use webpki::{CertDer, TrustAnchor};

// Ensure the chain is: end-entity → intermediate(s) → root
let chain = vec![
    CertDer::try_from(end_entity_pem)?,
    CertDer::try_from(intermediate_pem)?,
    // Root is in the trust store, not in the chain
];

// Verify the chain
end_entity.verify_is_valid_tls_server_cert(
    &ALL_VERIFICATION_ALGS,
    &trust_anchors,
    &chain[1..], // intermediates only
    now,
)?;
```

## Examples

```rust
use webpki::{CertDer, TrustAnchor, EndEntityCert};
use std::time::SystemTime;

fn verify_cert_chain(
    cert_pem: &[u8],
    intermediate_pem: &[u8],
) -> Result<(), Box<dyn std::error::Error>> {
    let end_entity = CertDer::try_from(cert_pem)?;
    let intermediate = CertDer::try_from(intermediate_pem)?;

    let trust_roots: Vec<TrustAnchor> = webpki_roots::TLS_SERVER_ROOTS
        .iter()
        .map(|ta| TrustAnchor {
            subject: ta.subject.as_ref(),
            spki: ta.spki.as_ref(),
            name_constraints: ta.name_constraints.as_ref().map(|nc| nc.as_ref()),
        })
        .collect();

    end_entity.verify_is_valid_tls_server_cert(
        &webpki::ring::ALL_VERIFICATION_ALGS,
        &trust_roots,
        &[intermediate],
        SystemTime::now(),
    )?;

    Ok(())
}
```

## Related Errors

- [Rustls Error]({{< relref "/languages/rust/rustls-error" >}}) — TLS implementation
- [Rustls Webpki Error]({{< relref "/languages/rust/rustls-webpki-error" >}}) — rustls-webpki
- [X509 Cert Error]({{< relref "/languages/rust/x509-cert-error" >}}) — X.509 parsing
