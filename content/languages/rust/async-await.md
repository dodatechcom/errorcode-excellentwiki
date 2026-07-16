---
title: "[Solution] Rust Async/Await Error — Async Function Not Found"
description: "Fix Rust async/await errors. Learn why async code fails to compile or run and how to properly use async functions and futures."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
tags: ["async", "await", "future", "tokio", "runtime"]
weight: 5
---

# Async/Await Error — Async Function Not Found

Errors related to async/await in Rust include messages like "async function not found", "future is not Send", or "missing async runtime". These occur when async code is misused or when the async ecosystem is not properly configured.

## Description

Rust's async/await is zero-cost and requires a runtime (like tokio) to execute. The compiler generates state machines for async functions, but doesn't include a runtime. Common issues:

- **Missing runtime** — async code has no executor to run on.
- **Not Send/Sync** — future can't be sent across threads.
- **Missing .await** — forgetting to await a future.
- **Blocking in async** — synchronous operations blocking the runtime.
- **Lifetime issues** — async functions with complex lifetime requirements.

## Common Causes

```rust
// Cause 1: Forgetting .await
async fn get_data() -> String {
    "data".to_string()
}

#[tokio::main]
async fn main() {
    let data = get_data(); // WARNING: future not polled!
    println!("{}", data); // prints future, not "data"
}

// Cause 2: Missing runtime
async fn do_work() {
    println!("async work");
}

fn main() {
    do_work(); // does nothing, future not executed
}

// Cause 3: Non-Send future
use std::rc::Rc;

#[tokio::main]
async fn main() {
    let data = Rc::new(42); // Rc is not Send
    tokio::task::spawn(async move {
        println!("{}", data);
    }).await.unwrap(); // ERROR: future !Send
}

// Cause 4: Blocking in async context
#[tokio::main]
async fn main() {
    std::thread::sleep(std::time::Duration::from_secs(5)); // blocks runtime
}
```

## Solutions

### Fix 1: Always .await futures

```rust
// Wrong
#[tokio::main]
async fn main() {
    let data = get_data(); // future not polled
    println!("{}", data);
}

// Correct
#[tokio::main]
async fn main() {
    let data = get_data().await; // await the future
    println!("{}", data);
}

async fn get_data() -> String {
    "data".to_string()
}
```

### Fix 2: Use a runtime for async code

```rust
// Wrong — no runtime
async fn do_work() -> i32 {
    42
}

fn main() {
    let result = do_work(); // future not executed
}

// Correct — use a runtime
#[tokio::main]
async fn main() {
    let result = do_work().await;
    println!("Result: {}", result);
}

async fn do_work() -> i32 {
    42
}
```

### Fix 3: Use Arc instead of Rc for async tasks

```rust
use std::sync::Arc;

// Wrong
use std::rc::Rc;

#[tokio::main]
async fn main() {
    let data = Rc::new(42); // not Send
    tokio::task::spawn(async move {
        println!("{}", data);
    }).await.unwrap();
}

// Correct
#[tokio::main]
async fn main() {
    let data = Arc::new(42); // Send
    tokio::task::spawn(async move {
        println!("{}", data);
    }).await.unwrap();
}
```

### Fix 4: Use spawn_blocking for sync operations

```rust
// Wrong
#[tokio::main]
async fn main() {
    let data = std::fs::read_to_string("file.txt").unwrap(); // blocks
}

// Correct
#[tokio::main]
async fn main() {
    let data = tokio::task::spawn_blocking(|| {
        std::fs::read_to_string("file.txt").unwrap()
    }).await.unwrap();
    println!("Read {} bytes", data.len());
}
```

## Examples

```rust
async fn hello() {
    println!("Hello from async!");
}

fn main() {
    hello(); // Does nothing — future not polled
    println!("This prints, but hello() doesn't");
}
```

Output:
```
This prints, but hello() doesn't
```

## Related Errors

- [Tokio]({{< relref "/languages/rust/tokio" >}}) — tokio runtime errors.
- [Pin]({{< relref "/languages/rust/pin" >}}) — cannot move pinned value.
- [Thread Panic]({{< relref "/languages/rust/thread-panic" >}}) — thread panics.
