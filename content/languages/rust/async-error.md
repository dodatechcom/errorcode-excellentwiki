---
title: "[Solution] Rust Future Is Not Send / Not a Future — Async Error Fix"
description: "Fix Rust async errors: future is not Send, not a future, or does not implement Send. Understand Send bounds and async task safety."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["async", "await", "future", "send", "tokio", "spawn", "pin"]
weight: 5
---

# Future Is Not Send / Not a Future

The error `future is not Send` or `the trait Send is not implemented` occurs when you try to spawn an async task on a multithreaded runtime, but the future captures a type that is not `Send`-safe. The error `not a future` occurs when you use `.await` on a value that does not implement the `Future` trait.

## Description

Tokio and other multithreaded async runtimes require futures to be `Send` so they can be moved between threads. Types like `Rc<T>`, `*const T`, and raw pointers are not `Send` because they are not safe to access from multiple threads. If a future captures any non-`Send` type, it cannot be spawned on a multithreaded runtime.

Common scenarios include using `Rc` inside async functions, holding `MutexGuard` across await points, and calling non-async functions that return non-`Send` types.

## Common Causes

- **Using Rc inside async fn** — `Rc<T>` is not `Send`; use `Arc<T>` instead
- **Holding MutexGuard across await** — `std::sync::MutexGuard` is not `Send`; use `tokio::sync::Mutex`
- **Non-Send type in spawned future** — capturing a non-`Send` value in a closure passed to `tokio::spawn`
- **Calling non-future with .await** — calling `.await` on a non-async value

## How to Fix

### Fix 1: Use Arc instead of Rc

```rust
// Wrong — Rc is not Send
use std::rc::Rc;
let data = Rc::new(vec![1, 2, 3]);
tokio::spawn(async move {
    println!("{:?}", data); // Error: future is not Send
});

// Correct — Arc is Send
use std::sync::Arc;
let data = Arc::new(vec![1, 2, 3]);
tokio::spawn(async move {
    println!("{:?}", data);
});
```

### Fix 2: Use tokio::sync::Mutex

```rust
// Wrong — std::sync::MutexGuard is not Send
let mutex = std::sync::Mutex::new(vec![1, 2, 3]);
tokio::spawn(async move {
    let guard = mutex.lock().unwrap(); // Not Send across await
    do_something().await;
});

// Correct — tokio::sync::Mutex
let mutex = tokio::sync::Mutex::new(vec![1, 2, 3]);
tokio::spawn(async move {
    let guard = mutex.lock().await;
    do_something().await;
});
```

### Fix 3: Use spawn_local for non-Send futures

```rust
let rt = tokio::runtime::LocalRuntime::new().unwrap();
let local = tokio::task::LocalSet::new();
local.spawn_local(async {
    // non-Send types are OK here
});
```

### Fix 4: Use spawn_blocking for non-async work

```rust
tokio::task::spawn_blocking(move || {
    // blocking, non-Send-safe work
    heavy_computation()
}).await?;
```

## Examples

```rust
use std::rc::Rc;

async fn process() {
    let data = Rc::new(vec![1, 2, 3]);
    println!("{:?}", data);
}

#[tokio::main]
async fn main() {
    tokio::spawn(process()); // Error: future is not Send
}
```

Output:
```
error future cannot be sent between threads safely
```

## Related Errors

- [tokio]({{< relref "/languages/rust/tokio" >}}) — Tokio runtime and task errors.
- [async-await]({{< relref "/languages/rust/async-await" >}}) — async/await syntax issues.
- [pin]({{< relref "/languages/rust/pin" >}}) — pinning futures and self-referential types.
