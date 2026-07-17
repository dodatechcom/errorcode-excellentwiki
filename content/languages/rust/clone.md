---
title: "[Solution] Rust Does Not Live Long Enough — Lifetime Too Short"
description: "Fix Rust 'does not live long enough' error. Learn why references must outlive the data they point to and how to extend lifetimes."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Does Not Live Long Enough — Lifetime Too Short

A compiler error with the message "does not live long enough" occurs when a reference outlives the data it points to. The referenced data is dropped before the reference is done being used.

## Description

In Rust, a reference must not outlive the value it refers to. This is enforced by the borrow checker. The error occurs when:

- A reference is returned from a function that owns the data.
- A reference is stored in a struct that outlives the source data.
- A reference escapes a scope where the data is valid.

This prevents dangling references — pointers to freed memory — which are undefined behavior in C/C++.

Common scenarios:

- **Returning reference to local variable** — the variable is dropped when the function returns.
- **Storing reference in struct** — struct lives longer than the borrowed data.
- **Closure capturing reference** — closure outlives the borrowed value.
- **Thread spawning with reference** — thread outlives the borrowed data.

## Common Causes

```rust
// Cause 1: Returning reference to local variable
fn create_string() -> &str {
    let s = String::from("hello");
    &s // Error: `s` does not live long enough
}

// Cause 2: Storing reference in struct
struct Holder<'a> {
    data: &'a str,
}

fn create_holder() -> Holder {
    let s = String::from("hello");
    Holder { data: &s } // Error: `s` does not live long enough
}

// Cause 3: Reference in closure
fn create_closure() -> Box<dyn Fn() -> &str> {
    let s = String::from("hello");
    Box::new(move || &s) // Error: `s` does not live long enough
}

// Cause 4: Reference escapes scope
fn get_ref() -> &'static str {
    let local = String::from("data");
    let r = &local;
    r // Error: borrowed value does not live long enough
}
```

## Solutions

### Fix 1: Return owned values instead of references

```rust
// Wrong
fn create_string() -> &str {
    let s = String::from("hello");
    &s
}

// Correct
fn create_string() -> String {
    String::from("hello")
}
```

### Fix 2: Use 'static lifetime with leak or static data

```rust
// Wrong
fn create_static() -> &'static str {
    let s = String::from("hello");
    &s
}

// Correct — use a string literal
fn create_static() -> &'static str {
    "hello"
}

// Or leak the string (use carefully!)
fn create_leaked() -> &'static str {
    Box::leak(String::from("hello").into_boxed_str())
}
```

### Fix 3: Pass data ownership to the struct

```rust
// Wrong — struct holds reference
struct Holder<'a> {
    data: &'a str,
}

// Correct — struct owns the data
struct Holder {
    data: String,
}

fn create_holder() -> Holder {
    let s = String::from("hello");
    Holder { data: s }
}
```

### Fix 4: Use Arc for shared ownership across threads

```rust
use std::sync::Arc;
use std::thread;

// Wrong
fn spawn_thread() {
    let s = String::from("hello");
    let r = &s;
    thread::spawn(move || {
        println!("{}", r); // Error: `s` does not live long enough
    });
}

// Correct
fn spawn_thread() {
    let s = Arc::new(String::from("hello"));
    let s_clone = Arc::clone(&s);
    thread::spawn(move || {
        println!("{}", s_clone);
    });
}
```

## Examples

```rust
fn main() {
    let r;
    {
        let x = 5;
        r = &x; // Error: `x` does not live long enough
    }
    println!("{}", r);
}
```

Output:
```
error[E0597]: `x` does not live long enough
```

## Related Errors

- [Lifetime]({{< relref "/languages/rust/lifetime" >}}) — missing lifetime specifier in function signatures.
- [Borrow Checker]({{< relref "/languages/rust/borrow-checker" >}}) — cannot borrow as mutable because already borrowed.
- [Move]({{< relref "/languages/rust/move" >}}) — using a value after it has been moved.
