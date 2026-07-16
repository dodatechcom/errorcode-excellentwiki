---
title: "[Solution] Rust Unwrap Panic on None / Err — Runtime Error Fix"
description: "Fix Rust unwrap() panics on None and Err values. Use proper error handling with match, if-let, and the ? operator instead."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["unwrap", "panic", "none", "error", "option", "result", "handling"]
weight: 5
---

# Unwrap Panic on None / Err

The error `called unwrap() on a None value` or `called Result::unwrap() on an Err` occurs when you call `.unwrap()` on an `Option::None` or `Result::Err`. This causes the thread to panic immediately with no way to recover.

## Description

Rust's `Option<T>` and `Result<T, E>` types represent possible absence or failure. The `.unwrap()` method extracts the inner value or panics if it is `None`/`Err`. While convenient for prototyping, unwrap panics are a common source of production crashes.

The fix is to handle both cases explicitly using `match`, `if let`, `unwrap_or`, or the `?` operator.

## Common Causes

- **Unwrapping fallible operations** — file I/O, network requests, parsing can all fail
- **Unwrapping Option from collection access** — `.first().unwrap()` on an empty collection
- **Chain of unwraps** — multiple unwraps in sequence where any can panic
- **Prototype code in production** — unwrap used during development left in shipping code

## How to Fix

### Fix 1: Use match for explicit handling

```rust
match std::fs::read_to_string("config.txt") {
    Ok(contents) => println!("{}", contents),
    Err(e) => eprintln!("failed to read config: {}", e),
}
```

### Fix 2: Use if-let for simple cases

```rust
let name: Option<&str> = Some("Alice");
if let Some(n) = name {
    println!("Hello, {}!", n);
} else {
    println!("No name provided");
}
```

### Fix 3: Use unwrap_or and unwrap_or_default

```rust
let config_value = config.get("timeout")
    .unwrap_or("30")
    .parse::<u64>()
    .unwrap_or(30);
```

### Fix 4: Use the ? operator in functions that return Result

```rust
use std::fs;
use std::io;

fn read_config() -> Result<String, io::Error> {
    let contents = fs::read_to_string("config.txt")?; // propagates error
    Ok(contents)
}
```

## Examples

```rust
fn main() {
    let numbers: Vec<i32> = vec![1, 2, 3];
    let tenth = numbers.get(9).unwrap(); // panics: called on None
}
```

Output:
```
thread 'main' panicked at 'called `Option::unwrap()` on a `None` value'
```

## Related Errors

- [expect-fail]({{< relref "/languages/rust/expect-fail" >}}) — unwrap with custom panic messages via expect().
- [overflow-panic]({{< relref "/languages/rust/overflow" >}}) — arithmetic overflow panics.
- [type-mismatch]({{< relref "/languages/rust/type-mismatch" >}}) — type errors that may lead to unwrap usage.
