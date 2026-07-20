---
title: "[Solution] Rust Poll Error — How to Fix"
description: "Fix Poll enum usage errors. Resolve Ready/Pending state handling, self-wakeup, and future progression."
languages: ["rust"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
comments: true
---

# Poll Error

Poll errors occur when implementing `Future` or `Stream` traits — incorrect polling behavior, missing wake notifications, or returning Pending without scheduling a wake.

## Common Causes

```rust
use std::task::{Context, Poll};
use std::future::Future;

// Returning Pending without calling wake — future never progresses
struct NeverComplete;
impl Future for NeverComplete {
    type Output = ();
    fn poll(self: Pin<&mut Self>, _cx: &mut Context) -> Poll<()> {
        Poll::Pending // Never calls cx.waker().wake() — hangs forever
    }
}

// Polling after returning Ready — undefined behavior
struct BadFuture { done: bool }
impl Future for BadFuture {
    type Output = i32;
    fn poll(mut self: Pin<&mut Self>, cx: &mut Context) -> Poll<i32> {
        if self.done { return Poll::Ready(42); }
        self.done = true;
        cx.waker().wake_by_ref();
        Poll::Pending
    }
    // Second poll returns Ready(42) — but may be polled again
}
```

## How to Fix

1. **Always call `wake_by_ref()` before returning `Pending`**

```rust
use std::task::{Context, Poll};
use std::future::Future;
use std::pin::Pin;
use std::time::{Duration, Instant};

struct DelayedValue {
    value: i32,
    deadline: Instant,
}

impl Future for DelayedValue {
    type Output = i32;

    fn poll(self: Pin<&mut Self>, cx: &mut Context) -> Poll<i32> {
        if Instant::now() >= self.deadline {
            Poll::Ready(self.value)
        } else {
            cx.waker().wake_by_ref(); // Schedule re-poll
            Poll::Pending
        }
    }
}
```

2. **Use state machines to track polling progress**

```rust
use std::future::Future;
use std::pin::Pin;
use std::task::{Context, Poll};

enum CountdownState { Counting(u32), Done }

struct Countdown { state: CountdownState }

impl Future for Countdown {
    type Output = String;

    fn poll(mut self: Pin<&mut Self>, cx: &mut Context) -> Poll<String> {
        match self.state {
            CountdownState::Counting(0) => {
                self.state = CountdownState::Done;
                Poll::Ready("Complete".to_string())
            }
            CountdownState::Counting(n) => {
                println!("Tick: {}", n);
                self.state = CountdownState::Counting(n - 1);
                cx.waker().wake_by_ref();
                Poll::Pending
            }
            CountdownState::Done => Poll::Ready("Already done".to_string()),
        }
    }
}

#[tokio::main]
async fn main() {
    println!("{}", Countdown { state: CountdownState::Counting(3) }.await);
}
```

3. **Don't poll after Ready — use a done flag**

```rust
use std::future::Future;
use std::pin::Pin;
use std::task::{Context, Poll};

struct OneShot { value: Option<i32> }

impl Future for OneShot {
    type Output = i32;

    fn poll(mut self: Pin<&mut Self>, _cx: &mut Context) -> Poll<i32> {
        match self.value.take() {
            Some(v) => Poll::Ready(v),
            None => Poll::Ready(-1), // Already consumed
        }
    }
}
```

## Examples

```rust
use std::future::Future;
use std::pin::Pin;
use std::task::{Context, Poll};
use std::time::{Duration, Instant};

struct Timer { deadline: Instant }

impl Timer {
    fn new(duration: Duration) -> Self {
        Timer { deadline: Instant::now() + duration }
    }
}

impl Future for Timer {
    type Output = ();

    fn poll(self: Pin<&mut Self>, cx: &mut Context) -> Poll<()> {
        if Instant::now() >= self.deadline {
            Poll::Ready(())
        } else {
            cx.waker().wake_by_ref();
            Poll::Pending
        }
    }
}

#[tokio::main]
async fn main() {
    println!("Waiting...");
    Timer::new(Duration::from_millis(100)).await;
    println!("Done!");
}
```

## Related Errors

- [Future Error]({{< relref "/languages/rust/rust-future-error" >}}) — future issues
- [Pin Error]({{< relref "/languages/rust/rust-pin-error" >}}) — pinning issues
- [Waker Error]({{< relref "/languages/rust/rust-waker-error" >}}) — waker issues
- [Stream Error]({{< relref "/languages/rust/rust-stream-error-rs" >}}) — stream issues
