---
title: "[Solution] Rust Out of Memory — Memory Allocation Failed"
description: "Fix Rust out of memory error. Learn why memory allocation fails and how to use try_reserve and streaming to avoid OOM."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
tags: ["memory", "allocation", "oom", "heap", "vec", "try_reserve"]
weight: 5
---

# Out of Memory — Memory Allocation Failed

A panic with the message "memory allocation failed" occurs when the system cannot allocate more memory for the Rust process.

## Description

Rust allocates heap memory through the system allocator. When the process hits system limits (physical RAM + swap, or per-process cgroups), allocation fails. Unlike stack overflow (which is per-thread), OOM affects the entire process.

Common scenarios:

- **Huge Vec creation** — `vec![0u8; u64::MAX]`.
- **Reading large files into memory** — `fs::read_to_string` on a huge file.
- **Collecting large iterators** — materializing millions of elements.
- **Unbounded string growth** — appending in a loop.
- **Memory leaks** — accumulating data without releasing.

## Common Causes

```rust
// Cause 1: Enormous Vec
let data = vec![0u8; 1_000_000_000_000]; // 1 TB

// Cause 2: Large file read
use std::fs;
let content = fs::read_to_string("/dev/zero"); // or huge file

// Cause 3: String growth in loop
let mut s = String::new();
for _ in 0..1_000_000_000 {
    s.push_str("hello");
}

// Cause 4: Exponential cloning
let mut v = vec![1];
for _ in 0..100 {
    let mut new = v.clone();
    new.append(&mut v);
    v = new;
}
```

## Solutions

### Fix 1: Use try_reserve for fallible allocation

```rust
fn safe_alloc(size: usize) -> Option<Vec<u8>> {
    let mut v = Vec::new();
    if v.try_reserve_exact(size).is_ok() {
        v.resize(size, 0);
        Some(v)
    } else {
        None
    }
}

fn main() {
    match safe_alloc(1_000_000) {
        Some(data) => println!("Allocated {} bytes", data.len()),
        None => eprintln!("Not enough memory"),
    }
}
```

### Fix 2: Stream data instead of loading entirely

```rust
use std::fs::File;
use std::io::{BufRead, BufReader};

fn process_file(path: &str) -> std::io::Result<()> {
    let file = File::open(path)?;
    let reader = BufReader::new(file);
    for line in reader.lines() {
        let line = line?;
        println!("{}", line);
    }
    Ok(())
}
```

### Fix 3: Use HashMap::try_reserve

```rust
use std::collections::HashMap;

fn main() {
    let mut map = HashMap::new();
    match map.try_reserve(1_000_000) {
        Ok(()) => {
            for i in 0..1_000_000 {
                map.insert(i, i * 2);
            }
            println!("Map has {} entries", map.len());
        }
        Err(e) => eprintln!("Allocation failed: {}", e),
    }
}
```

### Fix 4: Use memory-mapped files

```rust
use std::fs::File;
use memmap2::Mmap;

fn main() -> std::io::Result<()> {
    let file = File::open("large.bin")?;
    let mmap = unsafe { Mmap::map(&file)? };
    println!("First byte: {}", mmap[0]);
    Ok(())
}
```

## Examples

```rust
fn main() {
    let data = vec![0u8; 100_000_000_000];
    println!("Allocated: {} bytes", data.len());
}
```

Output:
```
thread 'main' panicked at 'memory allocation failed'
```

## Related Errors

- [Stack Overflow]({{< relref "/languages/rust/stack-overflow-2" >}}) — thread stack exhaustion.
- [Overflow]({{< relref "/languages/rust/overflow-2" >}}) — arithmetic overflow.
- [IO Error]({{< relref "/languages/rust/io-error-2" >}}) — general I/O errors.
