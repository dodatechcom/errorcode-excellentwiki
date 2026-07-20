---
title: "[Solution] anyhow Error Context Error Fix"
description: "Fix anyhow error context issues. Handle error chaining, context propagation, and reporting."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Anyhow Error

Anyhow errors occur when using the `anyhow` crate for application-level error handling — context chains, downcast failures, and conversion issues.

## Common Causes

```rust
use anyhow::{Context, Result};

// Missing context
fn read(path: &str) -> Result<String> {
    std::fs::read_to_string(path)? // No context about which file
}

// Using anyhow in library crates (hides types from callers)
pub fn parse(input: &str) -> anyhow::Result<i32> { input.parse().unwrap(); Ok(0) }
```

## How to Fix

1. **Add context to errors**

```rust
use anyhow::{Context, Result};

fn load_config(path: &str) -> Result<String> {
    std::fs::read_to_string(path)
        .with_context(|| format!("Failed to read config from '{}'", path))
}
```

2. **Use thiserror for libraries, anyhow for applications**

```rust
// Library: thiserror
use thiserror::Error;
#[derive(Error, Debug)]
pub enum ConfigError {
    #[error("IO: {0}")]
    Io(#[from] std::io::Error),
    #[error("Parse: {0}")]
    Parse(String),
}

// App: anyhow
use anyhow::Result;
fn main() -> Result<()> {
    let cfg = std::fs::read_to_string("config.toml").context("Reading config")?;
    Ok(())
}
```

3. **Downcast when matching specific errors**

```rust
use anyhow::Result;

fn fetch() -> Result<String> { todo!() }

fn handle() {
    match fetch() {
        Ok(val) => println!("{}", val),
        Err(e) => {
            if let Some(io_err) = e.downcast_ref::<std::io::Error>() {
                eprintln!("IO: {}", io_err);
            }
        }
    }
}
```

## Examples

```rust
use anyhow::{Context, Result, ensure};

fn divide(a: f64, b: f64) -> Result<f64> {
    ensure!(b != 0.0, "Cannot divide {} by zero", a);
    Ok(a / b)
}

fn main() -> Result<()> {
    let result = divide(10.0, 0.0).context("Computing ratio")?;
    println!("{}", result);
    Ok(())
}
```

## Related Errors

- [Thiserror Error]({{< relref "/languages/rust/thiserror-error" >}}) — thiserror crate
- [Error Handling]({{< relref "/languages/rust/rust-error-handling-rs" >}}) — general error handling
- [Color Eyre Error]({{< relref "/languages/rust/color-eyre-error" >}}) — color-eyre
