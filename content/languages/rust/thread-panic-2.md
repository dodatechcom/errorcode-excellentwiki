---
title: "[Solution] Rust Thread Panic — Thread Panicked at Message"
description: "Fix Rust thread panic. Learn how thread panics propagate, how to catch them, and how to prevent panics in threaded code."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
tags: ["thread", "panic", "spawn", "catch_unwind", "join"]
weight: 5
---

# Thread Panic — Thread Panicked at Message

A panic with the message "thread 'main' panicked at ..." occurs when a thread encounters an unrecoverable error. The panic message includes the source location and description.

## Description

When a thread panics in Rust:
1. The thread unwinds its stack (running destructors) and terminates.
2. The panic propagates to the parent via `thread::JoinHandle::join()`.
3. If the main thread panics, the process prints a message and aborts.

Panics are distinct from `Result` errors — they're for truly unrecoverable situations. Use `Result` for expected failures; reserve `panic!` for programmer errors.

Common scenarios:

- **Explicit panic!** — `panic!("unexpected state")`.
- **unwrap() on None/Err** — failed operation.
- **Index out of bounds** — accessing invalid index.
- **Assertion failure** — `assert!`, `assert_eq!` failing.
- **Integer overflow** — in debug builds.

## Common Causes

```rust
use std::thread;

// Cause 1: Explicit panic
thread::spawn(|| {
    panic!("something went wrong");
});

// Cause 2: unwrap on None
let v: Vec<i32> = vec![];
let first = v.first().unwrap(); // panics

// Cause 3: unwrap on Err
"abc".parse::<i32>().unwrap(); // panics

// Cause 4: Index out of bounds
let arr = [1, 2, 3];
let val = arr[10]; // panics

// Cause 5: Propagated child panic
let h = thread::spawn(|| { panic!("child crash"); });
h.join().unwrap(); // panics with child's message
```

## Solutions

### Fix 1: Catch panics with catch_unwind

```rust
use std::panic;

let result = panic::catch_unwind(|| {
    println!("before panic");
    panic!("oops");
    println!("after panic");
});

match result {
    Ok(_) => println!("No panic"),
    Err(e) => {
        let msg = e.downcast_ref::<&str>().unwrap_or(&"unknown");
        println!("Caught: {}", msg);
    }
}
```

### Fix 2: Handle join errors

```rust
use std::thread;

let h = thread::spawn(|| {
    let data: Result<i32, String> = Err("failed".into());
    data.unwrap(); // panics in thread
});

match h.join() {
    Ok(val) => println!("Thread completed: {:?}", val),
    Err(e) => {
        if let Some(msg) = e.downcast_ref::<String>() {
            println!("Thread panicked: {}", msg);
        } else if let Some(msg) = e.downcast_ref::<&str>() {
            println!("Thread panicked: {}", msg);
        }
    }
}
```

### Fix 3: Use Result instead of panic

```rust
fn parse_number(s: &str) -> Result<i32, Box<dyn std::error::Error>> {
    Ok(s.parse()?)
}

fn main() {
    match parse_number("42") {
        Ok(n) => println!("Parsed: {}", n),
        Err(e) => eprintln!("Failed: {}", e),
    }
}
```

### Fix 4: Set a custom panic hook

```rust
use std::panic;

panic::set_hook(Box::new(|info| {
    let location = info.location()
        .map(|l| format!("{}:{}", l.file(), l.line()))
        .unwrap_or_else(|| "unknown".into());
    let message = info.payload()
        .downcast_ref::<&str>()
        .unwrap_or(&"unknown panic");
    eprintln!("[PANIC] {} at {}", message, location);
}));

panic!("custom hook test");
```

## Examples

```rust
fn main() {
    let v = vec![1, 2, 3];
    println!("{}", v[10]);
}
```

Output:
```
thread 'main' panicked at 'index out of bounds: the len is 3 but the index is 10'
```

## Related Errors

- [Stack Overflow]({{< relref "/languages/rust/stack-overflow-2" >}}) — thread overflows its stack.
- [Unwrap Err]({{< relref "/languages/rust/unwrap-err-2" >}}) — unwrap on an Err Result.
- [Unwrap None]({{< relref "/languages/rust/unwrap-none-2" >}}) — unwrap on a None Option.
