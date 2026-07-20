---
title: "[Solution] thiserror Custom Error Derive Fix"
description: "Fix thiserror custom derive errors. Handle error enum definitions, source chaining, and Display implementations."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ThisError Error

ThisError errors occur when using the `thiserror` crate for custom error types — incorrect derive macros and missing source.

## Common Causes

```rust
// Missing source in #[from]
#[derive(thiserror::Error, Debug)]
enum MyError {
    #[error("IO error")]
    IoError(#[from] io::Error), // source is automatically io::Error
}

// Incorrect display formatting
#[error("Error: {0:?}")] // Debug format — may look ugly
```

## How to Fix

1. **Derive thiserror correctly**

```rust
use thiserror::Error;

#[derive(Error, Debug)]
enum MyError {
    #[error("IO error: {0}")]
    Io(#[from] std::io::Error),

    #[error("Parse error: {0}")]
    Parse(String),

    #[error("Custom error with code {code}")]
    Custom { code: u32, message: String },
}
```

2. **Use #[source] for error chains**

```rust
#[derive(Error, Debug)]
enum AppError {
    #[error("database error")]
    Database(#[source] sqlx::Error),

    #[error("config error")]
    Config(#[source] config::ConfigError),
}
```

3. **Implement Display correctly**

```rust
#[derive(Error, Debug)]
enum Error {
    #[error("failed to read `{path}`: {source}")]
    ReadError { path: String, source: io::Error },
}
```

## Examples

```rust
use thiserror::Error;
use std::fmt;

#[derive(Error, Debug)]
enum AppError {
    #[error("invalid input: {0}")]
    InvalidInput(String),

    #[error("not found: {resource}")]
    NotFound { resource: String },

    #[error(transparent)]
    Other(#[from] Box<dyn std::error::Error>),
}

fn do_work() -> Result<(), AppError> {
    Err(AppError::NotFound { resource: "user".into() })
}

fn main() {
    if let Err(e) = do_work() {
        eprintln!("Error: {}", e);
    }
}
```

## Related Errors

- [Anyhow Error]({{< relref "/languages/rust/anyhow-error" >}}) — anyhow
- [Error Handling]({{< relref "/languages/rust/rust-error-handling-rs" >}}) — patterns
- [Box Error]({{< relref "/languages/rust/rust-box-error" >}}) — Box<dyn Error>
