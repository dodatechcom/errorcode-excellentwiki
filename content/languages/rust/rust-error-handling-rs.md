---
title: "[Solution] Rust Error Handling Error — How to Fix"
description: "Fix Rust error handling patterns. Resolve Result, Option, and error propagation issues."
languages: ["rust"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
comments: true
---

# Error Handling

Rust error handling errors occur when using the `?` operator, `Result`, `Option`, or `unwrap()` incorrectly — type mismatches in error propagation, missing `From` implementations, or panicking in production code.

## Common Causes

```rust
// Error type mismatch — missing From impl
fn read_file() -> Result<String, MyError> {
    let content = std::fs::read_to_string("file.txt")?; // ERROR: io::Error !From MyError
    Ok(content)
}

// Using unwrap() in library code — panics on error
fn parse(input: &str) -> i32 {
    input.parse().unwrap() // Panics on invalid input
}

// Option without handling None
fn get_first(v: Vec<i32>) -> i32 {
    v[0] // Panics if empty
}
```

## How to Fix

1. **Implement `From` or use `map_err` for error conversion**

```rust
use std::fmt;

#[derive(Debug)]
enum AppError {
    Io(std::io::Error),
    Parse(String),
}

impl fmt::Display for AppError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match self {
            AppError::Io(e) => write!(f, "IO: {}", e),
            AppError::Parse(s) => write!(f, "Parse: {}", s),
        }
    }
}

impl From<std::io::Error> for AppError {
    fn from(e: std::io::Error) -> Self { AppError::Io(e) }
}

fn read_config() -> Result<String, AppError> {
    let content = std::fs::read_to_string("config.txt")?; // Uses From impl
    Ok(content)
}
```

2. **Replace `unwrap()` with proper error handling**

```rust
fn parse(input: &str) -> Result<i32, String> {
    input.parse().map_err(|e| format!("Failed to parse '{}': {}", input, e))
}

fn get_first(v: &[i32]) -> Option<&i32> {
    v.first()
}

fn main() {
    match parse("abc") {
        Ok(n) => println!("Parsed: {}", n),
        Err(e) => eprintln!("Error: {}", e),
    }

    let v = vec![1, 2, 3];
    if let Some(first) = get_first(&v) {
        println!("First: {}", first);
    }
}
```

3. **Use `thiserror` for libraries and `anyhow` for applications**

```rust
// Library error types
use thiserror::Error;

#[derive(Error, Debug)]
pub enum ServiceError {
    #[error("Database error: {0}")]
    Database(#[from] sqlx::Error),
    #[error("Not found: {0}")]
    NotFound(String),
    #[error("Unauthorized")]
    Unauthorized,
}

// Application-level with anyhow
use anyhow::Result;
fn main() -> Result<()> {
    let config = std::fs::read_to_string("config.toml")?;
    Ok(())
}
```

## Examples

```rust
use std::fmt;

#[derive(Debug)]
enum AppError { Io(std::io::Error), Parse(std::num::ParseIntError), Custom(String) }

impl fmt::Display for AppError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match self {
            AppError::Io(e) => write!(f, "IO error: {}", e),
            AppError::Parse(e) => write!(f, "Parse error: {}", e),
            AppError::Custom(s) => write!(f, "{}", s),
        }
    }
}
impl std::error::Error for AppError {}
impl From<std::io::Error> for AppError { fn from(e: std::io::Error) -> Self { AppError::Io(e) } }
impl From<std::num::ParseIntError> for AppError { fn from(e: std::num::ParseIntError) -> Self { AppError::Parse(e) } }

fn process() -> Result<i32, AppError> {
    let content = std::fs::read_to_string("numbers.txt")?;
    let num: i32 = content.trim().parse()?;
    if num < 0 { return Err(AppError::Custom("Negative not allowed".into())); }
    Ok(num)
}

fn main() {
    match process() {
        Ok(n) => println!("Result: {}", n),
        Err(e) => eprintln!("Failed: {}", e),
    }
}
```

## Related Errors

- [Anyhow Error]({{< relref "/languages/rust/rust-anyhow-error" >}}) — anyhow crate
- [Thiserror Error]({{< relref "/languages/rust/thiserror-error" >}}) — thiserror crate
- [Box Error]({{< relref "/languages/rust/rust-box-error" >}}) — Box<dyn Error>
