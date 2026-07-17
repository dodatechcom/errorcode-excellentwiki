---
title: "[Solution] serde_json Unexpected End of Input Error Fix"
description: "Fix serde_json unexpected end of input errors. Handle truncated JSON, incomplete streams, and encoding issues."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["serde", "json", "parsing", "truncated", "stream"]
weight: 5
---

# serde_json Unexpected End of Input Error

Fix serde_json unexpected end of input errors. Handle truncated JSON, incomplete streams, and encoding issues.

## What This Error Means

This error occurs when serde_json tries to parse JSON that is incomplete or truncated:

```
Error("EOF while parsing an object at line 1 column 42")
Error("EOF while parsing an array at line 1 column 1")
Error("unexpected end of input")
```

## Common Causes

```rust
// Cause 1: Truncated HTTP response body
let text = response.text().await?; // Incomplete JSON
let data: MyStruct = serde_json::from_str(&text)?;

// Cause 2: Reading partial file contents
let bytes = std::fs::read("data.json")?; // File was corrupted or truncated
let data: MyStruct = serde_json::from_slice(&bytes)?;

// Cause 3: Streaming JSON not fully received
// Cause 4: Encoding issues cutting off multi-byte characters
```

## How to Fix

### Fix 1: Validate JSON before deserializing

```rust
use serde_json::Value;

fn parse_json_safely(input: &str) -> Result<Value, serde_json::Error> {
    let trimmed = input.trim();
    if trimmed.is_empty() {
        return Err(serde_json::from_str::<Value>("{}").unwrap_err());
    }
    serde_json::from_str(trimmed)
}
```

### Fix 2: Use a buffered reader for streaming

```rust
use serde_json::from_reader;
use std::io::BufReader;

fn read_json_file(path: &str) -> Result<MyStruct, Box<dyn std::error::Error>> {
    let file = std::fs::File::open(path)?;
    let reader = BufReader::new(file);
    let data: MyStruct = from_reader(reader)?;
    Ok(data)
}
```

### Fix 3: Add validation after HTTP responses

```rust
async fn fetch_json<T: serde::de::DeserializeOwned>(
    url: &str,
) -> Result<T, reqwest::Error> {
    let response = reqwest::get(url).await?;
    let text = response.text().await?;

    if text.is_empty() {
        return Err(reqwest::Error::new(
            reqwest::StatusCode::OK,
            "Empty response body",
        ));
    }

    serde_json::from_str(&text)
        .map_err(|e| reqwest::Error::new(
            reqwest::StatusCode::OK,
            format!("JSON parse error: {}", e),
        ))
}
```

## Examples

```rust
use serde::Deserialize;
use serde_json;

#[derive(Deserialize, Debug)]
struct DataPoint {
    timestamp: u64,
    value: f64,
}

fn parse_batch(json: &str) -> Result<Vec<DataPoint>, serde_json::Error> {
    let trimmed = json.trim();
    if trimmed.is_empty() {
        return Ok(Vec::new());
    }
    serde_json::from_str(trimmed)
}

fn main() {
    let input = r#"[{"timestamp": 1640995200, "value": 42.0}]"#;
    match parse_batch(input) {
        Ok(data) => println!("Parsed {} data points", data.len()),
        Err(e) => eprintln!("Parse error: {}", e),
    }
}
```

## Related Errors

- [Serde Error]({{< relref "/languages/rust/serde-error-v2" >}}) — serde deserialization error
- [JSON Parse]({{< relref "/languages/rust/json-parse" >}}) — JSON parse error
- [Timed Out]({{< relref "/languages/rust/timed-out" >}}) — timeout error
