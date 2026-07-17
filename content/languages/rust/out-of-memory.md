---
title: "[Solution] Rust Out of Memory — Memory Allocation Failed"
description: "Fix Rust out of memory error. Learn why memory allocation fails and how to handle OOM conditions with proper resource management."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Out of Memory — Memory Allocation Failed

A panic with the message "memory allocation failed" occurs when the system cannot allocate more memory for the Rust process. This typically happens when trying to create a collection that is too large.

## Description

Rust uses the system allocator (or a custom allocator) to allocate heap memory. When the system runs out of memory — either physical RAM + swap or per-process limits — the allocation fails and Rust panics. This is different from stack overflow, which is about thread stack space.

Common scenarios:

- **Creating a very large Vec** — `vec![0u8; u64::MAX]`.
- **Loading large files into memory** — reading entire files into a `String`.
- **Collecting iterators** — materializing huge iterator results.
- **String concatenation** — building extremely long strings.
- **Memory leaks** — accumulating data without releasing it.

## Common Causes

```rust
// Cause 1: Creating a huge Vec
let data = vec![0u8; 1_000_000_000_000]; // 1 TB, will fail

// Cause 2: Loading large file content
use std::fs;
let huge_file = fs::read_to_string("/dev/zero"); // or any very large file

// Cause 3: Collecting large iterator
let big: Vec<i32> = (0..i64::MAX as i32).collect();

// Cause 4: String concatenation in loop
let mut s = String::new();
for _ in 0..1_000_000_000 {
    s.push_str("hello"); // grows without bound
}

// Cause 5: Recursive cloning
let mut v = vec![1];
for _ in 0..100 {
    let mut new_v = v.clone();
    new_v.append(&mut v);
    v = new_v;
}
```

## Solutions

### Fix 1: Check available memory before large allocations

```rust
// Wrong
let data = vec![0u8; huge_number];

// Correct — use checked allocation
fn safe_vec_fill(size: usize) -> Option<Vec<u8>> {
    let mut v = Vec::new();
    if v.try_reserve_exact(size).is_ok() {
        v.resize(size, 0);
        Some(v)
    } else {
        None
    }
}

fn main() {
    match safe_vec_fill(1_000_000) {
        Some(data) => println!("Allocated {} bytes", data.len()),
        None => eprintln!("Not enough memory"),
    }
}
```

### Fix 2: Stream data instead of loading into memory

```rust
use std::fs::File;
use std::io::{self, BufRead, BufReader};

// Wrong — loads entire file into memory
fn read_all(path: &str) -> io::Result<String> {
    std::fs::read_to_string(path)
}

// Correct — process line by line
fn process_file(path: &str) -> io::Result<()> {
    let file = File::open(path)?;
    let reader = BufReader::new(file);

    for line in reader.lines() {
        let line = line?;
        println!("{}", line);
    }
    Ok(())
}
```

### Fix 3: Use try_reserve for fallible allocation

```rust
use std::collections::HashMap;

fn main() {
    let mut map = HashMap::new();

    // Try to reserve space for many entries
    match map.try_reserve(1_000_000) {
        Ok(()) => {
            for i in 0..1_000_000 {
                map.insert(i, i * 2);
            }
            println!("Map has {} entries", map.len());
        }
        Err(e) => {
            eprintln!("Failed to allocate: {}", e);
        }
    }
}
```

### Fix 4: Use memory-mapped files for large data

```rust
// For very large files, use memory mapping instead of reading into memory
use std::fs::File;
use memmap2::Mmap;

fn main() -> std::io::Result<()> {
    let file = File::open("large_file.bin")?;
    let mmap = unsafe { Mmap::map(&file)? };

    // Access data without loading entire file into memory
    println!("First byte: {}", mmap[0]);
    Ok(())
}
```

## Examples

```rust
fn main() {
    // Attempting to allocate 100 GB
    let data = vec![0u8; 100_000_000_000];
    println!("Allocated: {} bytes", data.len());
}
```

Output:
```
thread 'main' panicked at 'memory allocation failed'
```

## Related Errors

- [Stack Overflow]({{< relref "/languages/rust/stack-overflow" >}}) — thread stack memory exhausted.
- [Overflow]({{< relref "/languages/rust/overflow" >}}) — arithmetic overflow.
- [IO Error]({{< relref "/languages/rust/io-error" >}}) — general IO errors including resource exhaustion.
