---
title: "[Solution] Rust Serde Deserialization Error — Schema Mismatch"
description: "Fix Rust serde deserialization errors. Learn why serde fails to deserialize data and how to handle unknown variants, missing fields, and type mismatches."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Serde Deserialization Error — Schema Mismatch

A serde error with messages like "unknown variant X, expected one of ..." or "missing field X" occurs when input data doesn't match the expected Rust type during deserialization.

## Description

Serde maps between data formats (JSON, TOML, YAML) and Rust types. Errors occur when:
- **Unknown variant** — data has a variant not in the enum.
- **Missing field** — required field absent from input.
- **Wrong type** — field value type doesn't match struct field.
- **Unexpected token** — format-specific syntax issue.

Common scenarios:

- **API changes** — new fields added or names changed.
- **Enum mismatch** — data has variant not in Rust enum.
- **Optional vs required** — missing field that struct requires.

## Common Causes

```rust
use serde::Deserialize;

#[derive(Deserialize, Debug)]
struct User { name: String, age: u32 }

// Cause 1: Unknown variant
#[derive(Deserialize, Debug)]
enum Color { Red, Green, Blue }

let json = r#"{"color": "Yellow"}"#;
let _c: Color = serde_json::from_str(json)?;

// Cause 2: Missing field
let json = r#"{"name": "Alice"}"#;
let _user: User = serde_json::from_str(json)?;

// Cause 3: Wrong type
let json = r#"{"name": "Alice", "age": "thirty"}"#;
let _user: User = serde_json::from_str(json)?;

// Cause 4: Unexpected null
let json = r#"{"name": null, "age": 30}"#;
let _user: User = serde_json::from_str(json)?;
```

## Solutions

### Fix 1: Use #[serde(default)] for optional fields

```rust
use serde::Deserialize;

#[derive(Deserialize, Debug)]
struct User {
    name: String,
    #[serde(default)]
    age: u32,
    #[serde(default)]
    email: Option<String>,
}

fn main() -> Result<(), serde_json::Error> {
    let json = r#"{"name": "Alice"}"#;
    let user: User = serde_json::from_str(json)?;
    println!("{:?}", user);
    Ok(())
}
```

### Fix 2: Use #[serde(rename)] for field mapping

```rust
use serde::Deserialize;

#[derive(Deserialize, Debug)]
struct User {
    #[serde(rename = "userName")]
    name: String,
    #[serde(rename = "userAge")]
    age: u32,
}

fn main() -> Result<(), serde_json::Error> {
    let json = r#"{"userName": "Alice", "userAge": 30}"#;
    let user: User = serde_json::from_str(json)?;
    println!("{:?}", user);
    Ok(())
}
```

### Fix 3: Catch unknown variants with #[serde(other)]

```rust
use serde::Deserialize;

#[derive(Deserialize, Debug)]
#[serde(rename_all = "snake_case")]
enum Status {
    Active,
    Inactive,
    #[serde(other)]
    Unknown,
}

fn main() -> Result<(), serde_json::Error> {
    let json = r#""pending""#;
    let status: Status = serde_json::from_str(json)?;
    println!("{:?}", status); // Unknown
    Ok(())
}
```

### Fix 4: Custom deserialize for flexible parsing

```rust
use serde::{Deserialize, Deserializer};

#[derive(Deserialize, Debug)]
struct Config {
    name: String,
    #[serde(deserialize_with = "parse_port_from_string")]
    port: u16,
}

fn parse_port_from_string<'de, D>(de: D) -> Result<u16, D::Error>
where D: Deserializer<'de> {
    let s = String::deserialize(de)?;
    s.parse().map_err(serde::de::Error::custom)
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let json = r#"{"name": "server", "port": "8080"}"#;
    let config: Config = serde_json::from_str(json)?;
    println!("{:?}", config);
    Ok(())
}
```

## Examples

```rust
use serde::Deserialize;

#[derive(Deserialize, Debug)]
struct User { name: String, age: u32 }

fn main() {
    let json = r#"{"name": "Alice"}"#;
    match serde_json::from_str::<User>(json) {
        Ok(user) => println!("{:?}", user),
        Err(e) => eprintln!("Error: {}", e),
    }
}
```

Output:
```
Error: missing field `age` at line 1 column 14
```

## Related Errors

- [JSON Parse]({{< relref "/languages/rust/json-parse-2" >}}) — invalid JSON syntax.
- [Type Mismatch]({{< relref "/languages/rust/type-mismatch-2" >}}) — wrong type in operations.
- [Missing Field]({{< relref "/languages/rust/missing-field-2" >}}) — missing field in struct.
