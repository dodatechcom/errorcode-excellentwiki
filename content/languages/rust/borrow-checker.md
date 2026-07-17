---
title: "[Solution] Rust Borrow Checker Error — Does Not Live Long Enough"
description: "Fix Rust borrow checker error: reference does not live long enough. Understand ownership, borrowing rules, and lifetime annotations."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Borrow Checker Error — Does Not Live Long Enough

The error `borrow checker: reference does not live long enough` occurs when you attempt to create a reference to data that will be dropped before the reference is used. Rust's borrow checker enforces this at compile time to prevent dangling pointers.

## Description

Rust's ownership system tracks the lifetime of every value. A reference (`&T` or `&mut T`) cannot outlive the data it points to. The borrow checker detects when a reference's scope extends beyond the owning value's lifetime and rejects the code.

Common scenarios include returning references to local variables, storing references in structs that outlive the data, and closures capturing references that are dropped before the closure executes.

## Common Causes

- **Returning a reference to a local variable** — the local is dropped when the function returns
- **Struct containing a reference** — the struct outlives the borrowed data
- **Closure capturing a short-lived reference** — the closure is used after the reference is invalid
- **Thread boundary crossing** — passing a reference to another thread without sufficient lifetime

## How to Fix

### Fix 1: Return owned data instead of references

```rust
// Wrong — returns reference to local
fn get_name() -> &str {
    let name = String::from("Alice");
    &name // Error: does not live long enough
}

// Correct — return owned String
fn get_name() -> String {
    String::from("Alice")
}
```

### Fix 2: Use lifetime annotations

```rust
// Wrong — compiler can't verify lifetime
fn longest(a: &str, b: &str) -> &str {
    if a.len() > b.len() { a } else { b }
}

// Correct — explicit lifetime
fn longest<'a>(a: &'a str, b: &'a str) -> &'a str {
    if a.len() > b.len() { a } else { b }
}
```

### Fix 3: Clone data to extend ownership

```rust
fn main() {
    let r;
    {
        let x = 5;
        r = &x; // Error: x does not live long enough
    }
    println!("{}", r);

    // Fix: clone the value
    let r;
    {
        let x = 5;
        r = x; // Copy the value
    }
    println!("{}", r);
}
```

### Fix 4: Use Arc for shared ownership across threads

```rust
use std::sync::Arc;
use std::thread;

fn main() {
    let data = Arc::new(vec![1, 2, 3]);
    let data_clone = Arc::clone(&data);

    thread::spawn(move || {
        println!("{:?}", data_clone);
    });
}
```

## Examples

```rust
fn main() {
    let reference_to_nothing;
    {
        let value = String::from("hello");
        reference_to_nothing = &value;
    } // value is dropped here
    // println!("{}", reference_to_nothing); // Error
}
```

Output:
```
error[E0597]: `value` does not live long enough
```

## Related Errors

- [move-error]({{< relref "/languages/rust/move" >}}) — using a value after it has been moved.
- [lifetime-error]({{< relref "/languages/rust/lifetime" >}}) — lifetime mismatch in function signatures.
- [type-mismatch]({{< relref "/languages/rust/type-mismatch" >}}) — type compatibility issues.
