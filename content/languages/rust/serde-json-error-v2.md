---
title: "[Solution] serde_json Unexpected End of Input Error Fix"
description: "Fix serde_json unexpected end of input errors. Handle truncated JSON, incomplete streams, and encoding issues."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Serde JSON Error

Serde JSON errors occur when using `serde_json` — invalid JSON syntax, trailing commas, and type mismatches.

## Common Causes

```rust
// Trailing comma
let v: Value = serde_json::from_str(r#"{"a": 1,}"#)?; // ERROR

// Unexpected token
let v: Value = serde_json::from_str(r#"{"a": 1 "#)?; // ERROR
```

## How to Fix

1. **Ensure valid JSON**

```rust
use serde_json::Value;

let json = r#"{"key": "value", "number": 42}"#;
let v: Value = serde_json::from_str(json)?;
```

2. **Handle type errors**

```rust
use serde::Deserialize;

#[derive(Deserialize)]
struct Config {
    name: String,
    port: u16,
}

let json = r#"{"name": "app", "port": 3000}"#;
let config: Config = serde_json::from_str(json)?;
```

3. **Use Value for dynamic JSON**

```rust
use serde_json::{json, Value};

let data = json!({
    "name": "Alice",
    "scores": [95, 87, 92]
});

let name = data["name"].as_str().unwrap();
```

## Examples

```rust
use serde_json::{json, Value};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let data = json!({
        "users": [
            {"name": "Alice", "age": 30},
            {"name": "Bob", "age": 25}
        ]
    });

    let users = data["users"].as_array().unwrap();
    for user in users {
        println!("{}: {}", user["name"], user["age"]);
    }
    Ok(())
}
```

## Related Errors

- [TOML Error]({{< relref "/languages/rust/toml-error" >}}) — TOML
- [YAML Error]({{< relref "/languages/rust/yaml-error" >}}) — YAML
- [Serde Error]({{< relref "/languages/rust/serde-error" >}}) — core serde
