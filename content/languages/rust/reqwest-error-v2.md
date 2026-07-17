---
title: "[Solution] reqwest TLS Certificate Error Fix"
description: "Fix reqwest TLS certificate errors. Handle certificate validation, custom certificates, and TLS backend issues."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# reqwest TLS Certificate Error

Fix reqwest TLS certificate errors. Handle certificate validation, custom certificates, and TLS backend issues.

## What This Error Means

reqwest TLS certificate errors occur when the HTTP client cannot validate the server's SSL/TLS certificate:

```
error sending request: error trying to connect: custom certificate find failed
reqwest::Error { kind: Builder(Certificate(CertificateRequired)) }
```

## Common Causes

```rust
// Cause 1: Self-signed certificate not trusted by system
let resp = reqwest::get("https://self-signed.local/api").await?;

// Cause 2: Certificate expired or not yet valid
// Cause 3: Missing intermediate certificates in chain
// Cause 4: Hostname does not match certificate CN/SAN
```

## How to Fix

### Fix 1: Add a custom CA certificate

```rust
use reqwest::Certificate;

let ca = Certificate::from_pem(b"-----BEGIN CERTIFICATE-----
MIIDxTCCAq2gAwIBAgIJAL...
-----END CERTIFICATE-----")?;

let client = reqwest::Client::builder()
    .add_root_certificate(ca)
    .build()?;
```

### Fix 2: Disable certificate verification (development only)

```rust
use reqwest::Client;

let client = Client::builder()
    .danger_accept_invalid_certs(true)
    .build()?;
```

### Fix 3: Use a custom TLS connector with native-tls

```rust
use native_tls::TlsConnector;

let tls = TlsConnector::builder()
    .add_root_certificate(native_tls::Certificate::from_pem(&ca_pem)?)
    .build()?;

let connector = hyper_tls::HttpsConnector::from((http_connector, tls));
```

## Examples

```rust
use reqwest::Certificate;
use std::fs;

async fn fetch_with_custom_ca() -> Result<(), reqwest::Error> {
    let ca_cert = fs::read("ca-cert.pem").expect("Failed to read CA cert");
    let cert = Certificate::from_pem(&ca_cert).expect("Invalid certificate");

    let client = reqwest::Client::builder()
        .add_root_certificate(cert)
        .timeout(std::time::Duration::from_secs(30))
        .build()?;

    let resp = client
        .get("https://internal.example.com/api/data")
        .send()
        .await?;

    println!("Status: {}", resp.status());
    Ok(())
}
```

## Related Errors

- [Webpki Error]({{< relref "/languages/rust/webpki-error" >}}) — webpki certificate error
- [Native TLS Error]({{< relref "/languages/rust/native-tls-error" >}}) — native-tls error
- [Reqwest Error]({{< relref "/languages/rust/reqwest-error" >}}) — reqwest error
