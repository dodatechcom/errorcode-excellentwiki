---
title: "[Solution] tempdir Create Error Fix"
description: "Fix tempdir creation errors. Handle permission issues, disk space, and cleanup."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# tempdir Create Error

The `tempdir` crate (now superseded by the `tempfile` crate) creates temporary directories that are automatically deleted when the `TempDir` value is dropped. Errors occur when the system's temporary directory is not writable, when disk space is exhausted, or when the directory name collides with an existing file. The `tempfile::TempDir` type provides the same functionality with better error handling and cross-platform support.

## Common Causes

```rust
use tempfile::TempDir;

// 1. Permission denied on temp directory
// On some systems /tmp may be mounted read-only or restricted

// 2. Disk full — cannot create directory
// tempfile will fail with io::Error if /tmp is full

// 3. Path component issues
let dir = TempDir::new_in("/nonexistent/path");
// Fails: parent directory doesn't exist

// 4. TempDir dropped before contents are flushed
let dir = TempDir::new()?;
let path = dir.path().join("data.bin");
std::fs::write(&path, b"hello")?;
drop(dir); // Directory deleted — file gone before you read it back
```

## How to Fix

1. **Use tempfile with proper error handling**

```rust
use tempfile::TempDir;
use std::fs;

fn process_with_temp_dir() -> Result<(), Box<dyn std::error::Error>> {
    let dir = TempDir::new()?;
    let file_path = dir.path().join("output.txt");

    fs::write(&file_path, "Hello, temporary world!")?;
    let content = fs::read_to_string(&file_path)?;
    println!("Read: {}", content);

    // Dir auto-deleted when `dir` goes out of scope
    Ok(())
}
```

2. **Persist the temp directory when you need it beyond scope**

```rust
use tempfile::TempDir;
use std::fs;

let dir = TempDir::new()?;
let file_path = dir.path().join("data.json");
fs::write(&file_path, r#"{"key": "value"}"#)?;

// Keep the directory alive — don't drop it
let persistent_path = dir.into_path(); // Returns PathBuf, skips cleanup
println!("Directory at: {}", persistent_path.display());
// Must manually clean up persistent_path later
```

3. **Use named temp files for specific filenames**

```rust
use tempfile::NamedTempFile;
use std::io::{Write, Read};

let mut file = NamedTempFile::new()?;
writeln!(file, "temporary data")?;

// Read it back
let mut content = String::new();
file.read_to_string(&mut content)?;
println!("Content: {}", content);

// Rename to final location atomically
let final_path = std::path::PathBuf::from("/tmp/final_output.txt");
file.persist(&final_path)?;
```

4. **Create temp files in a specific directory with a prefix**

```rust
use tempfile::Builder;

let dir = Builder::new()
    .prefix("myapp_")
    .tempdir()?;

let file = Builder::new()
    .prefix("data_")
    .suffix(".csv")
    .tempfile_in(dir.path())?;

println!("Temp dir: {}", dir.path().display());
println!("Temp file: {}", file.path().display());
```

## Examples

```rust
use tempfile::{TempDir, NamedTempFile};
use std::fs;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Create a temporary directory
    let temp_dir = TempDir::new()?;
    println!("Temp dir: {}", temp_dir.path().display());

    // Write multiple files
    for i in 0..5 {
        let path = temp_dir.path().join(format!("file_{}.txt", i));
        fs::write(&path, format!("Content of file {}", i))?;
    }

    // List files
    for entry in fs::read_dir(temp_dir.path())? {
        let entry = entry?;
        println!("  {} ({} bytes)",
            entry.file_name().to_string_lossy(),
            entry.metadata()?.len()
        );
    }

    // dir is automatically cleaned up here
    Ok(())
}
```

## Related Errors

- [Walkdir Error]({{< relref "/languages/rust/walkdir-error" >}}) — directory traversal
- [FS Extra Error]({{< relref "/languages/rust/fs-extra-error" >}}) — filesystem operations
- [Std FS Error]({{< relref "/languages/rust/rust-std-fs-error" >}}) — std filesystem
