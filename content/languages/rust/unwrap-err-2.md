---
title: "[Solution] Rust Called unwrap on Err — Result Unwrap Panic"
description: "Fix Rust unwrap() on Err panic. Learn why calling unwrap on a failed Result crashes and how to handle errors with match, ?, or expect."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
tags: ["unwrap", "result", "err", "error", "panic", "match"]
weight: 5
---

# Called unwrap on Err — Result Unwrap Panic

A panic with the message "called `Result::unwrap()` on an `Err` value: ..." occurs when you call `.unwrap()` on a `Result` that contains an `Err`.

## Description

`Result<T, E>` represents an operation that can fail — `Ok(value)` or `Err(error)`. The `.unwrap()` method extracts the value from `Ok` or panics with the error message from `Err`. This panic is one of the most common in Rust programs, especially when using `?` is not an option (e.g., in closures or initialization code).

Common scenarios:

- **File I/O** — file doesn't exist or is locked.
- **Network requests** — connection fails.
- **Parsing** — input doesn't match expected format.
- **Environment variables** — variable not set.
- **Lock acquisition** — mutex is poisoned.

## Common Causes

```rust
use std::fs;

// Cause 1: File not found
let content = fs::read_to_string("config.toml").unwrap(); // panics if missing

// Cause 2: Parse failure
let num: Result<i32, _> = "abc".parse();
num.unwrap(); // panic

// Cause 3: Permission error
let content = fs::read_to_string("/root/secret").unwrap(); // panic

// Cause 4: Network failure
let resp = reqwest::blocking::get("http://unreachable.invalid").unwrap(); // panic
```

## Solutions

### Fix 1: Use match for explicit handling

```rust
use std::fs;

match fs::read_to_string("config.toml") {
    Ok(content) => println!("Config: {}", content),
    Err(e) => eprintln!("Failed to read config: {}", e),
}
```

### Fix 2: Use the ? operator

```rust
use std::fs;
use std::io;

fn read_config() -> io::Result<String> {
    let content = fs::read_to_string("config.toml")?;
    Ok(content)
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let config = read_config()?;
    println!("{}", config);
    Ok(())
}
```

### Fix 3: Use unwrap_or_else for recovery

```rust
use std::fs;

let content = fs::read_to_string("config.toml").unwrap_or_else(|e| {
    eprintln!("Using default config: {}", e);
    String::from("[defaults]\nport = 8080")
});
```

### Fix 4: Use map_err to convert error types

```rust
use std::fs;

fn load_config() -> Result<String, String> {
    fs::read_to_string("config.toml")
        .map_err(|e| format!("Config error: {}", e))
}
```

## Examples

```rust
use std::fs;

fn main() {
    let content = fs::read_to_string("nonexistent_file.txt").unwrap();
    println!("{}", content);
}
```

Output:
```
thread 'main' panicked at 'called `Result::unwrap()` on an `Err` value: Os { code: 2, kind: NotFound, message: "No such file or directory" }'
```

## Related Errors

- [Unwrap None]({{< relref "/languages/rust/unwrap-none-2" >}}) — unwrap on a None Option.
- [Expect Fail]({{< relref "/languages/rust/expect-fail-2" >}}) — expect on an Err Result.
- [IO Error]({{< relref "/languages/rust/io-error-2" >}}) — the underlying I/O error.
