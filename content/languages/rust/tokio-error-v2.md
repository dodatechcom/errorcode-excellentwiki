---
title: "[Solution] tokio Runtime Builder Error Fix"
description: "Fix tokio runtime builder errors. Handle multi-threaded runtime creation and configuration issues."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["tokio", "async", "runtime", "thread"]
weight: 5
---

# tokio Runtime Builder Error

Fix tokio runtime builder errors. Handle multi-threaded runtime creation and configuration issues.

## What This Error Means

Tokio runtime builder errors occur when you try to create a runtime with invalid configuration or when the runtime cannot be started. Common messages include:

```
thread 'main' panicked at 'Cannot start a runtime from within a runtime'
io error: unable to start the runtime: no available cores
```

## Common Causes

```rust
// Cause 1: Creating a runtime inside an existing runtime
let rt = tokio::runtime::Runtime::new().unwrap();
rt.block_on(async {
    let inner_rt = tokio::runtime::Runtime::new(); // PANIC!
});

// Cause 2: Worker threads set to 0
let rt = tokio::runtime::Builder::new_multi_thread()
    .worker_threads(0)
    .enable_all()
    .build(); // Error

// Cause 3: Calling block_on from an async context
#[tokio::main]
async fn main() {
    let val = futures::executor::block_on(some_future); // PANIC
}
```

## How to Fix

### Fix 1: Use a single runtime or Handle::current

```rust
use tokio::runtime::Handle;

#[tokio::main]
async fn main() {
    // Spawn a blocking task instead of creating a new runtime
    let result = tokio::task::spawn_blocking(|| {
        // Blocking code here
        42
    }).await.unwrap();
}
```

### Fix 2: Set a valid number of worker threads

```rust
use tokio::runtime::Builder;

fn main() {
    let rt = Builder::new_multi_thread()
        .worker_threads(num_cpus::get().max(1))
        .enable_all()
        .build()
        .expect("Failed to create runtime");

    rt.block_on(async_main());
}
```

### Fix 3: Use async operations in async contexts

```rust
#[tokio::main]
async fn main() {
    // Instead of block_on, use .await
    let val = some_async_operation().await;

    // Or spawn a blocking task for CPU-bound work
    let val = tokio::task::spawn_blocking(|| {
        expensive_computation()
    }).await.unwrap();
}
```

## Examples

```rust
use tokio::runtime::Builder;

fn main() {
    let rt = Builder::new_multi_thread()
        .worker_threads(4)
        .enable_io()
        .enable_time()
        .thread_name("my-worker")
        .on_thread_start(|| {
            println!("Worker thread started");
        })
        .build()
        .expect("Failed to create runtime");

    rt.block_on(async {
        let handle = tokio::spawn(async {
            "hello from task"
        });
        let result = handle.await.unwrap();
        println!("{}", result);
    });
}
```

## Related Errors

- [Async Await]({{< relref "/languages/rust/async-await" >}}) — async/await error
- [Thread Panic]({{< relref "/languages/rust/thread-panic" >}}) — thread panic
- [Std Thread Error]({{< relref "/languages/rust/std-thread-error" >}}) — thread error
