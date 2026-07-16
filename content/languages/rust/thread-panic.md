---
title: "[Solution] Rust Thread Panic — Thread Panicked Error"
description: "Fix Rust thread panic. Learn why threads panic, how panic propagates across threads, and how to handle panics gracefully."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
tags: ["thread", "panic", "spawn", "catch_unwind", "panic-hook"]
weight: 5
---

# Thread Panic — Thread Panicked Error

A panic with the message "thread 'main' panicked at ..." occurs when a thread encounters an unrecoverable error. The panic message includes the location and a description of what went wrong.

## Description

In Rust, `panic!` is used for unrecoverable errors. When a thread panics:

- The thread unwinds its stack (running destructors) and terminates.
- The panic is propagated to the parent thread via `join()`.
- If the main thread panics, the entire process aborts (after printing the panic message).

Panics are different from `Result` errors — they're meant for situations where recovery is impossible or the program state is corrupted.

Common scenarios:

- **Explicit panic!** — `panic!("something went wrong")`.
- **unwrap() on None/Err** — calling unwrap on a failed operation.
- **Index out of bounds** — accessing invalid indices.
- **Assertion failures** — `assert!`, `assert_eq!` macros.
- **Integer overflow** — in debug mode.

## Common Causes

```rust
use std::thread;

// Cause 1: Explicit panic
thread::spawn(|| {
    panic!("explicit panic in thread");
});

// Cause 2: unwrap on None
let v: Vec<i32> = vec![];
let first = v.first().unwrap(); // panics

// Cause 3: unwrap on Err
let num: Result<i32, _> = "abc".parse();
num.unwrap(); // panics

// Cause 4: Index out of bounds
let arr = [1, 2, 3];
let val = arr[10]; // panics

// Cause 5: Failed thread join
let handle = thread::spawn(|| {
    panic!("child thread panic");
});
handle.join().unwrap(); // panics with the child's panic message
```

## Solutions

### Fix 1: Use catch_unwind to handle panics

```rust
use std::panic;

fn main() {
    let result = panic::catch_unwind(|| {
        println!("about to panic");
        panic!("oh no!");
        println!("this won't print");
    });

    match result {
        Ok(_) => println!("No panic occurred"),
        Err(e) => {
            let msg = e.downcast_ref::<&str>().unwrap_or(&"unknown panic");
            println!("Caught panic: {}", msg);
        }
    }
}
```

### Fix 2: Handle thread panics with join

```rust
use std::thread;

fn main() {
    let handle = thread::spawn(|| {
        let result: Result<i32, String> = Err(String::from("something failed"));
        result.unwrap(); // panics in the thread
    });

    match handle.join() {
        Ok(value) => println!("Thread completed: {:?}", value),
        Err(e) => {
            if let Some(msg) = e.downcast_ref::<&str>() {
                println!("Thread panicked: {}", msg);
            } else if let Some(msg) = e.downcast_ref::<String>() {
                println!("Thread panicked: {}", msg);
            } else {
                println!("Thread panicked with unknown message");
            }
        }
    }
}
```

### Fix 3: Set a custom panic hook

```rust
use std::panic;

fn main() {
    // Set custom panic handler
    panic::set_hook(Box::new(|info| {
        let location = info.location().map(|l| {
            format!("{}:{}:{}", l.file(), l.line(), l.column())
        }).unwrap_or_else(|| "unknown".to_string());

        let message = if let Some(s) = info.payload().downcast_ref::<&str>() {
            s.to_string()
        } else if let Some(s) = info.payload().downcast_ref::<String>() {
            s.clone()
        } else {
            "Box<dyn Any>".to_string()
        };

        eprintln!("Custom panic handler: {} at {}", message, location);
    }));

    panic!("custom hook test");
}
```

### Fix 4: Use Result instead of panic

```rust
// Wrong — uses unwrap which panics
fn parse_number(s: &str) -> i32 {
    s.parse().unwrap()
}

// Correct — returns Result
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

## Examples

```rust
fn main() {
    let v = vec![1, 2, 3];
    println!("{}", v[5]); // panics
}
```

Output:
```
thread 'main' panicked at 'index out of bounds: the len is 3 but the index is 5'
```

## Related Errors

- [Stack Overflow]({{< relref "/languages/rust/stack-overflow" >}}) — thread overflows its stack.
- [Unwrap Err]({{< relref "/languages/rust/unwrap-err" >}}) — calling unwrap on an Err Result.
- [Unwrap None]({{< relref "/languages/rust/unwrap-none" >}}) — calling unwrap on a None Option.
