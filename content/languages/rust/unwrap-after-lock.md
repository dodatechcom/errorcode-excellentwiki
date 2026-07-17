---
title: "[Solution] Rust Mutex Poisoned — Mutex Lock Poison Error"
description: "Fix Rust Mutex poisoned error. Learn why mutexes become poisoned when a thread panics while holding the lock and how to recover from it."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Mutex Poisoned — Mutex Lock Poison Error

A panic with the message "Mutex is poisoned" occurs when you try to lock a `Mutex` that has been poisoned. A mutex becomes poisoned when a thread panics while holding the lock.

## Description

Rust's `Mutex<T>` provides mutual exclusion for shared data. When a thread panics while holding a mutex lock, the mutex is marked as "poisoned" to prevent potentially inconsistent data from being used by other threads. The idea is that if a thread panicked, the protected data might be in an inconsistent state.

By default, calling `.lock()` on a poisoned mutex returns a `Err(PoisonError)`. You can choose to:
- **Panic** — the default behavior.
- **Recover** — access the potentially inconsistent data.
- **Use `forget_poison`** — reset the poison flag.

Common scenarios:

- **Thread panic while holding lock** — a thread crashes during critical section.
- **Propagation from child thread** — parent thread receives poisoned lock.
- **Nested mutexes** — inner mutex poisons outer mutex.

## Common Causes

```rust
use std::sync::{Arc, Mutex};
use std::thread;

// Cause 1: Thread panics while holding lock
let data = Arc::new(Mutex::new(vec![1, 2, 3]));
let data_clone = Arc::clone(&data);

let handle = thread::spawn(move || {
    let mut lock = data_clone.lock().unwrap();
    lock.push(4);
    panic!("oops!"); // Lock is poisoned after panic
});

handle.join().unwrap_err();

// Cause 2: Trying to use the poisoned lock
let mut lock = data.lock().unwrap(); // panics because mutex is poisoned

// Cause 3: Nested mutex poisoning
let outer = Arc::new(Mutex::new(0));
let inner = Arc::new(Mutex::new(0));
```

## Solutions

### Fix 1: Handle poisoned mutex gracefully

```rust
use std::sync::{Arc, Mutex};

let data = Arc::new(Mutex::new(vec![1, 2, 3]));

// Wrong — panics on poisoned mutex
let lock = data.lock().unwrap();

// Correct — handle the poison error
match data.lock() {
    Ok(lock) => {
        println!("Data: {:?}", *lock);
    }
    Err(poisoned) => {
        // Access the data anyway
        let lock = poisoned.into_inner();
        println!("Mutex was poisoned, but data is: {:?}", *lock);
    }
}
```

### Fix 2: Use into_inner to recover data

```rust
use std::sync::{Arc, Mutex};

let data = Arc::new(Mutex::new(vec![1, 2, 3]));

// Recover data from poisoned mutex
let lock = match data.lock() {
    Ok(lock) => lock,
    Err(poisoned) => poisoned.into_inner(),
};

println!("Data: {:?}", *lock);
```

### Fix 3: Use catch_unwind to prevent poisoning

```rust
use std::panic;
use std::sync::{Arc, Mutex};

let data = Arc::new(Mutex::new(vec![1, 2, 3]));
let data_clone = Arc::clone(&data);

let handle = thread::spawn(move || {
    let result = panic::catch_unwind(panic::AssertUnwindSafe(|| {
        let mut lock = data_clone.lock().unwrap();
        lock.push(4);
        // If something panics here, the lock won't be poisoned
    }));

    if result.is_err() {
        println!("Thread panicked, but mutex is not poisoned");
    }
});

handle.join().unwrap();
let lock = data.lock().unwrap(); // Works because we caught the panic
println!("Data: {:?}", *lock);
```

### Fix 4: Use parking_lot mutex (no poisoning)

```toml
# Cargo.toml
[dependencies]
parking_lot = "0.12"
```

```rust
use parking_lot::Mutex;
use std::sync::Arc;
use std::thread;

let data = Arc::new(Mutex::new(vec![1, 2, 3]));
let data_clone = Arc::clone(&data);

let handle = thread::spawn(move || {
    let mut lock = data_clone.lock();
    lock.push(4);
    panic!("oops!"); // parking_lot mutex is NOT poisoned
});

handle.join().unwrap_err();
let lock = data.lock(); // Works with parking_lot
println!("Data: {:?}", *lock);
```

## Examples

```rust
use std::sync::{Arc, Mutex};
use std::thread;

fn main() {
    let data = Arc::new(Mutex::new(0));
    let data_clone = Arc::clone(&data);

    let handle = thread::spawn(move || {
        let mut lock = data_clone.lock().unwrap();
        *lock += 1;
        panic!("thread panicked!");
    });

    let _ = handle.join();

    // This panics because the mutex is poisoned
    let lock = data.lock().unwrap();
    println!("Value: {}", *lock);
}
```

Output:
```
thread 'main' panicked at 'called `Result::unwrap()` on an `Err` value: PoisonError { .. }'
```

## Related Errors

- [Thread Panic]({{< relref "/languages/rust/thread-panic" >}}) — thread panics at a given message.
- [Unwrap Err]({{< relref "/languages/rust/unwrap-err" >}}) — calling unwrap on an Err Result.
