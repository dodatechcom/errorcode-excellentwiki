---
title: "[Solution] Rust I/O Error — Input/Output Failure"
description: "Fix Rust I/O error. Learn about common IO error kinds in Rust and how to handle them with match, ?, and error context."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# I/O Error — Input/Output Failure

An error with the message "I/O error: ..." occurs when a Rust program encounters a problem during input/output operations — filesystem, network, pipes, or devices.

## Description

Rust's `std::io::Error` wraps OS-level error codes with an `ErrorKind` enum classifying the failure (`NotFound`, `PermissionDenied`, `ConnectionRefused`, etc.). This type is the universal error for all I/O operations.

Common scenarios:

- **File operations** — reading, writing, creating files.
- **Network operations** — socket reads/writes, connections.
- **Pipe operations** — reading from or writing to pipes.
- **Directory operations** — listing, creating directories.
- **Standard I/O** — console operations.

## Common Causes

```rust
use std::fs;

// Cause 1: File not found
let content = fs::read_to_string("missing.txt")?;

// Cause 2: Permission denied
let content = fs::read_to_string("/etc/shadow")?;

// Cause 3: Disk full
let mut file = fs::File::create("/full_disk/out.txt")?;
use std::io::Write;
write!(file, "data")?;

// Cause 4: Connection refused
let stream = std::net::TcpStream::connect("localhost:9999")?;

// Cause 5: Broken pipe
let mut stdout = std::io::stdout();
write!(stdout, "data")?;
```

## Solutions

### Fix 1: Match on ErrorKind

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

### Fix 2: Use ? with custom error types

```rust
use std::fs;
use std::io;

#[derive(Debug)]
enum AppError {
    Io(io::Error),
    Parse(std::num::ParseIntError),
}

impl From<io::Error> for AppError {
    fn from(e: io::Error) -> Self { AppError::Io(e) }
}

impl From<std::num::ParseIntError> for AppError {
    fn from(e: std::num::ParseIntError) -> Self { AppError::Parse(e) }
}

fn read_number(path: &str) -> Result<i32, AppError> {
    let content = fs::read_to_string(path)?;
    let num: i32 = content.trim().parse()?;
    Ok(num)
}
```

### Fix 3: Use anyhow for ergonomic error handling

```rust
use std::fs;

fn read_config(path: &str) -> anyhow::Result<String> {
    let content = fs::read_to_string(path)?;
    Ok(content)
}

fn main() -> anyhow::Result<()> {
    let config = read_config("config.toml")?;
    println!("Config: {} bytes", config.len());
    Ok(())
}
```

### Fix 4: Retry on transient errors

```rust
use std::fs;
use std::io;
use std::thread;
use std::time::Duration;

fn read_with_retry(path: &str, retries: u32) -> io::Result<String> {
    for attempt in 0..retries {
        match fs::read_to_string(path) {
            Ok(content) => return Ok(content),
            Err(e) if e.kind() == io::ErrorKind::Interrupted
                && attempt < retries - 1 =>
            {
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
    match fs::read_to_string("missing.txt") {
        Ok(content) => println!("{}", content),
        Err(e) => eprintln!("I/O error: {}", e),
    }
}
```

Output:
```
I/O error: No such file or directory (os error 2)
```

## Related Errors

- [File Not Found]({{< relref "/languages/rust/file-not-found-2" >}}) — specific file not found error.
- [Permission Denied]({{< relref "/languages/rust/permission-denied-2" >}}) — permission error.
- [Unwrap Err]({{< relref "/languages/rust/unwrap-err-2" >}}) — panicking on I/O error.
