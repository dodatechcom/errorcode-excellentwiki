---
title: "[Solution] Rust Permission Denied — File Access Forbidden"
description: "Fix Rust permission denied error. Learn why file operations fail with 'Permission denied' and how to handle file permissions in Rust."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Permission Denied — File Access Forbidden

An IO error with the message "Permission denied (os error 13)" occurs when your process lacks the OS-level permissions required for a file operation.

## Description

Operating systems control file access via permissions. When your Rust process doesn't have the required permission, the OS returns error code 13 (`EACCES`). This can happen for read, write, or execute operations.

Common scenarios:

- **Reading system files** — `/etc/shadow`, `/etc/sudoers`.
- **Writing to system dirs** — `/usr/bin`, `/etc`.
- **Executing without +x** — running scripts without execute permission.
- **Files owned by root** — regular user accessing root-owned files.
- **Directory not writable** — creating files in read-only directories.

## Common Causes

```rust
use std::fs;

// Cause 1: Reading protected file
let content = fs::read_to_string("/etc/shadow")?;

// Cause 2: Writing to system directory
fs::write("/usr/bin/myfile", "data")?;

// Cause 3: Executing without permission
std::process::Command::new("./myscript.sh").output()?;

// Cause 4: Accessing another user's files
let content = fs::read_to_string("/root/.ssh/id_rsa")?;
```

## Solutions

### Fix 1: Check permissions before access

```rust
use std::fs;
use std::os::unix::fs::PermissionsExt;

fn check_permissions(path: &str) -> std::io::Result<()> {
    let meta = fs::metadata(path)?;
    let perm = meta.permissions();
    println!("Read: {}", perm.mode() & 0o400 != 0);
    println!("Write: {}", perm.mode() & 0o200 != 0);
    println!("Execute: {}", perm.mode() & 0o100 != 0);
    Ok(())
}
```

### Fix 2: Handle permission errors gracefully

```rust
use std::fs;
use std::io;

fn read_file(path: &str) -> Option<String> {
    match fs::read_to_string(path) {
        Ok(content) => Some(content),
        Err(e) if e.kind() == io::ErrorKind::PermissionDenied => {
            eprintln!("Permission denied: {}", path);
            None
        }
        Err(e) => {
            eprintln!("Error reading {}: {}", path, e);
            None
        }
    }
}
```

### Fix 3: Use user-writable directories

```rust
use std::fs;
use std::path::PathBuf;

fn get_data_dir() -> PathBuf {
    if let Some(home) = std::env::var_os("HOME") {
        PathBuf::from(home).join(".myapp")
    } else {
        PathBuf::from("/tmp/myapp")
    }
}

fn main() -> std::io::Result<()> {
    let dir = get_data_dir();
    fs::create_dir_all(&dir)?;
    fs::write(dir.join("config.toml"), "[server]\nport = 8080")?;
    println!("Config written to {}", dir.display());
    Ok(())
}
```

### Fix 4: Use sudo for system-level operations

```rust
use std::process::Command;

fn main() -> std::io::Result<()> {
    let output = Command::new("sudo")
        .args(&["tee", "/etc/myapp/config.conf"])
        .output()?;
    if !output.status.success() {
        eprintln!("Failed to write config");
    }
    Ok(())
}
```

## Examples

```rust
use std::fs;

fn main() {
    match fs::read_to_string("/etc/shadow") {
        Ok(content) => println!("{}", content),
        Err(e) => eprintln!("Error: {}", e),
    }
}
```

Output:
```
Error: Permission denied (os error 13)
```

## Related Errors

- [File Not Found]({{< relref "/languages/rust/file-not-found-2" >}}) — file doesn't exist.
- [IO Error]({{< relref "/languages/rust/io-error-2" >}}) — general I/O error handling.
- [Unwrap Err]({{< relref "/languages/rust/unwrap-err-2" >}}) — panicking on permission error.
