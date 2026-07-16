---
title: "[Solution] Rust Reqwest Error — HTTP Request Failed"
description: "Fix Rust reqwest error. Learn why HTTP requests fail with reqwest and how to handle network, TLS, and timeout errors."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
tags: ["reqwest", "http", "request", "network", "tls", "async"]
weight: 5
---

# Reqwest Error — HTTP Request Failed

An error from the `reqwest` crate with the message "error sending request: ..." occurs when an HTTP request fails due to network issues, TLS errors, timeouts, or invalid configurations.

## Description

`reqwest` is Rust's most popular HTTP client. It wraps various error types under `reqwest::Error`, which can represent:

- **Network errors** — DNS resolution failure, connection refused, timeout.
- **TLS errors** — certificate validation failure, protocol mismatch.
- **Request errors** — invalid URL, invalid header values.
- **Redirect errors** — too many redirects, redirect to invalid URL.
- **Body errors** — sending body on GET request, encoding errors.

Common scenarios:

- **Server unreachable** — DNS failure or network down.
- **Invalid certificate** — self-signed cert or expired cert.
- **Timeout** — server too slow to respond.
- **Invalid URL** — malformed URL string.
- **Proxy issues** — proxy not reachable or misconfigured.

## Common Causes

```rust
use reqwest;

// Cause 1: Network not available
let resp = reqwest::blocking::get("http://example.com")?;

// Cause 2: Invalid TLS certificate
let client = reqwest::blocking::Client::builder()
    .danger_accept_invalid_certs(false) // default
    .build()?;
let resp = client.get("https://self-signed.example.com").send()?;

// Cause 3: Timeout
let client = reqwest::blocking::Client::builder()
    .timeout(std::time::Duration::from_secs(1))
    .build()?;
let resp = client.get("http://slow-server.com").send()?;

// Cause 4: Invalid URL
let resp = reqwest::blocking::get("not-a-url")?;

// Cause 5: DNS resolution failure
let resp = reqwest::blocking::get("http://nonexistent.invalid")?;
```

## Solutions

### Fix 1: Handle different error types

```rust
use reqwest;
use std::time::Duration;

fn fetch(url: &str) -> Result<String, Box<dyn std::error::Error>> {
    let client = reqwest::blocking::Client::builder()
        .timeout(Duration::from_secs(30))
        .build()?;

    let response = client.get(url).send().map_err(|e| {
        if e.is_timeout() {
            format!("Request timed out: {}", e)
        } else if e.is_connect() {
            format!("Connection failed: {}", e)
        } else {
            format!("Request failed: {}", e)
        }
    })?;

    let body = response.text()?;
    Ok(body)
}

fn main() {
    match fetch("http://example.com") {
        Ok(body) => println!("Response: {} bytes", body.len()),
        Err(e) => eprintln!("Error: {}", e),
    }
}
```

### Fix 2: Use async reqwest with proper error handling

```rust
use reqwest;
use std::time::Duration;

async fn fetch_async(url: &str) -> Result<String, reqwest::Error> {
    let client = reqwest::Client::builder()
        .timeout(Duration::from_secs(30))
        .connect_timeout(Duration::from_secs(10))
        .build()?;

    let response = client.get(url).send().await?;
    let body = response.text().await?;
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

### Fix 3: Configure TLS settings

```rust
use reqwest::Certificate;
use std::fs;

fn create_client_with_custom_ca() -> Result<reqwest::Client, Box<dyn std::error::Error>> {
    let ca_cert = fs::read("ca-cert.pem")?;
    let cert = Certificate::from_pem(&ca_cert)?;

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

fn fetch_with_retry(url: &str, max_retries: u32) -> Result<String, reqwest::Error> {
    let client = Client::builder()
        .timeout(Duration::from_secs(30))
        .build()?;

    let mut last_err = None;

    for attempt in 0..max_retries {
        match client.get(url).send() {
            Ok(response) => {
                return response.text();
            }
            Err(e) => {
                eprintln!("Attempt {} failed: {}", attempt + 1, e);
                last_err = Some(e);
                if attempt < max_retries - 1 {
                    thread::sleep(Duration::from_millis(500 * (attempt as u64 + 1)));
                }
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

- [Connection Refused]({{< relref "/languages/rust/connection-refused" >}}) — server actively rejects connection.
- [Timed Out]({{< relref "/languages/rust/timed-out" >}}) — request timed out.
- [Invalid URL]({{< relref "/languages/rust/invalid-url" >}}) — malformed URL.
