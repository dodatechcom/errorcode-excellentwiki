---
title: "[Solution] Rust File Not Found — No Such File or Directory"
description: "Fix Rust file not found error. Learn why file operations fail with 'No such file or directory' and how to handle missing files properly."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
tags: ["file", "not-found", "io", "filesystem", "path"]
weight: 5
---

# File Not Found — No Such File or Directory

An IO error with the message "No such file or directory (os error 2)" occurs when you try to read, write, or open a file that doesn't exist at the specified path.

## Description

Rust's file operations rely on the operating system's file system. When you specify a path that doesn't exist, the OS returns error code 2 (`ENOENT`), which Rust wraps as `io::Error` with kind `NotFound`. This is one of the most common IO errors.

Common scenarios:

- **Typo in file path** — misspelled filename or directory.
- **Relative vs absolute path** — file exists but at a different location.
- **File deleted** — file existed when code was written but is gone now.
- **Permission on parent directory** — can't traverse to the file.

## Common Causes

```rust
use std::fs;

// Cause 1: Typo in filename
let content = fs::read_to_string("config.ttml")?; // should be "config.toml"

// Cause 2: Wrong directory
let content = fs::read_to_string("data/config.toml")?; // file is in root

// Cause 3: File not yet created
let content = fs::read_to_string("output.txt")?; // program hasn't created it yet

// Cause 4: Path constructed incorrectly
let filename = "data";
let path = format!("{}/file.txt", filename);
let content = fs::read_to_string(&path)?; // "data/file.txt" doesn't exist
```

## Solutions

### Fix 1: Check if file exists before reading

```rust
use std::path::Path;

// Wrong
let content = fs::read_to_string("config.toml")?;

// Correct
let path = Path::new("config.toml");
if path.exists() {
    let content = fs::read_to_string(path)?;
    println!("Config: {}", content);
} else {
    println!("Config file not found, using defaults");
}
```

### Fix 2: Use default values for missing files

```rust
use std::fs;

fn load_config(path: &str) -> String {
    fs::read_to_string(path).unwrap_or_else(|e| {
        eprintln!("Warning: {}: {}, using default config", path, e);
        String::from("[defaults]\nkey = value")
    })
}

fn main() {
    let config = load_config("config.toml");
    println!("{}", config);
}
```

### Fix 3: Create the file if it doesn't exist

```rust
use std::fs;
use std::path::Path;

fn ensure_config(path: &str) -> std::io::Result<String> {
    let path = Path::new(path);
    if !path.exists() {
        fs::write(path, "[config]\nkey = value")?;
        println!("Created default config at {}", path.display());
    }
    fs::read_to_string(path)
}

fn main() -> std::io::Result<()> {
    let config = ensure_config("config.toml")?;
    println!("Config: {}", config);
    Ok(())
}
```

### Fix 4: Use canonicalize to resolve paths

```rust
use std::fs;
use std::path::PathBuf;

fn find_file(name: &str) -> Option<PathBuf> {
    let path = PathBuf::from(name);
    if path.exists() {
        Some(fs::canonicalize(path).ok()?)
    } else {
        // Try relative to current directory
        let cwd = std::env::current_dir().ok()?;
        let full_path = cwd.join(name);
        if full_path.exists() {
            Some(fs::canonicalize(full_path).ok()?)
        } else {
            None
        }
    }
}
```

## Examples

```rust
use std::fs;

fn main() {
    let content = fs::read_to_string("does_not_exist.txt")
        .expect("Failed to read file");
    println!("{}", content);
}
```

Output:
```
thread 'main' panicked at 'Failed to read file: Os { code: 2, kind: NotFound, message: "No such file or directory" }'
```

## Related Errors

- [IO Error]({{< relref "/languages/rust/io-error" >}}) — general IO error handling.
- [Permission Denied]({{< relref "/languages/rust/permission-denied" >}}) — file exists but can't access it.
- [Unwrap Err]({{< relref "/languages/rust/unwrap-err" >}}) — panicking on file operation failure.
