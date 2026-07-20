---
title: "[Solution] Rust Std Sync Error — How to Fix"
description: "Fix standard library synchronization errors. Resolve Once, Condvar, and barrier usage issues."
languages: ["rust"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
comments: true
---

# Std Sync Error

Std sync errors occur when using `std::sync` primitives — mutex poisoning, deadlock, atomic ordering violations, and condvar issues.

## Common Causes

```rust
use std::sync::{Arc, Mutex, Condvar};
use std::thread;

// Mutex poisoning
let m = Arc::new(Mutex::new(0));
let m2 = Arc::clone(&m);
let h = thread::spawn(move || {
    let _guard = m2.lock().unwrap();
    panic!("panic while holding lock"); // Poisons mutex
});
let _ = h.join();
let _ = m.lock().unwrap(); // ERROR: poisoned

// Atomic ordering violation
use std::sync::atomic::{AtomicBool, Ordering};
static FLAG: AtomicBool = AtomicBool::new(false);
// Thread 1: FLAG.store(true, Ordering::Relaxed);
// Thread 2: while !FLAG.load(Ordering::Relaxed) {} // May never see update

// Condvar misuse — lost wakeup
```

## How to Fix

1. **Handle poisoned mutexes gracefully**

```rust
use std::sync::{Arc, Mutex};
use std::thread;

let data = Arc::new(Mutex::new(vec![1, 2, 3]));
let data2 = Arc::clone(&data);

let handle = thread::spawn(move || {
    let mut d = data2.lock().unwrap();
    d.push(4);
    panic!("oops");
});
let _ = handle.join();

// Recover from poisoned mutex
let data = data.lock().unwrap_or_else(|poisoned| poisoned.into_inner());
println!("{:?}", *data); // [1, 2, 3, 4]
```

2. **Use proper atomic ordering**

```rust
use std::sync::atomic::{AtomicBool, AtomicUsize, Ordering};
use std::sync::Arc;
use std::thread;

let ready = Arc::new(AtomicBool::new(false));
let data = Arc::new(AtomicUsize::new(0));

let ready_clone = Arc::clone(&ready);
let data_clone = Arc::clone(&data);

// Producer
thread::spawn(move || {
    data_clone.store(42, Ordering::Release); // Release ensures prior writes are visible
    ready_clone.store(true, Ordering::Release);
});

// Consumer
while !ready.load(Ordering::Acquire) { // Acquire synchronizes with Release
    std::thread::yield_now();
}
println!("Data: {}", data.load(Ordering::Acquire)); // Always sees 42
```

3. **Use Condvar properly to avoid lost wakeups**

```rust
use std::sync::{Arc, Mutex, Condvar};

let pair = Arc::new((Mutex::new(false), Condvar::new()));
let pair2 = Arc::clone(&pair);

// Waiter
thread::spawn(move || {
    let (lock, cvar) = &*pair2;
    let mut ready = lock.lock().unwrap();
    while !*ready {
        ready = cvar.wait(ready).unwrap();
    }
    println!("Got signal!");
});

// Signaler
std::thread::sleep(std::time::Duration::from_millis(100));
let (lock, cvar) = &*pair;
*lock.lock().unwrap() = true;
cvar.notify_one();
```

## Examples

```rust
use std::sync::{Arc, Mutex, Condvar};
use std::thread;
use std::time::Duration;

fn main() {
    let pair = Arc::new((Mutex::new(0u32), Condvar::new()));
    let pair2 = Arc::clone(&pair);

    // Worker thread
    let handle = thread::spawn(move || {
        let (lock, cvar) = &*pair2;
        let mut count = lock.lock().unwrap();
        *count += 1;
        println!("Worker incremented to {}", *count);
        cvar.notify_all();
    });

    // Main thread waits for condition
    let (lock, cvar) = &*pair;
    let mut count = lock.lock().unwrap();
    while *count == 0 {
        count = cvar.wait(count).unwrap();
    }
    println!("Main saw count: {}", *count);

    handle.join().unwrap();
}
```

## Related Errors

- [Mutex Error]({{< relref "/languages/rust/rust-mutex-error" >}}) — mutex issues
- [RwLock Error]({{< relref "/languages/rust/rust-rwlock-error" >}}) — read-write locks
- [Arc Error]({{< relref "/languages/rust/rust-arc-error" >}}) — shared ownership
