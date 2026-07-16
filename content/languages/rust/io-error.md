---
title: "[Solution] Rust I/O Error — Input/Output Error"
description: "Fix Rust I/O error. Learn about common IO error types in Rust and how to handle them with proper error handling."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
tags: ["io", "error", "filesystem", "network", "read", "write"]
weight: 5
---

# I/O Error — Input/Output Error

An error with the message "I/O error: ..." occurs when a Rust program encounters a problem during input/output operations. This is a broad category covering filesystem, network, and device I/O failures.

## Description

Rust's `std::io::Error` is the general-purpose error type for I/O operations. It wraps OS-level error codes and provides context about what went wrong. The error includes a `ErrorKind` enum that classifies the failure (e.g., `NotFound`, `PermissionDenied`, `ConnectionRefused`).

Common scenarios:

- **File operations** — reading, writing, or creating files.
- **Directory operations** — listing, creating, or deleting directories.
- **Network operations** — socket reads/writes, connections.
- **Pipe operations** — reading from or writing to pipes.
- **Standard input/output** — console operations.

## Common Causes

```rust
use std::fs;
use std::io;

// Cause 1: File not found
let content = fs::read_to_string("nonexistent.txt")?;

// Cause 2: Permission denied
let content = fs::read_to_string("/root/secret.txt")?;

// Cause 3: Disk full
let mut file = fs::File::create("/full_disk/output.txt")?;
use std::io::Write;
write!(file, "data")?;

// Cause 4: Broken pipe
let mut stdout = io::stdout();
write!(stdout, "data")?;

// Cause 5: Connection refused
let stream = std::net::TcpStream::connect("localhost:9999")?;
```

## Solutions

### Fix 1: Match on ErrorKind for specific handling

```rust
use std::fs;
use std::io::{self, ErrorKind};

fn read_file(path: &str) -> io::Result<String> {
    fs::read_to_string(path).map_err(|e| {
        match e.kind() {
            ErrorKind::NotFound => {
                eprintln!("File not found: {}", path);
                e
            }
            ErrorKind::PermissionDenied => {
                eprintln!("Permission denied: {}", path);
                e
            }
            _ => {
                eprintln!("IO error reading {}: {}", path, e);
                e
            }
        }
    })
}
```

### Fix 2: Use the ? operator with From implementation

```rust
use std::fs;
use std::io;

#[derive(Debug)]
enum AppError {
    Io(io::Error),
    Parse(std::num::ParseIntError),
}

impl From<io::Error> for AppError {
    fn from(e: io::Error) -> Self {
        AppError::Io(e)
    }
}

impl From<std::num::ParseIntError> for AppError {
    fn from(e: std::num::ParseIntError) -> Self {
        AppError::Parse(e)
    }
}

fn read_number(path: &str) -> Result<i32, AppError> {
    let content = fs::read_to_string(path)?; // converts io::Error to AppError
    let num: i32 = content.trim().parse()?; // converts ParseIntError to AppError
    Ok(num)
}
```

### Fix 3: Use anyhow for ergonomic error handling

```toml
# Cargo.toml
[dependencies]
anyhow = "1"
```

```rust
use std::fs;

fn read_config(path: &str) -> anyhow::Result<String> {
    let content = fs::read_to_string(path)?;
    Ok(content)
}

fn main() -> anyhow::Result<()> {
    let config = read_config("config.toml")?;
    println!("Config: {}", config);
    Ok(())
}
```

### Fix 4: Retry operations on transient errors

```rust
use std::fs;
use std::io;
use std::thread;
use std::time::Duration;

fn read_with_retry(path: &str, max_retries: u32) -> io::Result<String> {
    for attempt in 0..max_retries {
        match fs::read_to_string(path) {
            Ok(content) => return Ok(content),
            Err(e) if e.kind() == io::ErrorKind::Interrupted && attempt < max_retries - 1 => {
                thread::sleep(Duration::from_millis(100 * (attempt as u64 + 1)));
                continue;
            }
            Err(e) => return Err(e),
        }
    }
    unreachable!()
}
```

## Examples

```rust
use std::fs;

fn main() {
    match fs::read_to_string("config.txt") {
        Ok(content) => println!("Config: {}", content),
        Err(e) => eprintln!("I/O error: {}", e),
    }
}
```

Output (if file doesn't exist):
```
I/O error: No such file or directory (os error 2)
```

## Related Errors

- [File Not Found]({{< relref "/languages/rust/file-not-found" >}}) — specific IO error for missing files.
- [Permission Denied]({{< relref "/languages/rust/permission-denied" >}}) — specific IO error for permission issues.
- [Unwrap Err]({{< relref "/languages/rust/unwrap-err" >}}) — panicking on IO error with unwrap.
