---
title: "[Solution] fs_extra File Operation Error Fix"
description: "Fix fs_extra file operation errors. Handle copy, move, and directory operations."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# FS Extra Error

FS extra errors occur when using the `fs_extra` crate for extended filesystem operations — copy failures and space issues.

## Common Causes

```rust
// Copy to non-existent destination
fs_extra::dir::copy("src", "/nonexistent", &CopyOptions::new());

// Insufficient disk space
// Copy large directory to small partition
```

## How to Fix

1. **Ensure destination exists**

```rust
use fs_extra::dir;
use std::fs;

fs::create_dir_all("/destination")?;
dir::copy("src", "/destination", &CopyOptions::new())?;
```

2. **Check disk space before large copies**

```rust
use std::path::Path;

fn has_space(path: &Path, needed: u64) -> bool {
    // Platform-specific check
    true // Simplified
}
```

## Examples

```rust
use fs_extra::dir::{self, CopyOptions};

fn main() {
    let mut options = CopyOptions::new();
    options.overwrite = true;

    match dir::copy("source_dir", "/tmp/backup", &options) {
        Ok(_) => println!("Copy succeeded"),
        Err(e) => eprintln!("Copy failed: {}", e),
    }
}
```

## Related Errors

- [Std FS Error]({{< relref "/languages/rust/rust-std-fs-error" >}}) — std filesystem
- [Walkdir Error]({{< relref "/languages/rust/walkdir-error" >}}) — directory traversal
- [Notify Error]({{< relref "/languages/rust/notify-error" >}}) — filesystem watching
