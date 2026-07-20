---
title: "[Solution] Rust Pin Error — How to Fix"
description: "Fix Pin reference errors. Resolve pinned projection, Unpin trait bounds, and self-referential struct issues."
languages: ["rust"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
comments: true
---

# Pin Error

Pin errors occur when working with `std::pin::Pin` — unpinned values, self-referential struct issues, or calling methods that require Unpin on pinned data.

## Common Causes

```rust
use std::pin::Pin;
use std::future::Future;

// Trying to move a pinned value
fn bad_move(pinned: Pin<&mut i32>) {
    let moved = *pinned; // ERROR: cannot move out of pinned reference
}

// Self-referential struct — cannot be safely constructed
struct MyFuture {
    data: String,
    // ptr: *const String, // Would point into data — self-referential
}

// Missing Unpin — some futures need explicit unpinning
async fn needs_unpin(future: impl Future<Output = i32> + Unpin) {}
```

## How to Fix

1. **Use `Box::pin` to create heap-pinned values**

```rust
use std::pin::Pin;
use std::future::Future;

fn make_pinned() -> Pin<Box<dyn Future<Output = i32>>> {
    Box::pin(async { 42 })
}

#[tokio::main]
async fn main() {
    let result = make_pinned().await;
    println!("Result: {}", result);
}
```

2. **Implement `Unpin` when your type is safe to move**

```rust
use std::pin::Pin;
use std::task::{Context, Poll};

struct MyFuture { value: i32 }

impl std::future::Future for MyFuture {
    type Output = i32;
    fn poll(self: Pin<&mut Self>, _cx: &mut Context) -> Poll<i32> {
        Poll::Ready(self.value) // self is safe to access because MyFuture is Unpin
    }
}

// MyFuture automatically implements Unpin because all fields are Unpin
```

3. **Use `pin!` macro or `pin_project` for safe pin projections**

```rust
use std::pin::pin;
use std::future::Future;

async fn example() {
    let future = pin!(async { 42 });
    let result = future.await;
    println!("{}", result);
}
```

## Examples

```rust
use std::pin::Pin;
use std::task::{Context, Poll};

struct CountDown {
    count: u32,
}

impl CountDown {
    fn new(count: u32) -> Pin<Box<Self>> {
        Box::pin(CountDown { count })
    }
}

impl std::future::Future for CountDown {
    type Output = String;

    fn poll(mut self: Pin<&mut Self>, cx: &mut Context<'_>) -> Poll<String> {
        if self.count == 0 {
            Poll::Ready("Done!".to_string())
        } else {
            println!("Count: {}", self.count);
            self.count -= 1;
            cx.waker().wake_by_ref();
            Poll::Pending
        }
    }
}

#[tokio::main]
async fn main() {
    let result = CountDown::new(3).await;
    println!("{}", result);
}
```

## Related Errors

- [Future Error]({{< relref "/languages/rust/rust-future-error" >}}) — future issues
- [Poll Error]({{< relref "/languages/rust/rust-poll-error" >}}) — polling issues
- [Waker Error]({{< relref "/languages/rust/rust-waker-error" >}}) — waker issues
