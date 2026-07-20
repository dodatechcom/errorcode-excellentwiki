---
title: "[Solution] std::thread Spawn Error Fix"
description: "Fix std::thread spawn errors. Handle thread configuration, join handles, and panics."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# std::thread Spawn Error

The standard library's `std::thread::spawn` returns a `JoinHandle`, but the thread itself can panic or fail to start if the OS runs out of resources. When a spawned thread panics, calling `.join()` on its handle returns an `Err(JoinError)` containing the panic payload. Thread-unsafe access to shared state (e.g., `Rc` across threads, `!Send` types) causes compile-time or runtime errors.

## Common Causes

```rust
use std::thread;

// 1. Panicking inside a spawned thread — join returns Err
let handle = thread::spawn(|| {
    panic!("something went wrong");
});
let result = handle.join(); // Err(Any)

// 2. Sending a non-Send type across thread boundaries
use std::rc::Rc;
thread::spawn(|| {
    let data = Rc::new(42);
    println!("{}", data); // ERROR: Rc<i32> cannot be sent between threads safely
});

// 3. Detached thread — no one calls join(), panic is silently swallowed
thread::spawn(|| {
    panic!("forgotten thread");
});
// No handle retained — panic goes nowhere

// 4. Thread panics propagate through shared state
use std::sync::{Arc, Mutex};
let data = Arc::new(Mutex::new(0u32));
let data2 = Arc::clone(&data);
thread::spawn(move || {
    let _lock = data2.lock().unwrap(); // panics → mutex poisoned
});
```

## How to Fix

1. **Always join spawned threads and handle JoinError**

```rust
use std::thread;

let handle = thread::spawn(|| {
    "result from thread"
});

match handle.join() {
    Ok(val) => println!("Thread returned: {}", val),
    Err(e) => {
        // Downcast to get the panic message
        if let Some(msg) = e.downcast_ref::<&str>() {
            eprintln!("Thread panicked: {}", msg);
        } else if let Some(msg) = e.downcast_ref::<String>() {
            eprintln!("Thread panicked: {}", msg);
        }
    }
}
```

2. **Use Send + 'static bound constraints explicitly**

```rust
use std::thread;
use std::sync::Arc;

// Only types implementing Send + 'static can be moved into threads
let data = Arc::new(vec![1, 2, 3]);
let data_clone = Arc::clone(&data);

let handle = thread::spawn(move || {
    println!("Thread sees: {:?}", data_clone);
});

handle.join().unwrap();
```

3. **Use scoped threads for borrowing local data**

```rust
use std::thread;

let mut data = vec![1, 2, 3, 4, 5];

thread::scope(|s| {
    s.spawn(|| {
        println!("Thread 1: {:?}", &data);
    });
    s.spawn(|| {
        println!("Thread 2: {:?}", &data);
    });
});
// data still valid here — no Arc needed
```

4. **Use `catch_unwind` to handle panics without crashing**

```rust
use std::panic::{catch_unwind, AssertUnwindSafe};
use std::thread;

let handle = thread::spawn(AssertUnwindSafe(|| {
    if true { panic!("oops"); }
    42
}));

let result = catch_unwind(|| handle.join());
match result {
    Ok(Ok(val)) => println!("Got: {}", val),
    Ok(Err(_)) => eprintln!("Thread panicked"),
    Err(_) => eprintln!("Join itself panicked"),
}
```

## Examples

```rust
use std::thread;
use std::sync::{Arc, atomic::{AtomicU32, Ordering}};

fn main() {
    let counter = Arc::new(AtomicU32::new(0));
    let mut handles = vec![];

    for _ in 0..10 {
        let counter = Arc::clone(&counter);
        let handle = thread::spawn(move || {
            counter.fetch_add(1, Ordering::SeqCst);
        });
        handles.push(handle);
    }

    for h in handles {
        h.join().expect("Thread panicked");
    }

    println!("Final count: {}", counter.load(Ordering::SeqCst));
}
```

## Related Errors

- [Tokio Error]({{< relref "/languages/rust/tokio-error" >}}) — async task panics
- [Scoped Threadpool Error]({{< relref "/languages/rust/scoped-threadpool-error" >}}) — scoped threads
- [Crossbeam Error]({{< relref "/languages/rust/crossbeam-error" >}}) — crossbeam threads
