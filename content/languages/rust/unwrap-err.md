---
title: "[Solution] Rust Called unwrap on Err — Result Unwrap Panic"
description: "Fix Rust unwrap() on Err panic. Learn why calling unwrap on an Err Result causes a panic and how to handle errors properly."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Called unwrap on Err — Result Unwrap Panic

A panic with the message "called `Result::unwrap()` on an `Err` value" occurs when you call `.unwrap()` on a `Result` that contains an `Err`. This is a common panic when error handling is overlooked.

## Description

`Result<T, E>` is Rust's way of representing operations that can fail — it can be either `Ok(value)` or `Err(error)`. The `.unwrap()` method extracts the value from `Ok` or panics with the error message from `Err`. This panic is almost always a bug — the programmer didn't anticipate or handle the failure case.

Common scenarios:

- **File operations** — file doesn't exist or can't be opened.
- **Network requests** — connection fails or times out.
- **Parsing** — input string doesn't match expected format.
- **System calls** — OS operations fail due to permissions or resources.

## Common Causes

```rust
use std::fs;

// Cause 1: File not found
let content = fs::read_to_string("nonexistent.txt").unwrap(); // panics with Err

// Cause 2: Parsing failure
let num: Result<i32, _> = "abc".parse(); // Err
let num = num.unwrap(); // panics

// Cause 3: Network error
let response = reqwest::blocking::get("http://invalid.example.com").unwrap(); // panics on connection error

// Cause 4: Permission denied
let content = fs::read_to_string("/root/secret.txt").unwrap(); // panics on permission error
```

## Solutions

### Fix 1: Use match for explicit error handling

```rust
use std::fs;

// Wrong
let content = fs::read_to_string("config.txt").unwrap();

// Correct
match fs::read_to_string("config.txt") {
    Ok(content) => println!("Config: {}", content),
    Err(e) => eprintln!("Failed to read config: {}", e),
}
```

### Fix 2: Use the ? operator to propagate errors

```rust
use std::fs;
use std::io;

// Wrong
fn read_config() -> String {
    fs::read_to_string("config.txt").unwrap() // panics on error
}

// Correct
fn read_config() -> Result<String, io::Error> {
    fs::read_to_string("config.txt") // Returns Result, ? propagates errors
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let config = read_config()?;
    println!("Config: {}", config);
    Ok(())
}
```

### Fix 3: Use unwrap_or for default values

```rust
use std::fs;

// Wrong
let content = fs::read_to_string("config.txt").unwrap();

// Correct
let content = fs::read_to_string("config.txt")
    .unwrap_or_else(|e| {
        eprintln!("Warning: could not read config: {}", e);
        String::from("default_config")
    });
```

### Fix 4: Use map_err to convert error types

```rust
use std::fs;
use std::io;

fn read_config() -> Result<String, String> {
    fs::read_to_string("config.txt")
        .map_err(|e| format!("Failed to read config: {}", e))
}

fn main() {
    match read_config() {
        Ok(content) => println!("Config: {}", content),
        Err(e) => eprintln!("Error: {}", e),
    }
}
```

## Examples

```rust
use std::fs;

fn main() {
    // This panics because the file doesn't exist
    let content = fs::read_to_string("missing_file.txt").unwrap();
    println!("Content: {}", content);
}
```

Output:
```
thread 'main' panicked at 'called `Result::unwrap()` on an `Err` value: Os { code: 2, kind: NotFound, message: "No such file or directory" }'
```

## Related Errors

- [Unwrap None]({{< relref "/languages/rust/unwrap-none" >}}) — calling unwrap on a None Option.
- [Expect Fail]({{< relref "/languages/rust/expect-fail" >}}) — calling expect on an Err Result.
- [File Not Found]({{< relref "/languages/rust/file-not-found" >}}) — the specific IO error for missing files.
