---
title: "[Solution] Rust RwLock Error — How to Fix"
description: "Fix RwLock read-write lock errors. Resolve reader starvation, writer priority, and poisoning issues."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# RwLock Error

RwLock errors occur when using `std::sync::RwLock` or `tokio::sync::RwLock` — poisoning, lock contention, or holding write locks too long.

## Common Causes

```rust
use std::sync::{Arc, RwLock};

// Mutex poisoning
let lock = Arc::new(RwLock::new(vec![1, 2, 3]));
let lock_clone = Arc::clone(&lock);
std::thread::spawn(move || {
    let mut w = lock_clone.write().unwrap();
    w.push(4);
    panic!("Oops!"); // Poisons the lock
}).join().unwrap();
let r = lock.read().unwrap(); // ERROR: lock is poisoned

// Write lock contention — readers blocked
let data = Arc::new(RwLock::new(0));
let data_clone = Arc::clone(&data);
std::thread::spawn(move || {
    let mut w = data_clone.write().unwrap(); // Blocks all readers
    std::thread::sleep(std::time::Duration::from_secs(10));
});

// Holding write lock across await (with tokio)
```

## How to Fix

1. **Recover from poisoned locks**

```rust
use std::sync::RwLock;

let lock = RwLock::new(vec![1, 2, 3]);
let data = lock.write().unwrap_or_else(|poisoned| poisoned.into_inner());
println!("{:?}", *data);
```

2. **Keep write locks short and use read locks for queries**

```rust
use std::sync::{Arc, RwLock};
use std::thread;

let data = Arc::new(RwLock::new(std::collections::HashMap::new()));

// Short write lock
{
    let mut map = data.write().unwrap();
    map.insert("key".to_string(), 42);
} // Lock released here

// Multiple readers can proceed
let readers: Vec<_> = (0..5).map(|i| {
    let data = Arc::clone(&data);
    thread::spawn(move || {
        let map = data.read().unwrap();
        println!("Reader {}: {:?}", i, *map);
    })
}).collect();

for r in readers { r.join().unwrap(); }
```

3. **Use `try_write` to avoid blocking**

```rust
use std::sync::RwLock;

let lock = RwLock::new(0);
match lock.try_write() {
    Ok(mut val) => { *val += 1; },
    Err(_) => eprintln!("Lock held by another thread"),
}
```

## Examples

```rust
use std::sync::{Arc, RwLock};
use std::thread;

fn main() {
    let cache = Arc::new(RwLock::new(std::collections::HashMap::new()));

    let mut handles = vec![];

    // Writer threads
    for i in 0..3 {
        let cache = Arc::clone(&cache);
        handles.push(thread::spawn(move || {
            let mut map = cache.write().unwrap();
            map.insert(format!("key-{}", i), i * 100);
            println!("Writer {} inserted", i);
        }));
    }

    // Reader threads
    for _ in 0..3 {
        let cache = Arc::clone(&cache);
        handles.push(thread::spawn(move || {
            let map = cache.read().unwrap();
            println!("Reader sees {} entries", map.len());
        }));
    }

    for h in handles { h.join().unwrap(); }
    let map = cache.read().unwrap();
    println!("Final cache: {:?}", *map);
}
```

## Related Errors

- [Mutex Error]({{< relref "/languages/rust/rust-mutex-error" >}}) — exclusive locks
- [Arc Error]({{< relref "/languages/rust/rust-arc-error" >}}) — shared ownership
- [Std Sync Error]({{< relref "/languages/rust/rust-std-sync-error" >}}) — sync primitives
