---
title: "[Solution] Rust Cannot Move Pinned Value — Pin Error"
description: "Fix Rust cannot move pinned value error. Learn why pinned values cannot be moved and how to use Pin, Unpin, and pin_project properly."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
tags: ["pin", "pinned", "async", "self-referential", "future", "unpin"]
weight: 5
---

# Cannot Move Pinned Value — Pin Error

A compiler error with the message "cannot move pinned value" occurs when you try to move a value that has been pinned with `Pin<&mut T>`.

## Description

`Pin<P>` wraps a pointer and prevents the value it points to from being moved in memory. This is critical for self-referential structs and async futures, which hold references to their own fields. Moving such a value would invalidate those internal references.

Once pinned, a value cannot be moved without unsafe code. The compiler enforces this.

Common scenarios:

- **Moving a future** — `std::mem::move` on a pinned future.
- **Swapping pinned values** — `std::mem::swap` with pinned data.
- **Returning pinned values** — returning a Pin from a function.
- **Unpin trait** — most types implement Unpin, allowing movement.

## Common Causes

```rust
use std::pin::Pin;
use std::future::Future;

// Cause 1: Moving a pinned future
async fn create_future() -> String { "data".to_string() }

#[tokio::main]
async fn main() {
    let future = Box::pin(create_future());
    let moved = *future; // ERROR: cannot move pinned value
}

// Cause 2: Swapping pinned values
use std::mem;

#[tokio::main]
async fn main() {
    let mut a = Box::pin(42i32);
    let mut b = Box::pin(100i32);
    // mem::swap(&mut a, &mut b); // ERROR for non-Unpin types
}

// Cause 3: Non-Unpin struct
struct MyStruct { data: Vec<i32> }
// MyStruct doesn't implement Unpin by default if it contains Pin
```

## Solutions

### Fix 1: Use get_mut for Unpin types

```rust
use std::pin::Pin;

fn main() {
    let pinned = Box::pin(42i32);
    let value = *pinned; // OK: i32 is Unpin
    println!("{}", value);
}
```

### Fix 2: Swap through as_mut/get_mut

```rust
use std::pin::Pin;
use std::mem;

#[tokio::main]
async fn main() {
    let mut a = Box::pin(42i32);
    let mut b = Box::pin(100i32);
    mem::swap(a.as_mut().get_mut(), b.as_mut().get_mut());
    println!("a={}, b={}", a, b); // a=100, b=42
}
```

### Fix 3: Use pin_project for safe projections

```rust
// Cargo.toml: pin-project = "1"
use pin_project::pin_project;
use std::pin::Pin;

#[pin_project]
struct MyFuture {
    #[pin]
    inner: tokio::io::ReadHalf<tokio::net::TcpStream>,
    data: Vec<u8>,
}
```

### Fix 4: Use Box::pin for heap-allocated pinned futures

```rust
use std::pin::Pin;
use std::future::Future;

async fn compute() -> i32 { 42 }

#[tokio::main]
async fn main() {
    let future: Pin<Box<dyn Future<Output = i32>>> = Box::pin(compute());
    let result = future.await;
    println!("Result: {}", result);
}
```

## Examples

```rust
use std::pin::Pin;

#[tokio::main]
async fn main() {
    let future = Box::pin(async {
        println!("inside pinned future");
        42
    });
    let result = future.await;
    println!("Result: {}", result);
}
```

Note: The error occurs when you try to move the pinned future itself, not when polling it.

## Related Errors

- [Async Await]({{< relref "/languages/rust/async-await-2" >}}) — async function not found.
- [Borrow Checker]({{< relref "/languages/rust/borrow-checker-2" >}}) — cannot borrow as mutable.
- [Move]({{< relref "/languages/rust/move-2" >}}) — using a value after it was moved.
