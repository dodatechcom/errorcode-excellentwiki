---
title: "[Solution] Rust Waker Error — How to Fix"
description: "Fix Waker and RawWaker errors. Resolve waker creation, waking correctness, and context issues."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Waker Error

Waker errors occur when implementing or using `Waker` — failing to wake, double-waking, or using wakers incorrectly in custom futures.

## Common Causes

```rust
use std::task::{Context, Poll, Waker};

// Not calling wake when returning Pending
struct MyFuture;
impl std::future::Future for MyFuture {
    type Output = ();
    fn poll(self: Pin<&mut Self>, _cx: &mut Context) -> Poll<()> {
        Poll::Pending // Never wakes — future hangs forever
    }
}

// Using wrong waker — waking a different task's waker
// Storing waker without cloning it

// Multiple wakers for same task
```

## How to Fix

1. **Always wake the waker before returning Pending**

```rust
use std::future::Future;
use std::pin::Pin;
use std::task::{Context, Poll};
use std::time::{Duration, Instant};

struct WaitUntil { deadline: Instant }

impl Future for WaitUntil {
    type Output = ();

    fn poll(self: Pin<&mut Self>, cx: &mut Context) -> Poll<()> {
        if Instant::now() >= self.deadline {
            Poll::Ready(())
        } else {
            cx.waker().wake_by_ref(); // Schedule re-poll
            Poll::Pending
        }
    }
}
```

2. **Clone wakers for storage**

```rust
use std::task::{Context, Poll, Waker};
use std::future::Future;
use std::pin::Pin;

struct SharedFuture {
    waker: Option<Waker>,
    value: Option<i32>,
}

impl Future for SharedFuture {
    type Output = i32;

    fn poll(mut self: Pin<&mut Self>, cx: &mut Context) -> Poll<i32> {
        if let Some(val) = self.value.take() {
            return Poll::Ready(val);
        }
        self.waker = Some(cx.waker().clone());
        Poll::Pending
    }
}
```

3. **Use `wake_by_ref` instead of consuming the waker**

```rust
use std::task::{Context, Poll};
use std::future::Future;
use std::pin::Pin;

struct Timer { ticks: u32 }

impl Future for Timer {
    type Output = u32;

    fn poll(mut self: Pin<&mut Self>, cx: &mut Context) -> Poll<u32> {
        if self.ticks == 0 {
            Poll::Ready(0)
        } else {
            self.ticks -= 1;
            cx.waker().wake_by_ref(); // Don't consume the waker
            Poll::Pending
        }
    }
}

#[tokio::main]
async fn main() {
    let result = Timer { ticks: 3 }.await;
    println!("Done: {}", result);
}
```

## Examples

```rust
use std::future::Future;
use std::pin::Pin;
use std::task::{Context, Poll};
use std::time::{Duration, Instant};

struct Countdown {
    remaining: u32,
    last_tick: Instant,
}

impl Future for Countdown {
    type Output = String;

    fn poll(mut self: Pin<&mut Self>, cx: &mut Context) -> Poll<String> {
        if self.remaining == 0 {
            return Poll::Ready("Countdown complete!".into());
        }

        if self.last_tick.elapsed() >= Duration::from_millis(100) {
            println!("Tick: {}", self.remaining);
            self.remaining -= 1;
            self.last_tick = Instant::now();
        }

        cx.waker().wake_by_ref();
        Poll::Pending
    }
}

#[tokio::main]
async fn main() {
    let result = Countdown { remaining: 3, last_tick: Instant::now() }.await;
    println!("{}", result);
}
```

## Related Errors

- [Poll Error]({{< relref "/languages/rust/rust-poll-error" >}}) — polling issues
- [Future Error]({{< relref "/languages/rust/rust-future-error" >}}) — future issues
- [Pin Error]({{< relref "/languages/rust/rust-pin-error" >}}) — pinning issues
