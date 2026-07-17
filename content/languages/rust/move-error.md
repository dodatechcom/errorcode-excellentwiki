---
title: "[Solution] Rust Use of Moved Value — Compiler Error Fix"
description: "Fix Rust 'use of moved value' error. Understand ownership transfer, Copy trait, and how to reuse values after moves."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Use of Moved Value — Compiler Error

The error `use of moved value` occurs when you attempt to use a value after it has been moved to another owner. In Rust, moving a value transfers ownership, and the original variable can no longer be accessed.

## Description

Rust's ownership system ensures that each value has exactly one owner. When you assign a value to another variable or pass it to a function, ownership is transferred (moved) unless the type implements the `Copy` trait. After a move, the original variable is considered invalid.

This prevents double-free errors and ensures memory safety without a garbage collector.

## Common Causes

- **Passing to a function** — passing an owned value to a function transfers ownership
- **Assignment** — assigning a non-Copy value to another variable moves it
- **Iteration** — `for item in vec` moves the vector; use `&vec` for borrowing
- **Pattern matching** — destructuring a value can move its contents

## How to Fix

### Fix 1: Clone the value before moving

```rust
let s1 = String::from("hello");
let s2 = s1.clone(); // s1 is still valid
println!("{} {}", s1, s2);
```

### Fix 2: Borrow instead of move

```rust
// Wrong — moves v
fn print_vec(v: Vec<i32>) {
    println!("{:?}", v);
}

// Correct — borrow the vector
fn print_vec(v: &Vec<i32>) {
    println!("{:?}", v);
}

let v = vec![1, 2, 3];
print_vec(&v); // v is still valid
```

### Fix 3: Use the Copy trait for simple types

```rust
// i32 implements Copy, so it's copied, not moved
let x = 5;
let y = x; // x is still valid
println!("{} {}", x, y);
```

### Fix 4: Return values to transfer ownership back

```rust
fn process_and_return(mut data: Vec<i32>) -> Vec<i32> {
    data.push(4);
    data // return ownership to caller
}

let mut v = vec![1, 2, 3];
v = process_and_return(v); // v is valid again
```

## Examples

```rust
fn main() {
    let s1 = String::from("hello");
    let s2 = s1; // s1 is moved to s2
    println!("{}", s1); // Error: use of moved value
}
```

Output:
```
error[E0382]: borrow of moved value: `s1`
```

## Related Errors

- [borrow-checker]({{< relref "/languages/rust/borrow-checker" >}}) — simultaneous mutable and immutable borrows.
- [clone]({{< relref "/languages/rust/clone" >}}) — cloning values to avoid moves.
- [unwrap-none]({{< relref "/languages/rust/unwrap-none" >}}) — unwrapping None values.
