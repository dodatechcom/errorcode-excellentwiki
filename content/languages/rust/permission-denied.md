---
title: "[Solution] Rust Permission Denied — File Access Error"
description: "Fix Rust permission denied error. Learn why file operations fail with 'Permission denied' and how to handle file permissions in Rust."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Permission Denied — File Access Error

An IO error with the message "Permission denied (os error 13)" occurs when you try to read, write, or execute a file without the necessary operating system permissions.

## Description

The operating system controls file access through permissions (Unix-style `chmod` or Windows ACLs). When your Rust process doesn't have the required permission for a file operation, the OS returns error code 13 (`EACCES`), which Rust wraps as `io::Error` with kind `PermissionDenied`.

Common scenarios:

- **Reading protected files** — `/etc/shadow`, system config files.
- **Writing to system directories** — `/usr/bin`, `/etc`.
- **Executing without +x** — running scripts without execute permission.
- **Owned by another user** — files owned by root or another user.
- **Directory not writable** — trying to create files in read-only directories.

## Common Causes

```rust
use std::fs;

// Cause 1: Reading a system-protected file
let content = fs::read_to_string("/etc/shadow")?;

// Cause 2: Writing to a system directory
fs::write("/usr/bin/myfile", "data")?;

// Cause 3: Creating files in a read-only directory
fs::write("/read-only-dir/file.txt", "data")?;

// Cause 4: Running a script without execute permission
std::process::Command::new("./myscript.sh").output()?;

// Cause 5: Opening a file owned by another user
let file = std::fs::File::open("/root/.ssh/id_rsa")?;
```

## Solutions

### Fix 1: Check permissions before accessing

```rust
use std::fs;
use std::os::unix::fs::PermissionsExt;

fn check_permissions(path: &str) -> std::io::Result<()> {
    let metadata = fs::metadata(path)?;
    let permissions = metadata.permissions();

    println!("Read: {}", permissions.mode() & 0o400 != 0);
    println!("Write: {}", permissions.mode() & 0o200 != 0);
    println!("Execute: {}", permissions.mode() & 0o100 != 0);

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
            eprintln!("Permission denied reading {}: {}", path, e);
            None
        }
        Err(e) => {
            eprintln!("Error reading {}: {}", path, e);
            None
        }
    }
}
```

### Fix 3: Use alternative paths that are writable

```rust
use std::fs;
use std::path::PathBuf;

fn get_data_dir() -> PathBuf {
    // Use user's home directory instead of system directories
    if let Some(home) = std::env::var_os("HOME") {
        PathBuf::from(home).join(".myapp")
    } else {
        PathBuf::from("/tmp/myapp")
    }
}

fn main() -> std::io::Result<()> {
    let data_dir = get_data_dir();
    fs::create_dir_all(&data_dir)?;

    let config_path = data_dir.join("config.toml");
    fs::write(&config_path, "[config]\nkey = value")?;
    println!("Config written to {}", config_path.display());
    Ok(())
}
```

### Fix 4: Use sudo for system-level operations (carefully)

```rust
use std::process::Command;

fn main() -> std::io::Result<()> {
    // Only use sudo when absolutely necessary
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

- [File Not Found]({{< relref "/languages/rust/file-not-found" >}}) — file doesn't exist.
- [IO Error]({{< relref "/languages/rust/io-error" >}}) — general IO error handling.
- [Unwrap Err]({{< relref "/languages/rust/unwrap-err" >}}) — panicking on permission error.
