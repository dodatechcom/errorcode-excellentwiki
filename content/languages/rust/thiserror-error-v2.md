---
title: "[Solution] thiserror Custom Error Derive Fix"
description: "Fix thiserror custom derive errors. Handle error enum definitions, source chaining, and Display implementations."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# thiserror Custom Error Derive

Fix thiserror custom derive errors. Handle error enum definitions, source chaining, and Display implementations.

## What This Error Means

thiserror errors occur when defining custom error types with the derive macro:

```
error[E0277]: the trait bound `MyError: std::error::Error` is not satisfied
error[E0599]: no method named `context` found for struct `MyError`
```

## Common Causes

```rust
// Cause 1: Missing #[from] attribute for automatic conversion
#[derive(thiserror::Error)]
enum MyError {
    Io(#[from] std::io::Error),  // Missing #[from] prevents ? operator
}

// Cause 2: Conflicting Display and #[error] attributes
// Cause 3: Source field not properly annotated
// Cause 4: Using thiserror in binary when library crate defines errors
```

## How to Fix

### Fix 1: Properly annotate error variants

```rust
use thiserror::Error;

#[derive(Error, Debug)]
pub enum AppError {
    #[error("I/O error: {0}")]
    Io(#[from] std::io::Error),

    #[error("Parse error: {0}")]
    Parse(#[from] std::num::ParseIntError),

    #[error("Configuration error: {message}")]
    Config {
        message: String,
        #[source]
        source: Option<Box<dyn std::error::Error + Send + Sync>>,
    },

    #[error("Database error")]
    Database(#[from] sqlx::Error),
}
```

### Fix 2: Use #[source] for error chaining

```rust
use thiserror::Error;

#[derive(Error, Debug)]
pub enum BuildError {
    #[error("Failed to compile: {0}")]
    Compile(#[source] std::io::Error),

    #[error("Missing dependency: {name}")]
    MissingDep {
        name: String,
    },

    #[error("Version conflict: {package} requires {required}, found {found}")]
    VersionConflict {
        package: String,
        required: String,
        found: String,
    },
}
```

### Fix 3: Convert between error types with From

```rust
use thiserror::Error;

#[derive(Error, Debug)]
pub enum ServiceError {
    #[error("Not found: {0}")]
    NotFound(String),

    #[error("Unauthorized")]
    Unauthorized,

    #[error(transparent)]
    Internal(#[from] anyhow::Error),
}

impl From<std::io::Error> for ServiceError {
    fn from(e: std::io::Error) -> Self {
        ServiceError::Internal(e.into())
    }
}
```

## Examples

```rust
use thiserror::Error;

#[derive(Error, Debug)]
pub enum CliError {
    #[error("Failed to read file '{path}': {source}")]
    FileRead {
        path: String,
        #[source]
        source: std::io::Error,
    },

    #[error("Invalid configuration: {0}")]
    Config(String),

    #[error("Operation timed out after {seconds}s")]
    Timeout { seconds: u64 },
}

fn read_config(path: &str) -> Result<String, CliError> {
    std::fs::read_to_string(path)
        .map_err(|e| CliError::FileRead {
            path: path.to_string(),
            source: e,
        })
}

fn main() {
    match read_config("config.toml") {
        Ok(content) => println!("Config: {}", content),
        Err(CliError::FileRead { path, source }) => {
            eprintln!("Could not read '{}': {}", path, source);
        }
        Err(e) => eprintln!("Error: {}", e),
    }
}
```

## Related Errors

- [Anyhow Error]({{< relref "/languages/rust/anyhow-error-v2" >}}) — anyhow context error
- [Trait Error]({{< relref "/languages/rust/trait-error" >}}) — trait object error
- [IO Error]({{< relref "/languages/rust/io-error" >}}) — I/O error
