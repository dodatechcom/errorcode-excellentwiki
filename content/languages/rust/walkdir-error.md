---
title: "[Solution] walkdir Directory Walk Error Fix"
description: "Fix walkdir directory walk errors. Handle permission issues, symlink loops, and depth limits."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# walkdir Directory Walk Error

The `walkdir` crate provides a recursive directory walker with support for following symlinks, filtering by depth, and customising traversal. Errors occur when the walker encounters permission-denied directories, circular symlinks, or when files are deleted between listing and access. The `WalkDir` iterator yields `Result<DirEntry>` values.

## Common Causes

```rust
use walkdir::WalkDir;

// 1. Permission denied on a subdirectory
// walkdir will yield Err for directories it can't read
for entry in WalkDir::new("/root") {
    match entry {
        Ok(entry) => println!("{}", entry.path().display()),
        Err(e) => eprintln!("Error walking {}: {}", e.path().display(), e),
    }
}

// 2. Infinite symlink loops — walkdir follows symlinks by default
// /a/link -> /a creates infinite recursion
let walker = WalkDir::new("/a/link"); // walks forever

// 3. Following symlinks outside the root directory
// Default follows_links(false) still follows symlinks for some operations

// 4. Max depth reached
let walker = WalkDir::new("/").max_depth(1);
// Only immediate children
```

## How to Fix

1. **Handle permission errors gracefully**

```rust
use walkdir::WalkDir;

for entry in WalkDir::new("/var/log").into_iter().filter_map(|e| e.ok()) {
    println!("{}", entry.path().display());
}

// Or handle errors explicitly
for entry in WalkDir::new("/var/log") {
    match entry {
        Ok(entry) => {
            if entry.file_type().is_file() {
                println!("File: {}", entry.path().display());
            }
        }
        Err(e) => {
            eprintln!("Skipped: {} ({})", e.path().display(), e);
            // Continue walking despite errors
        }
    }
}
```

2. **Prevent symlink loops with max_depth and no_follow**

```rust
use walkdir::WalkDir;

// Don't follow symlinks — prevents infinite loops
let walker = WalkDir::new("/data")
    .follow_links(false)
    .max_depth(10);

for entry in walker {
    match entry {
        Ok(entry) => println!("{}", entry.path().display()),
        Err(e) => eprintln!("Error: {}", e),
    }
}
```

3. **Filter by file type and depth**

```rust
use walkdir::WalkDir;

// Only files (not directories), max depth 3
let rust_files: Vec<_> = WalkDir::new("src")
    .max_depth(3)
    .into_iter()
    .filter_map(|e| e.ok())
    .filter(|e| e.file_type().is_file())
    .filter(|e| e.path().extension().map_or(false, |ext| ext == "rs"))
    .collect();

println!("Found {} Rust files", rust_files.len());
for file in &rust_files {
    println!("  {}", file.path().display());
}
```

4. **Use sorted entries for deterministic output**

```rust
use walkdir::WalkDir;

let entries: Vec<_> = WalkDir::new(".")
    .sort_by_file_name()
    .into_iter()
    .filter_map(|e| e.ok())
    .collect();

for entry in &entries {
    let depth = entry.depth();
    let indent = "  ".repeat(depth);
    println!("{}{}", indent, entry.file_name().to_string_lossy());
}
```

## Examples

```rust
use walkdir::WalkDir;
use std::path::Path;

fn count_by_extension(dir: &str) -> std::collections::HashMap<String, usize> {
    let mut counts = std::collections::HashMap::new();

    for entry in WalkDir::new(dir)
        .into_iter()
        .filter_map(|e| e.ok())
        .filter(|e| e.file_type().is_file())
    {
        let ext = entry.path()
            .extension()
            .and_then(|e| e.to_str())
            .unwrap_or("no_ext")
            .to_string();
        *counts.entry(ext).or_insert(0) += 1;
    }
    counts
}

fn main() {
    let counts = count_by_extension(".");
    let mut sorted: Vec<_> = counts.into_iter().collect();
    sorted.sort_by(|a, b| b.1.cmp(&a.1));

    for (ext, count) in sorted {
        println!("{:>5} .{}", count, ext);
    }
}
```

## Related Errors

- [Glob Error]({{< relref "/languages/rust/glob-error" >}}) — glob patterns
- [Notify Error]({{< relref "/languages/rust/notify-error" >}}) — filesystem watching
- [Std FS Error]({{< relref "/languages/rust/rust-std-fs-error" >}}) — filesystem ops
