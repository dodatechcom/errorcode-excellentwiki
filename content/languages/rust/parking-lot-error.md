---
title: "[Solution] parking_lot Lock Error Fix"
description: "Fix parking_lot lock errors. Handle mutex poisoning, deadlock detection, and read-write locks."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Parking Lot Error

Parking lot errors occur when using the `parking_lot` crate — deadlocks, poisoned locks, and timing issues.

## Common Causes

```rust
// Deadlock: two locks acquired in opposite order
let a = Mutex::new(1);
let b = Mutex::new(2);
let _a = a.lock();
let _b = b.lock(); // May deadlock if another thread holds b then a

// Poisoned lock
let lock = Arc::new(Mutex::new(vec![]));
let data = lock.lock().unwrap(); // Panics if lock was poisoned
```

## How to Fix

1. **Always acquire locks in consistent order**

```rust
use parking_lot::Mutex;
use std::sync::Arc;

let a = Arc::new(Mutex::new(vec![1]));
let b = Arc::new(Mutex::new(vec![2]));
// Always lock a before b, in every thread
let _a = a.lock();
let _b = b.lock();
```

2. **Use try_lock for non-blocking access**

```rust
use parking_lot::Mutex;

let m = Mutex::new(42);
match m.try_lock() {
    Some(guard) => println!("Got lock: {}", *guard),
    None => println!("Lock is held, trying later"),
}
```

3. **Use RwLock for read-heavy workloads**

```rust
use parking_lot::RwLock;

let data = RwLock::new(vec![1, 2, 3]);
// Multiple readers allowed
let r1 = data.read();
let r2 = data.read();
// Exclusive write
drop(r1);
drop(r2);
let mut w = data.write();
w.push(4);
```

## Examples

```rust
use parking_lot::{Mutex, RwLock};
use std::sync::Arc;
use std::thread;

fn main() {
    let counter = Arc::new(Mutex::new(0));
    let mut handles = vec![];

    for _ in 0..10 {
        let c = counter.clone();
        handles.push(thread::spawn(move || {
            let mut num = c.lock();
            *num += 1;
        }));
    }

    for h in handles { h.join().unwrap(); }
    println!("Counter: {}", *counter.lock());
}
```

## Related Errors

- [RwLock Error]({{< relref "/languages/rust/rust-rwlock-error" >}}) — std RwLock
- [Mutex Error]({{< relref "/languages/rust/rust-mutex-error" >}}) — std Mutex
- [Deadlock Error]({{< relref "/languages/rust/deadlock" >}}) — deadlocks
