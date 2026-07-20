---
title: "[Solution] Rust Mutex Error — How to Fix"
description: "Fix Mutex synchronization errors. Resolve deadlock, poisoning, and lock acquisition issues."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Mutex Error

Mutex errors occur when using `std::sync::Mutex` or `tokio::sync::Mutex` incorrectly — poisoning, deadlock, holding locks across await points, or lock contention.

## Common Causes

```rust
use std::sync::{Arc, Mutex};
use std::thread;

// Mutex poisoning — panic while holding lock
let data = Arc::new(Mutex::new(vec![1, 2, 3]));
let data_clone = Arc::clone(&data);
let handle = thread::spawn(move || {
    let mut d = data_clone.lock().unwrap();
    d.push(4);
    panic!("Oops!"); // Poisoned mutex
});
let _ = handle.join();
let d = data.lock().unwrap(); // ERROR: mutex is poisoned

// Holding std::sync::Mutex across await points
async fn bad(data: &Arc<Mutex<Vec<i32>>>) {
    let guard = data.lock().unwrap();
    tokio::time::sleep(std::time::Duration::from_secs(1)).await; // BAD: holding lock
}

// Deadlock: acquiring locks in different order
let a = Mutex::new(1);
let b = Mutex::new(2);
// Thread 1: lock a, then b
// Thread 2: lock b, then a — DEADLOCK
```

## How to Fix

1. **Use `.lock().unwrap_or_else(|e| e.into_inner())` to recover from poisoned mutex**

```rust
use std::sync::Mutex;

let m = Mutex::new(vec![1, 2, 3]);
// If poisoned, recover the data
let data = m.lock().unwrap_or_else(|poisoned| poisoned.into_inner());
println!("{:?}", *data);
```

2. **Never hold std::sync::Mutex across await points — use tokio::sync::Mutex**

```rust
use tokio::sync::Mutex;
use std::sync::Arc;

async fn process(data: &Arc<Mutex<Vec<i32>>>) {
    let mut guard = data.lock().await;
    guard.push(4);
    tokio::time::sleep(std::time::Duration::from_secs(1)).await; // OK with tokio Mutex
    guard.push(5);
}
```

3. **Always acquire locks in a consistent order**

```rust
use std::sync::{Arc, Mutex};

struct Account {
    balance: Mutex<f64>,
}

// Always acquire locks in address order to prevent deadlock
fn transfer(a: &Account, b: &Account, amount: f64) {
    let a_addr = a as *const _ as usize;
    let b_addr = b as *const _ as usize;

    if a_addr < b_addr {
        let mut a_lock = a.balance.lock().unwrap();
        let mut b_lock = b.balance.lock().unwrap();
        *a_lock -= amount;
        *b_lock += amount;
    } else {
        let mut b_lock = b.balance.lock().unwrap();
        let mut a_lock = a.balance.lock().unwrap();
        *a_lock -= amount;
        *b_lock += amount;
    }
}
```

## Examples

```rust
use std::sync::{Arc, Mutex};
use std::thread;

fn main() {
    let counter = Arc::new(Mutex::new(0));
    let mut handles = vec![];

    for _ in 0..10 {
        let counter = Arc::clone(&counter);
        handles.push(thread::spawn(move || {
            let mut num = counter.lock().unwrap();
            *num += 1;
        }));
    }

    for h in handles { h.join().unwrap(); }
    println!("Final count: {}", *counter.lock().unwrap());
}
```

## Related Errors

- [RwLock Error]({{< relref "/languages/rust/rust-rwlock-error" >}}) — read-write locks
- [Arc Error]({{< relref "/languages/rust/rust-arc-error" >}}) — shared ownership
- [Std Sync Error]({{< relref "/languages/rust/rust-std-sync-error" >}}) — sync primitives
