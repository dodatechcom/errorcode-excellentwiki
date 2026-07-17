---
title: "[Solution] Rust Tokio Runtime Error — Async Runtime Error"
description: "Fix Rust tokio runtime error. Learn why tokio async runtime fails and how to properly create and use async runtimes."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Tokio Runtime Error — Async Runtime Error

A tokio error with messages like "Cannot start a runtime from within a runtime" or "there is no reactor running" occurs when async code is used incorrectly with respect to the tokio runtime.

## Description

Tokio is Rust's most popular async runtime. It must be created before async tasks can run. Common errors include:

- **Nested runtime** — starting a new runtime inside an existing one.
- **Missing runtime** — using async functions without a runtime.
- **Blocking in async** — calling blocking code in an async context.
- **Runtime dropped** — runtime dropped while tasks are still running.

These errors are caught at runtime, not compile time, because they depend on execution context.

Common scenarios:

- **Calling `block_on` inside async** — `runtime.block_on()` inside a task.
- **Using `#[tokio::main]` and creating another runtime** — double runtime.
- **Blocking I/O in async** — synchronous file I/O in an async task.
- **Forgetting `#[tokio::main]`** — calling async functions from sync main.

## Common Causes

```rust
// Cause 1: Nested runtime
use tokio::runtime::Runtime;

fn main() {
    let rt1 = Runtime::new().unwrap();
    rt1.block_on(async {
        let rt2 = Runtime::new().unwrap(); // ERROR: nested runtime
        rt2.block_on(async {
            println!("nested");
        });
    });
}

// Cause 2: Missing runtime
async fn do_work() {
    println!("async work");
}

fn main() {
    do_work(); // WARNING: nothing happens, future not polled
}

// Cause 3: Blocking in async context
#[tokio::main]
async fn main() {
    let handle = tokio::task::spawn(async {
        std::thread::sleep(std::time::Duration::from_secs(10)); // BLOCKS runtime
        println!("done");
    });
    handle.await.unwrap();
}

// Cause 4: Creating runtime inside async fn
#[tokio::main]
async fn main() {
    let rt = tokio::runtime::Runtime::new().unwrap(); // ERROR
}
```

## Solutions

### Fix 1: Use spawn_blocking for blocking operations

```rust
// Wrong
#[tokio::main]
async fn main() {
    let data = std::fs::read_to_string("file.txt").unwrap(); // blocks runtime
    println!("{}", data.len());
}

// Correct
#[tokio::main]
async fn main() {
    let data = tokio::task::spawn_blocking(|| {
        std::fs::read_to_string("file.txt").unwrap()
    }).await.unwrap();
    println!("{}", data.len());
}
```

### Fix 2: Use tokio::fs for async file operations

```rust
// Wrong
#[tokio::main]
async fn main() {
    let data = std::fs::read_to_string("file.txt").unwrap(); // blocks
}

// Correct
#[tokio::main]
async fn main() {
    let data = tokio::fs::read_to_string("file.txt").await.unwrap();
    println!("{}", data.len());
}
```

### Fix 3: Don't nest runtimes — use handle instead

```rust
// Wrong
#[tokio::main]
async fn main() {
    let rt = tokio::runtime::Runtime::new().unwrap(); // nested runtime
    rt.block_on(async { println!("nested"); }).unwrap();
}

// Correct — use current runtime handle
#[tokio::main]
async fn main() {
    let handle = tokio::runtime::Handle::current();
    let result = handle.spawn_blocking(|| {
        // blocking work here
        42
    }).await.unwrap();
    println!("Result: {}", result);
}
```

### Fix 4: Use runtime block_on from sync code

```rust
use tokio::runtime::Runtime;

async fn do_async_work() -> String {
    tokio::time::sleep(tokio::time::Duration::from_millis(100)).await;
    "done".to_string()
}

fn main() {
    // Create runtime in sync context
    let rt = Runtime::new().unwrap();
    let result = rt.block_on(do_async_work());
    println!("Result: {}", result);
}
```

## Examples

```rust
use tokio::runtime::Runtime;

fn main() {
    let rt1 = Runtime::new().unwrap();
    rt1.block_on(async {
        let rt2 = Runtime::new().unwrap(); // panics
        rt2.block_on(async {}).unwrap();
    });
}
```

Output:
```
thread 'main' panicked at 'Cannot start a runtime from within a runtime.'
```

## Related Errors

- [Async Await]({{< relref "/languages/rust/async-await" >}}) — async fn not found.
- [Thread Panic]({{< relref "/languages/rust/thread-panic" >}}) — thread panics.
- [Stack Overflow]({{< relref "/languages/rust/stack-overflow" >}}) — thread stack overflow.
