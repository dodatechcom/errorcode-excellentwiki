---
title: "[Solution] Rust Reqwest Error — HTTP Request Failed"
description: "Fix Rust reqwest error. Learn why HTTP requests fail with reqwest and how to handle network, TLS, timeout, and DNS errors."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Reqwest Error — HTTP Request Failed

An error from the `reqwest` crate with the message "error sending request: ..." occurs when an HTTP request fails due to network issues, TLS errors, timeouts, or invalid configurations.

## Description

`reqwest` is Rust's most popular HTTP client. It wraps various error types under `reqwest::Error`, covering network errors, TLS failures, request construction errors, redirect issues, and body encoding problems.

Common scenarios:

- **Server unreachable** — DNS failure or network down.
- **Invalid certificate** — self-signed or expired cert.
- **Timeout** — server too slow.
- **Invalid URL** — malformed URL string.
- **Proxy issues** — proxy not reachable.

## Common Causes

```rust
use reqwest;

// Cause 1: Network unavailable
let resp = reqwest::blocking::get("http://example.com")?;

// Cause 2: Invalid TLS certificate
let client = reqwest::blocking::Client::builder()
    .danger_accept_invalid_certs(false)
    .build()?;
let resp = client.get("https://self-signed.example.com").send()?;

// Cause 3: Timeout
let client = reqwest::blocking::Client::builder()
    .timeout(std::time::Duration::from_secs(1))
    .build()?;
let resp = client.get("http://slow-server.com").send()?;

// Cause 4: DNS failure
let resp = reqwest::blocking::get("http://nonexistent.invalid")?;
```

## Solutions

### Fix 1: Classify error types

```rust
use std::time::Duration;

fn fetch(url: &str) -> Result<String, Box<dyn std::error::Error>> {
    let client = reqwest::blocking::Client::builder()
        .timeout(Duration::from_secs(30))
        .build()?;

    let response = client.get(url).send().map_err(|e| {
        if e.is_timeout() { format!("Timed out: {}", e) }
        else if e.is_connect() { format!("Connect failed: {}", e) }
        else { format!("Request failed: {}", e) }
    })?;

    Ok(response.text()?)
}
```

### Fix 2: Use async reqwest

```rust
use reqwest;
use std::time::Duration;

async fn fetch_async(url: &str) -> Result<String, reqwest::Error> {
    let client = reqwest::Client::builder()
        .timeout(Duration::from_secs(30))
        .connect_timeout(Duration::from_secs(10))
        .build()?;
    let body = client.get(url).send().await?.text().await?;
    Ok(body)
}

#[tokio::main]
async fn main() {
    match fetch_async("http://example.com").await {
        Ok(body) => println!("Response: {} bytes", body.len()),
        Err(e) => eprintln!("Error: {}", e),
    }
}
```

### Fix 3: Configure TLS

```rust
use reqwest::Certificate;
use std::fs;

fn custom_ca_client() -> Result<reqwest::Client, Box<dyn std::error::Error>> {
    let ca = fs::read("ca-cert.pem")?;
    let cert = Certificate::from_pem(&ca)?;
    let client = reqwest::Client::builder()
        .add_root_certificate(cert)
        .build()?;
    Ok(client)
}
```

### Fix 4: Retry failed requests

```rust
use reqwest::blocking::Client;
use std::thread;
use std::time::Duration;

fn fetch_retry(url: &str, retries: u32) -> Result<String, reqwest::Error> {
    let client = Client::builder().timeout(Duration::from_secs(30)).build()?;
    let mut last_err = None;
    for attempt in 0..retries {
        match client.get(url).send() {
            Ok(resp) => return resp.text(),
            Err(e) => {
                last_err = Some(e);
                thread::sleep(Duration::from_millis(500 * (attempt as u64 + 1)));
            }
        }
    }
    Err(last_err.unwrap())
}
```

## Examples

```rust
use reqwest;

fn main() {
    match reqwest::blocking::get("http://nonexistent.invalid") {
        Ok(resp) => println!("Status: {}", resp.status()),
        Err(e) => eprintln!("Error: {}", e),
    }
}
```

Output:
```
Error: error sending request: error sending request for url (http://nonexistent.invalid/): error trying to connect: dns error: failed to lookup address information
```

## Related Errors

- [Connection Refused]({{< relref "/languages/rust/connection-refused-2" >}}) — server rejects connection.
- [Timed Out]({{< relref "/languages/rust/timed-out-2" >}}) — request timed out.
- [Invalid URL]({{< relref "/languages/rust/invalid-url-2" >}}) — malformed URL.
