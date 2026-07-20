---
title: "[Solution] Rust Derive Error — How to Fix"
description: "Fix derive macro errors. Resolve custom derive implementations, attribute parsing, and generated code issues."
languages: ["rust"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
comments: true
---

# Derive Error

Derive errors occur when `#[derive(...)]` macros cannot automatically implement traits for a type, typically because a contained field doesn't implement the required trait or the derive macro isn't in scope.

## Common Causes

```rust
// #[derive(Debug)] fails because inner type doesn't implement Debug
struct Opaque(*mut std::ffi::c_void);
// #[derive(Debug)] fails — raw pointers need manual Debug impl

// #[derive(Clone)] fails on non-Clone fields
#[derive(Clone)]
struct Config {
    handle: std::sync::MutexGuard<'static, i32>, // MutexGuard !Clone
}

// Missing derive dependency
use serde::{Serialize, Deserialize};
#[derive(Serialize)] // ERROR if serde not in Cargo.toml
struct Data { value: i32 }
```

## How to Fix

1. **Manually implement traits that cannot be derived**

```rust
use std::fmt;

struct Opaque(*mut std::ffi::c_void);

impl fmt::Debug for Opaque {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "Opaque({:p})", self.0)
    }
}
```

2. **Ensure all fields implement the derived trait**

```rust
#[derive(Debug, Clone)]
struct Config {
    name: String,
    width: u32,
    height: u32,
}

#[derive(Debug, Clone)]
struct App {
    config: Config,
    version: String,
}
```

3. **Add derive macros to Cargo.toml and use correct imports**

```toml
[dependencies]
serde = { version = "1.0", features = ["derive"] }
thiserror = "1.0"
```

```rust
use serde::{Serialize, Deserialize};
use thiserror::Error;

#[derive(Debug, Serialize, Deserialize)]
struct Config { name: String, value: i32 }

#[derive(Error, Debug)]
enum AppError {
    #[error("IO error: {0}")]
    Io(#[from] std::io::Error),
    #[error("Parse error: {0}")]
    Parse(#[from] std::num::ParseIntError),
}
```

## Examples

```rust
use serde::{Serialize, Deserialize};
use std::fmt;

#[derive(Debug, Clone, Serialize, Deserialize)]
struct Point { x: f64, y: f64 }

#[derive(Debug, Clone, Serialize, Deserialize)]
struct Circle {
    center: Point,
    radius: f64,
}

impl Circle {
    fn area(&self) -> f64 {
        std::f64::consts::PI * self.radius * self.radius
    }
}

fn main() {
    let c = Circle { center: Point { x: 0.0, y: 0.0 }, radius: 5.0 };
    let json = serde_json::to_string_pretty(&c).unwrap();
    println!("{}", json);
    let parsed: Circle = serde_json::from_str(&json).unwrap();
    println!("Area: {:.2}", parsed.area());
}
```

## Related Errors

- [Syn Error]({{< relref "/languages/rust/rust-syn-error" >}}) — proc macro parsing
- [Proc Macro Error]({{< relref "/languages/rust/rust-proc-macro-error" >}}) — proc macro issues
- [Serde Error]({{< relref "/languages/rust/rust-serde-error-rs" >}}) — serialization issues
