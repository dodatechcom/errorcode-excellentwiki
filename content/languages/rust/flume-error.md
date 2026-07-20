---
title: "[Solution] flume Channel Error Fix"
description: "Fix flume channel errors. Handle sender/receiver lifecycle, bounded channels, and async receivers."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Flume Error

Flume errors occur when using the `flume` crate for async/sync channels — send/recv failures and bounded channel overflow.

## Common Causes

```rust
// Sending on disconnected channel
let (tx, rx) = flume::unbounded();
drop(rx);
tx.send(42).unwrap(); // Err: Disconnected

// Bounded channel full
let (tx, rx) = flume::bounded(1);
tx.send(1).unwrap();
tx.try_send(2).unwrap(); // Err: Full
```

## How to Fix

1. **Handle disconnection**

```rust
use flume;

let (tx, rx) = flume::unbounded();
if tx.send("hello").is_err() {
    eprintln!("Receiver dropped");
}
```

2. **Use try_send for non-blocking**

```rust
use flume;

let (tx, rx) = flume::bounded(10);
match tx.try_send("data") {
    Ok(()) => println!("Sent"),
    Err(flume::TrySendError::Full(_)) => eprintln!("Full"),
    Err(flume::TrySendError::Disconnected(_)) => eprintln!("Disconnected"),
}
```

## Examples

```rust
use flume;
use std::thread;

fn main() {
    let (tx, rx) = flume::unbounded();

    for i in 0..5 {
        let tx = tx.clone();
        thread::spawn(move || tx.send(format!("msg {}", i)).unwrap());
    }
    drop(tx);

    while let Ok(msg) = rx.recv() {
        println!("Got: {}", msg);
    }
}
```

## Related Errors

- [MPSC Error]({{< relref "/languages/rust/rust-mpsc-error" >}}) — std channels
- [Channel Error]({{< relref "/languages/rust/rust-channel-error" >}}) — channel issues
- [Tokio Error]({{< relref "/languages/rust/tokio-error" >}}) — async channels
