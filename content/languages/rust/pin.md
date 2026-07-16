---
title: "[Solution] Rust Cannot Move Pinned Value — Pin Error"
description: "Fix Rust cannot move pinned value error. Learn why pinned values cannot be moved and how to use Pin properly in async Rust."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
tags: ["pin", "pinned", "async", "self-referential", "unsafe", "future"]
weight: 5
---

# Cannot Move Pinned Value — Pin Error

A compiler error with the message "cannot move pinned value" occurs when you try to move a value that has been pinned with `Pin<&mut T>`. Pinned values guarantee their memory address won't change, which is essential for self-referential structs.

## Description

`Pin<P>` wraps a pointer and prevents the value it points to from being moved in memory. This is critical for:

- **Self-referential structs** — structs that contain references to their own fields.
- **Async futures** — generated state machines that are self-referential.
- **Generators** — stackless coroutines that hold across yield points.

Once a value is pinned, it cannot be moved without unsafe code. The compiler enforces this to prevent creating dangling references within the struct.

Common scenarios:

- **Moving a future** — `std::mem::move` on a pinned future.
- **Swapping pinned values** — `std::mem::swap` with pinned data.
- **Returning pinned values** — returning a Pin from a function.
- **Unpin trait** — most types implement Unpin, allowing them to be moved.

## Common Causes

```rust
use std::pin::Pin;
use std::future::Future;

// Cause 1: Moving a pinned future
async fn create_future() -> String {
    "data".to_string()
}

#[tokio::main]
async fn main() {
    let future = Box::pin(create_future());
    let moved = *future; // ERROR: cannot move pinned value
}

// Cause 2: Swapping pinned values
use std::pin::Pin;
use std::mem;

#[tokio::main]
async fn main() {
    let mut a = Box::pin(42i32);
    let mut b = Box::pin(100i32);

    // ERROR: cannot move pinned value
    // mem::swap(&mut a, &mut b);
}

// Cause 3: Unpin requirement
struct MyStruct {
    data: Vec<i32>,
}

// MyStruct doesn't implement Unpin by default
// if it contained Pin<Box<dyn Future>>
```

## Solutions

### Fix 1: Use Pin::into_inner for Unpin types

```rust
use std::pin::Pin;

fn main() {
    let pinned = Box::pin(42i32);

    // i32 implements Unpin, so we can extract the value
    let value = *pinned; // OK for Unpin types
    println!("{}", value);
}
```

### Fix 2: Use std::mem::swap with Pin::as_mut

```rust
use std::pin::Pin;
use std::mem;

#[tokio::main]
async fn main() {
    let mut a = Box::pin(42i32);
    let mut b = Box::pin(100i32);

    // For Unpin types, swap through as_mut
    let a_ref = a.as_mut();
    let b_ref = b.as_mut();

    // If both are Unpin, we can use get_mut
    let a_val = a.as_mut().get_mut();
    let b_val = b.as_mut().get_mut();
    mem::swap(a_val, b_val);

    println!("a={}, b={}", a, b); // a=100, b=42
}
```

### Fix 3: Use pin_project for safe pin projections

```toml
# Cargo.toml
[dependencies]
pin-project = "1"
```

```rust
use pin_project::pin_project;
use std::pin::Pin;

#[pin_project]
struct MyFuture {
    #[pin]
    inner: tokio::io::ReadHalf<tokio::net::TcpStream>,
    data: Vec<u8>,
}

impl MyFuture {
    fn new(stream: tokio::net::TcpStream) -> Self {
        let (read_half, _write_half) = tokio::io::split(stream);
        MyFuture {
            inner: read_half,
            data: Vec::new(),
        }
    }
}
```

### Fix 4: Use Box::pin to heap-allocate pinned values

```rust
use std::pin::Pin;
use std::future::Future;

async fn compute() -> i32 {
    42
}

#[tokio::main]
async fn main() {
    // Box::pin creates a pinned, heap-allocated future
    let future: Pin<Box<dyn Future<Output = i32>>> = Box::pin(compute());

    // The future is pinned on the heap and can be safely polled
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

    // This is fine — we poll the pinned future
    let result = future.await;
    println!("Result: {}", result);
}
```

Note: The error occurs when you try to move the pinned future itself, not when polling it.

## Related Errors

- [Async Await]({{< relref "/languages/rust/async-await" >}}) — async function not found.
- [Borrow Checker]({{< relref "/languages/rust/borrow-checker" >}}) — cannot borrow as mutable.
- [Move]({{< relref "/languages/rust/move" >}}) — using a value after it has been moved.
