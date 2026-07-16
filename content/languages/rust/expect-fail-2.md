---
title: "[Solution] Rust Called expect on Err — Expect Panic on Result"
description: "Fix Rust expect() on Err panic. Learn why expect panics on Err Results and how to use it properly with error recovery strategies."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
tags: ["expect", "result", "err", "error", "panic", "unwrap"]
weight: 5
---

# Called expect on Err — Expect Panic on Result

A panic with the message "called `Result::expect()` on an `Err` value: ..." occurs when you call `.expect()` on a `Result` that contains an `Err`.

## Description

`expect()` works identically to `unwrap()` but accepts a custom message string that appears in the panic output. It documents _why_ the programmer believes the operation should succeed. Despite the better error message, `.expect()` still panics — the distinction from `.unwrap()` is diagnostic, not behavioral.

Use `.expect()` when failure truly indicates a programmer error (e.g., internal invariants). For recoverable errors, use `match`, `?`, or `unwrap_or_else`.

Common scenarios:

- **Initialization code** — reading a config file that must exist.
- **Test assertions** — convenience in test code.
- **Program invariants** — something that should never fail.
- **Environment setup** — required environment variable.

## Common Causes

```rust
use std::fs;

// Cause 1: File that might not exist
let config = fs::read_to_string("config.toml")
    .expect("config file must exist");

// Cause 2: Environment variable not set
let home = std::env::var("HOME")
    .expect("HOME must be set");

// Cause 3: Parsing that might fail
let port: u16 = "not_a_number".parse()
    .expect("port must be numeric");

// Cause 4: Network that might be unreachable
let resp = reqwest::blocking::get("http://example.com")
    .expect("network must be available");
```

## Solutions

### Fix 1: Replace with match for recoverable errors

```rust
use std::fs;

match fs::read_to_string("config.toml") {
    Ok(content) => println!("Loaded config: {} bytes", content.len()),
    Err(e) => {
        eprintln!("Warning: could not load config: {}", e);
        println!("Using default configuration");
    }
}
```

### Fix 2: Use the ? operator in functions returning Result

```rust
use std::fs;
use std::io;

fn load_config() -> Result<String, io::Error> {
    fs::read_to_string("config.toml")
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let config = load_config()?;
    println!("Config loaded: {} bytes", config.len());
    Ok(())
}
```

### Fix 3: Use unwrap_or_else with context

```rust
use std::fs;

let config = fs::read_to_string("config.toml").unwrap_or_else(|e| {
    eprintln!("Config not found ({}), using defaults", e);
    String::from("[server]\nport = 8080\n")
});
```

### Fix 4: Use expect only for truly infallible operations

```rust
// Good use of expect: the mutex should never be poisoned
use std::sync::{Arc, Mutex};

let data = Arc::new(Mutex::new(Vec::new()));
let lock = data.lock().expect("mutex should not be poisoned");

// Bad use of expect: file might not exist
// let config = fs::read_to_string("config.toml").expect("must exist");
```

## Examples

```rust
use std::fs;

fn main() {
    let content = fs::read_to_string("missing.txt")
        .expect("Failed to read configuration file");
    println!("{}", content);
}
```

Output:
```
thread 'main' panicked at 'Failed to read configuration file: Os { code: 2, kind: NotFound, message: "No such file or directory" }'
```

## Related Errors

- [Unwrap Err]({{< relref "/languages/rust/unwrap-err-2" >}}) — calling unwrap on an Err Result.
- [Unwrap None]({{< relref "/languages/rust/unwrap-none-2" >}}) — calling unwrap on a None Option.
- [File Not Found]({{< relref "/languages/rust/file-not-found-2" >}}) — the specific file system error.
