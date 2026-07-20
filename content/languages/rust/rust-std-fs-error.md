---
title: "[Solution] Rust Std FS Error — How to Fix"
description: "Fix standard library filesystem errors. Resolve file creation, permission, and path issues."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Std FS Error

Std fs errors occur when using `std::fs` functions — file not found, permission denied, disk full, or path resolution failures.

## Common Causes

```rust
// File not found
let content = std::fs::read_to_string("missing.txt").unwrap(); // PANICS

// Permission denied
let content = std::fs::read_to_string("/root/secret.txt").unwrap(); // PANICS

// Creating directory that already exists
std::fs::create_dir("/existing/dir").unwrap(); // ERROR: already exists

// Disk full
std::fs::write("output.txt", large_data).unwrap(); // ERROR: No space left
```

## How to Fix

1. **Use `Result` types instead of `unwrap()`**

```rust
use std::fs;

fn read_config(path: &str) -> Result<String, Box<dyn std::error::Error>> {
    let content = fs::read_to_string(path)?;
    Ok(content)
}

fn main() {
    match read_config("config.toml") {
        Ok(content) => println!("Config: {}", content),
        Err(e) => eprintln!("Failed to read config: {}", e),
    }
}
```

2. **Check for file existence before operations**

```rust
use std::path::Path;

fn ensure_dir(path: &str) -> std::io::Result<()> {
    if !Path::new(path).exists() {
        std::fs::create_dir_all(path)?;
    }
    Ok(())
}

fn safe_read(path: &str) -> Option<String> {
    if Path::new(path).exists() {
        std::fs::read_to_string(path).ok()
    } else {
        None
    }
}
```

3. **Handle permissions appropriately**

```rust
use std::fs;
use std::os::unix::fs::PermissionsExt;

fn set_executable(path: &str) -> std::io::Result<()> {
    let mut perms = fs::metadata(path)?.permissions();
    perms.set_mode(0o755);
    fs::set_permissions(path, perms)
}
```

## Examples

```rust
use std::fs;
use std::io;

fn main() -> io::Result<()> {
    // Write a file
    fs::write("hello.txt", "Hello, World!")?;

    // Read it back
    let content = fs::read_to_string("hello.txt")?;
    println!("Content: {}", content);

    // Read binary
    let bytes = fs::read("hello.txt")?;
    println!("Bytes: {:?}", bytes);

    // Create directories recursively
    fs::create_dir_all("a/b/c")?;

    // List directory
    for entry in fs::read_dir(".")? {
        let entry = entry?;
        println!("{}: {} bytes",
            entry.file_name().to_string_lossy(),
            entry.metadata()?.len()
        );
    }

    // Cleanup
    fs::remove_file("hello.txt")?;
    fs::remove_dir_all("a")?;

    Ok(())
}
```

## Related Errors

- [Std IO Error]({{< relref "/languages/rust/rust-std-io-error" >}}) — I/O operations
- [IO Error]({{< relref "/languages/rust/io-error" >}}) — general I/O errors
- [Permission Denied]({{< relref "/languages/rust/permission-denied" >}}) — permission issues
