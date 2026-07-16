---
title: "[Solution] Rust Mutex Poisoned — Lock Poison Error"
description: "Fix Rust Mutex poisoned error. Learn why mutexes become poisoned when a thread panics and how to recover from or prevent poisoning."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
tags: ["mutex", "poisoned", "thread", "lock", "sync", "arc"]
weight: 5
---

# Mutex Poisoned — Lock Poison Error

A panic with the message "Mutex is poisoned" (or an `Err(PoisonError)` from `.lock().unwrap()`) occurs when you try to lock a `Mutex` that has been poisoned by a thread that panicked while holding the lock.

## Description

Rust's `Mutex<T>` marks itself as "poisoned" when a thread panics while holding the lock. This is a safety mechanism — the data inside might be in an inconsistent state. By default, `.lock().unwrap()` on a poisoned mutex panics again.

You can recover from a poisoned mutex using `poison.into_inner()`, which gives you access to the data even if it might be corrupted. Whether to use this depends on whether your data can tolerate partial updates.

Common scenarios:

- **Thread panic during critical section** — thread crashes while holding lock.
- **Nested panics** — inner lock causes a panic that poisons outer lock.
- **Propagation** — parent thread tries to use a lock poisoned by a child.

## Common Causes

```rust
use std::sync::{Arc, Mutex};
use std::thread;

// Cause 1: Thread panics while holding lock
let data = Arc::new(Mutex::new(vec![1, 2, 3]));
let data2 = Arc::clone(&data);
let h = thread::spawn(move || {
    let mut lock = data2.lock().unwrap();
    lock.push(4);
    panic!("crash!"); // mutex poisoned after this
});
h.join().unwrap_err();
data.lock().unwrap(); // panics: mutex is poisoned

// Cause 2: Poisoning propagation
let data = Arc::new(Mutex::new(0));
let d2 = Arc::clone(&data);
let h = thread::spawn(move || {
    *d2.lock().unwrap() = 1;
    panic!();
});
h.join().unwrap_err();
// data is now poisoned
```

## Solutions

### Fix 1: Handle the poison error

```rust
use std::sync::{Arc, Mutex};

let data = Arc::new(Mutex::new(vec![1, 2, 3]));

match data.lock() {
    Ok(lock) => println!("Data: {:?}", *lock),
    Err(poisoned) => {
        let lock = poisoned.into_inner();
        println!("Mutex was poisoned, data: {:?}", *lock);
    }
}
```

### Fix 2: Recover with into_inner

```rust
use std::sync::{Arc, Mutex};

let data = Arc::new(Mutex::new(vec![1, 2, 3]));

// After a thread panics and poisons the mutex:
let lock = match data.lock() {
    Ok(l) => l,
    Err(poisoned) => poisoned.into_inner(),
};
println!("Recovered data: {:?}", *lock);
```

### Fix 3: Prevent poisoning with catch_unwind

```rust
use std::panic;
use std::sync::{Arc, Mutex};

let data = Arc::new(Mutex::new(Vec::new()));
let d2 = Arc::clone(&data);

let h = std::thread::spawn(move || {
    let _ = panic::catch_unwind(panic::AssertUnwindSafe(|| {
        let mut lock = d2.lock().unwrap();
        lock.push(42);
    }));
});
h.join().unwrap();

let lock = data.lock().unwrap(); // not poisoned
println!("{:?}", *lock);
```

### Fix 4: Use parking_lot (no poisoning by design)

```rust
// Cargo.toml: parking_lot = "0.12"
use parking_lot::Mutex;

let data = Mutex::new(vec![1, 2, 3]);
{
    let mut lock = data.lock();
    lock.push(4);
}
println!("{:?}", *data.lock());
```

## Examples

```rust
use std::sync::{Arc, Mutex};
use std::thread;

fn main() {
    let data = Arc::new(Mutex::new(0));
    let d2 = Arc::clone(&data);

    let h = thread::spawn(move || {
        let mut lock = d2.lock().unwrap();
        *lock += 1;
        panic!("oops");
    });

    let _ = h.join();
    let lock = data.lock().unwrap();
    println!("Value: {}", *lock);
}
```

Output:
```
thread 'main' panicked at 'called `Result::unwrap()` on an `Err` value: PoisonError { .. }'
```

## Related Errors

- [Thread Panic]({{< relref "/languages/rust/thread-panic-2" >}}) — thread panics at a message.
- [Unwrap Err]({{< relref "/languages/rust/unwrap-err-2" >}}) — unwrap on an Err Result.
- [Unwrap None]({{< relref "/languages/rust/unwrap-none-2" >}}) — unwrap on a None Option.
