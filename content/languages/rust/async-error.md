---
title: "[Solution] Rust Future Is Not Send / Not a Future — Async Error Fix"
description: "Fix Rust async errors: future is not Send, not a future, or does not implement Send. Understand Send bounds and async task safety."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Async Error

Async errors occur when using async/await in Rust — issues with `Send` bounds, lifetime violations across await points, and runtime-specific problems.

## Common Causes

```rust
// Not Send — cannot spawn on multi-threaded runtime
use std::rc::Rc;
async fn bad() {
    let data = Rc::new(42);
    tokio::time::sleep(std::time::Duration::from_millis(10)).await;
    println!("{}", data); // Rc !Send
}

// Borrowing across await points
async fn borrow_across(data: &Vec<i32>) -> &i32 {
    let r = &data[0];
    tokio::time::sleep(std::time::Duration::from_millis(10)).await;
    r // data may be dropped while r is borrowed
}
```

## How to Fix

1. **Use `Arc` instead of `Rc` in async code**

```rust
use std::sync::Arc;

async fn process() {
    let data = Arc::new(vec![1, 2, 3]);
    let data_clone = Arc::clone(&data);
    tokio::spawn(async move {
        println!("{:?}", data_clone);
    }).await.unwrap();
}
```

2. **Clone data before await**

```rust
async fn safe_borrow(data: Vec<i32>) -> i32 {
    let first = data[0]; // Copy the value before await
    tokio::time::sleep(std::time::Duration::from_millis(10)).await;
    first
}
```

3. **Use `tokio::spawn` with proper Send bounds**

```rust
#[tokio::main]
async fn main() {
    let handle = tokio::spawn(async {
        tokio::time::sleep(std::time::Duration::from_millis(100)).await;
        42
    });
    println!("Result: {}", handle.await.unwrap());
}
```

## Examples

```rust
use std::sync::Arc;
use tokio::sync::Mutex;

#[tokio::main]
async fn main() {
    let shared = Arc::new(Mutex::new(vec![1, 2, 3]));

    let mut handles = vec![];
    for i in 0..5 {
        let shared = Arc::clone(&shared);
        handles.push(tokio::spawn(async move {
            shared.lock().await.push(i);
        }));
    }
    for h in handles { h.await.unwrap(); }
    println!("{:?}", *shared.lock().await);
}
```

## Related Errors

- [Tokio Runtime Error]({{< relref "/languages/rust/rust-tokio-runtime-error" >}}) — runtime issues
- [Future Error]({{< relref "/languages/rust/rust-future-error" >}}) — future issues
- [Arc Error]({{< relref "/languages/rust/rust-arc-error" >}}) — shared ownership
