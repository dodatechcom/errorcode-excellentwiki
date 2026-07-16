---
title: "[Solution] Rust Tokio Runtime Error — Async Runtime Error"
description: "Fix Rust tokio runtime error. Learn why tokio async runtime fails with nested runtimes, missing runtimes, and blocking in async contexts."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
tags: ["tokio", "async", "runtime", "thread", "block"]
weight: 5
---

# Tokio Runtime Error — Async Runtime Error

A tokio error like "Cannot start a runtime from within a runtime" or "there is no reactor running" occurs when async code is used incorrectly with respect to the tokio runtime.

## Description

Tokio is Rust's most popular async runtime. It must be created before async tasks can run. Common errors include:

- **Nested runtime** — starting a new runtime inside an existing one.
- **Missing runtime** — using async functions without a runtime.
- **Blocking in async** — calling blocking code in an async context.
- **Runtime dropped** — runtime dropped while tasks are running.

These errors are caught at runtime because they depend on execution context.

Common scenarios:

- **Calling `block_on` inside async** — `runtime.block_on()` inside a task.
- **Creating another runtime** — double runtime inside `#[tokio::main]`.
- **Blocking I/O** — `std::fs::read_to_string` in an async task.
- **Forgetting `#[tokio::main]`** — calling async functions from sync main.

## Common Causes

```rust
// Cause 1: Nested runtime
use tokio::runtime::Runtime;

fn main() {
    let rt1 = Runtime::new().unwrap();
    rt1.block_on(async {
        let rt2 = Runtime::new().unwrap(); // ERROR: nested runtime
        rt2.block_on(async { println!("nested"); });
    });
}

// Cause 2: Missing runtime
async fn do_work() { println!("async"); }
fn main() { do_work(); } // nothing happens

// Cause 3: Blocking in async
#[tokio::main]
async fn main() {
    std::thread::sleep(std::time::Duration::from_secs(10)); // blocks runtime
}

// Cause 4: Runtime inside async fn
#[tokio::main]
async fn main() {
    let rt = tokio::runtime::Runtime::new().unwrap(); // ERROR
}
```

## Solutions

### Fix 1: Use spawn_blocking for blocking ops

```rust
#[tokio::main]
async fn main() {
    let data = tokio::task::spawn_blocking(|| {
        std::fs::read_to_string("file.txt").unwrap()
    }).await.unwrap();
    println!("Read {} bytes", data.len());
}
```

### Fix 2: Use tokio::fs for async file ops

```rust
#[tokio::main]
async fn main() {
    let data = tokio::fs::read_to_string("file.txt").await.unwrap();
    println!("{} bytes", data.len());
}
```

### Fix 3: Use Handle::current instead of new runtime

```rust
#[tokio::main]
async fn main() {
    let handle = tokio::runtime::Handle::current();
    let result = handle.spawn_blocking(|| 42).await.unwrap();
    println!("Result: {}", result);
}
```

### Fix 4: Use block_on from sync code

```rust
use tokio::runtime::Runtime;

async fn work() -> String { "done".to_string() }

fn main() {
    let rt = Runtime::new().unwrap();
    let result = rt.block_on(work());
    println!("Result: {}", result);
}
```

## Examples

```rust
use tokio::runtime::Runtime;

fn main() {
    let rt1 = Runtime::new().unwrap();
    rt1.block_on(async {
        let rt2 = Runtime::new().unwrap();
        rt2.block_on(async {}).unwrap();
    });
}
```

Output:
```
thread 'main' panicked at 'Cannot start a runtime from within a runtime.'
```

## Related Errors

- [Async Await]({{< relref "/languages/rust/async-await-2" >}}) — async fn not found.
- [Thread Panic]({{< relref "/languages/rust/thread-panic-2" >}}) — thread panics.
- [Stack Overflow]({{< relref "/languages/rust/stack-overflow-2" >}}) — thread stack overflow.
