---
title: "[Solution] tokio Runtime Error Fix"
description: "Fix tokio runtime errors. Handle async runtime configuration, task panics, and resource exhaustion."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Tokio Error

Tokio errors occur when using the `tokio` runtime — spawn panics, task failures, and channel errors.

## Common Causes

```rust
// Spawning on a shutdown runtime
let rt = Runtime::new()?;
rt.shutdown_timeout(Duration::from_secs(0));
rt.spawn(async { }); // ERROR: runtime shut down

// Panicking inside spawn — join error
let handle = tokio::spawn(async {
    panic!("task panicked");
});
handle.await??; // JoinError
```

## How to Fix

1. **Handle spawn errors**

```rust
use tokio::task;

let handle = task::spawn(async {
    // work
    42
});

match handle.await {
    Ok(val) => println!("Result: {}", val),
    Err(e) => eprintln!("Task panicked: {}", e),
}
```

2. **Use JoinSet for structured concurrency**

```rust
use tokio::task::JoinSet;

let mut set = JoinSet::new();
for i in 0..10 {
    set.spawn(async move { i * 2 });
}
while let Some(result) = set.join_next().await {
    println!("Got: {}", result?);
}
```

3. **Use select for multiple futures**

```rust
use tokio::select;

tokio::select! {
    val = async_op_1() => println!("Op1: {}", val),
    val = async_op_2() => println!("Op2: {}", val),
}
```

## Examples

```rust
use tokio::time::{sleep, Duration};
use tokio::task;

#[tokio::main]
async fn main() {
    let handle1 = task::spawn(async {
        sleep(Duration::from_millis(100)).await;
        "task 1"
    });
    let handle2 = task::spawn(async {
        sleep(Duration::from_millis(50)).await;
        "task 2"
    });

    let (r1, r2) = tokio::join!(handle1, handle2);
    println!("{} and {}", r1.unwrap(), r2.unwrap());
}
```

## Related Errors

- [Tokio Error v2]({{< relref "/languages/rust/tokio-error-v2" >}}) — tokio v2
- [Crossbeam Error]({{< relref "/languages/rust/crossbeam-error" >}}) — concurrency
- [MPSC Error]({{< relref "/languages/rust/rust-mpsc-error" >}}) — channels
