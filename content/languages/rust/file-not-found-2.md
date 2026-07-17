---
title: "[Solution] Rust File Not Found — No Such File or Directory"
description: "Fix Rust file not found error. Learn why file operations fail with 'No such file or directory' and how to handle missing files."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# File Not Found — No Such File or Directory

An IO error with the message "No such file or directory (os error 2)" occurs when you try to access a file at a path that doesn't exist.

## Description

When you call `fs::read_to_string`, `File::open`, or any file operation with a path that doesn't exist, the OS returns error code 2 (`ENOENT`). Rust wraps this as `io::Error` with kind `NotFound`.

Common scenarios:

- **Typo in filename** — `config.tml` instead of `config.toml`.
- **Wrong directory** — file is in `./data/` but you used `./`.
- **File not yet created** — program expects output file before creating it.
- **Relative vs absolute path** — current directory differs from expected.

## Common Causes

```rust
use std::fs;

// Cause 1: Typo
let content = fs::read_to_string("config.ttml")?; // should be .toml

// Cause 2: Wrong directory
let content = fs::read_to_string("data/config.toml")?; // file is in root

// Cause 3: File doesn't exist yet
let content = fs::read_to_string("output.txt")?; // not created yet

// Cause 4: Path built incorrectly
let dir = "data";
let path = format!("{}/file.txt", dir);
let content = fs::read_to_string(&path)?; // "data/file.txt" doesn't exist
```

## Solutions

### Fix 1: Check existence first

```rust
use std::path::Path;

let path = Path::new("config.toml");
if path.exists() {
    let content = std::fs::read_to_string(path)?;
    println!("Config: {} bytes", content.len());
} else {
    println!("Config not found, using defaults");
}
```

### Fix 2: Provide a default value

```rust
use std::fs;

fn load_config(path: &str) -> String {
    fs::read_to_string(path).unwrap_or_else(|e| {
        eprintln!("Warning: {}: {}", path, e);
        String::from("[defaults]\nport = 8080")
    })
}

fn main() {
    let config = load_config("config.toml");
    println!("{}", config);
}
```

### Fix 3: Create the file if missing

```rust
use std::fs;
use std::path::Path;

fn ensure_file(path: &str, default: &str) -> std::io::Result<String> {
    if !Path::new(path).exists() {
        fs::write(path, default)?;
        println!("Created {}", path);
    }
    fs::read_to_string(path)
}

fn main() -> std::io::Result<()> {
    let content = ensure_file("config.toml", "[server]\nport = 8080")?;
    println!("{}", content);
    Ok(())
}
```

### Fix 4: Use canonicalize to resolve paths

```rust
use std::path::PathBuf;
use std::fs;

fn find_file(name: &str) -> Option<PathBuf> {
    let path = PathBuf::from(name);
    if path.exists() {
        fs::canonicalize(path).ok()
    } else {
        let cwd = std::env::current_dir().ok()?;
        let full = cwd.join(name);
        if full.exists() { fs::canonicalize(full).ok() } else { None }
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

- [IO Error]({{< relref "/languages/rust/io-error-2" >}}) — general I/O error handling.
- [Permission Denied]({{< relref "/languages/rust/permission-denied-2" >}}) — file exists but can't access.
- [Unwrap Err]({{< relref "/languages/rust/unwrap-err-2" >}}) — panicking on file operation failure.
