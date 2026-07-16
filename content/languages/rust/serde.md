---
title: "[Solution] Rust Serde Error — Deserialization Failed"
description: "Fix Rust serde deserialization errors. Learn why serde fails to deserialize data and how to handle unknown variants, missing fields, and type mismatches."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
tags: ["serde", "deserialization", "json", "struct", "enum", "derive"]
weight: 5
---

# Serde Error — Deserialization Failed

A serde error with messages like "unknown variant X, expected one of ..." or "missing field X" occurs when the input data doesn't match the expected Rust type structure during deserialization.

## Description

Serde is Rust's serialization/deserialization framework. It maps between data formats (JSON, TOML, YAML, etc.) and Rust types. Errors occur when:

- **Unknown variant** — JSON has a variant name not in the enum definition.
- **Missing field** — required field is absent from the input.
- **Wrong type** — field value type doesn't match the struct field type.
- **Unexpected token** — format-specific syntax error.

Serde errors are descriptive and include the exact field and expected types, making debugging straightforward.

Common scenarios:

- **API response changes** — new fields added or field names changed.
- **Enum variant mismatch** — data has variant not handled in Rust enum.
- **Optional vs required** — field missing but struct requires it.
- **Type confusion** — expecting string, got integer.

## Common Causes

```rust
use serde::Deserialize;

#[derive(Deserialize, Debug)]
struct User {
    name: String,
    age: u32,
}

// Cause 1: Unknown variant
#[derive(Deserialize, Debug)]
enum Color {
    Red,
    Green,
    Blue,
}

let json = r#"{"color": "Yellow"}"#; // Yellow not in enum
let _c: Color = serde_json::from_str(json)?; // error

// Cause 2: Missing field
let json = r#"{"name": "Alice"}"#; // missing "age"
let _user: User = serde_json::from_str(json)?; // error

// Cause 3: Wrong type
let json = r#"{"name": "Alice", "age": "thirty"}"#; // age is string
let _user: User = serde_json::from_str(json)?; // error

// Cause 4: Unexpected null
let json = r#"{"name": null, "age": 30}"#;
let _user: User = serde_json::from_str(json)?; // error if not Option
```

## Solutions

### Fix 1: Use #[serde(default)] for optional fields

```rust
use serde::Deserialize;

#[derive(Deserialize, Debug)]
struct User {
    name: String,
    #[serde(default)]
    age: u32, // defaults to 0 if missing
    #[serde(default)]
    email: Option<String>, // defaults to None if missing
}

fn main() -> Result<(), serde_json::Error> {
    let json = r#"{"name": "Alice"}"#;
    let user: User = serde_json::from_str(json)?;
    println!("{:?}", user);
    Ok(())
}
```

### Fix 2: Use #[serde(rename)] for field name mapping

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

### Fix 3: Handle unknown variants with a catch-all

```rust
use serde::Deserialize;

#[derive(Deserialize, Debug)]
#[serde(rename_all = "snake_case")]
enum Status {
    Active,
    Inactive,
    #[serde(other)]
    Unknown, // catches any unrecognized variant
}

fn main() -> Result<(), serde_json::Error> {
    let json = r#""pending""#;
    let status: Status = serde_json::from_str(json)?;
    println!("{:?}", status); // Unknown
    Ok(())
}
```

### Fix 4: Use custom deserialize for flexible parsing

```rust
use serde::{Deserialize, Deserializer};
use serde_json;

#[derive(Deserialize, Debug)]
struct Config {
    name: String,
    #[serde(deserialize_with = "deserialize_number_from_string")]
    port: u16,
}

fn deserialize_number_from_string<'de, D>(deserializer: D) -> Result<u16, D::Error>
where
    D: Deserializer<'de>,
{
    let s = String::deserialize(deserializer)?;
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
struct User {
    name: String,
    age: u32,
}

fn main() {
    let json = r#"{"name": "Alice"}"#; // missing "age"

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

- [JSON Parse]({{< relref "/languages/rust/json-parse" >}}) — invalid JSON syntax.
- [Type Mismatch]({{< relref "/languages/rust/type-mismatch" >}}) — wrong type in operations.
- [Missing Field]({{< relref "/languages/rust/missing-field" >}}) — missing field in struct initialization.
