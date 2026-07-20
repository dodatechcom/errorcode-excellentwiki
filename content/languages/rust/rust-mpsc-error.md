---
title: "[Solution] Rust MPSC Error — How to Fix"
description: "Fix MPSC channel errors. Resolve multiple producer, single consumer communication failures."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# MPSC Error

MPSC (Multi-Producer, Single-Consumer) errors occur when using `std::sync::mpsc` channels — sending on closed channels, type mismatches, or channel capacity issues.

## Common Causes

```rust
use std::sync::mpsc;

// Sending on a closed channel
let (tx, rx) = mpsc::channel();
drop(rx); // Receiver dropped
tx.send(42).unwrap(); // ERROR: SendError(42) — receiver gone

// Bounded channel full
let (tx, rx) = mpsc::sync_channel(2);
tx.send(1).unwrap();
tx.send(2).unwrap();
tx.try_send(3).unwrap(); // ERROR: TrySendError::Full(3)

// Type mismatch
let (tx, rx) = mpsc::channel::<String>();
tx.send(42).unwrap(); // ERROR: expected String, found i32
```

## How to Fix

1. **Check channel liveness before sending**

```rust
use std::sync::mpsc;

let (tx, rx) = mpsc::channel();

if tx.send("hello").is_err() {
    eprintln!("Receiver dropped");
}

// Non-blocking send
match tx.try_send("data") {
    Ok(()) => println!("Sent"),
    Err(mpsc::TrySendError::Full(_)) => eprintln!("Full"),
    Err(mpsc::TrySendError::Disconnected(_)) => eprintln!("Disconnected"),
}
```

2. **Clone tx for multi-producer pattern**

```rust
use std::sync::mpsc;
use std::thread;

let (tx, rx) = mpsc::channel();
let mut handles = vec![];

for i in 0..5 {
    let tx = tx.clone();
    handles.push(thread::spawn(move || {
        tx.send(format!("Message from thread {}", i)).unwrap();
    }));
}

drop(tx); // Drop original sender
for h in handles { h.join().unwrap(); }

while let Ok(msg) = rx.recv() {
    println!("Received: {}", msg);
}
```

3. **Use tokio channels for async contexts**

```rust
use tokio::sync::mpsc;

#[tokio::main]
async fn main() {
    let (tx, mut rx) = mpsc::channel(100);

    for i in 0..10 {
        let tx = tx.clone();
        tokio::spawn(async move {
            tx.send(format!("msg {}", i)).await.unwrap();
        });
    }
    drop(tx);

    while let Some(msg) = rx.recv().await {
        println!("Got: {}", msg);
    }
}
```

## Examples

```rust
use std::sync::mpsc;
use std::thread;
use std::time::Duration;

fn main() {
    let (tx, rx) = mpsc::channel();

    // Multiple producers
    for i in 0..3 {
        let tx = tx.clone();
        thread::spawn(move || {
            for j in 0..3 {
                tx.send(format!("Thread {} msg {}", i, j)).unwrap();
                thread::sleep(Duration::from_millis(10));
            }
        });
    }
    drop(tx);

    // Single consumer
    let mut count = 0;
    for msg in rx {
        count += 1;
        println!("[{}] {}", count, msg);
    }
    println!("Total: {} messages", count);
}
```

## Related Errors

- [Channel Error]({{< relref "/languages/rust/rust-channel-error" >}}) — channel issues
- [Flume Error]({{< relref "/languages/rust/flume-error" >}}) — flume crate
- [Tokio Error]({{< relref "/languages/rust/tokio-error" >}}) — async channels
