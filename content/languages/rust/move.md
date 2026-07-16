---
title: "[Solution] Rust Use of Moved Value — Move Error"
description: "Fix Rust use of moved value error. Learn why Rust moves values by default and how to use Clone, Copy, or references to fix move errors."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
tags: ["move", "ownership", "clone", "copy", "reference", "value"]
weight: 5
---

# Use of Moved Value — Move Error

A compiler error with the message "use of moved value" occurs when you try to use a value after it has been moved to another variable or function. In Rust, assigning a value to another variable or passing it to a function by default moves ownership.

## Description

Rust's ownership system ensures memory safety without a garbage collector. When you assign a value like `let b = a`, the value is _moved_ from `a` to `b`. After the move, `a` is no longer valid. This prevents double-free errors and ensures each value has exactly one owner.

Types that implement the `Copy` trait (like integers, booleans, and characters) are copied instead of moved. Types like `String`, `Vec`, and custom structs are moved by default.

Common scenarios:

- **Passing to a function** — `func(my_string)` moves ownership.
- **Assigning to another variable** — `let b = my_string` moves it.
- **Returning from a function** — moving ownership to the caller.
- **Collection operations** — removing from a `Vec` moves the element out.

## Common Causes

```rust
// Cause 1: Passing String to a function
fn print_string(s: String) {
    println!("{}", s);
}

let name = String::from("Alice");
print_string(name);
println!("{}", name); // Error: value used here after move

// Cause 2: Assigning to another variable
let s1 = String::from("hello");
let s2 = s1;
println!("{}", s1); // Error: value used here after move

// Cause 3: Using in multiple match arms
let opt = Some(String::from("value"));
match opt {
    Some(s) => println!("Got: {}", s),
    None => println!("None"),
}
match opt { // Error: value used here after move
    Some(s) => println!("Got again: {}", s),
    None => println!("None again"),
}

// Cause 4: Using after iteration
let names = vec![String::from("Alice"), String::from("Bob")];
for name in names {
    println!("{}", name);
}
println!("{:?}", names); // Error: value used here after move
```

## Solutions

### Fix 1: Clone the value

```rust
// Wrong
let s1 = String::from("hello");
let s2 = s1;
println!("{}", s1); // Error

// Correct
let s1 = String::from("hello");
let s2 = s1.clone();
println!("{} {}", s1, s2); // Both valid
```

### Fix 2: Use references instead of moving

```rust
// Wrong
fn print_string(s: String) {
    println!("{}", s);
}

let name = String::from("Alice");
print_string(name);
println!("{}", name); // Error

// Correct
fn print_string(s: &str) {
    println!("{}", s);
}

let name = String::from("Alice");
print_string(&name);
println!("{}", name); // Still valid
```

### Fix 3: Implement Copy for simple types

```rust
// Wrong — String doesn't implement Copy
let s1 = String::from("hello");
let s2 = s1;

// Correct — use types that implement Copy
let n1 = 42;
let n2 = n1; // Copied, not moved
println!("{} {}", n1, n2); // Both valid
```

### Fix 4: Use references in loops

```rust
// Wrong — moves each element
let names = vec![String::from("Alice"), String::from("Bob")];
for name in names {
    println!("{}", name);
}
// names is no longer valid

// Correct — borrow elements
let names = vec![String::from("Alice"), String::from("Bob")];
for name in &names {
    println!("{}", name);
}
println!("Total: {}", names.len()); // Still valid
```

## Examples

```rust
fn main() {
    let greeting = String::from("Hello, world!");
    let moved_greeting = greeting;

    // This line causes the error
    println!("{}", greeting);
}
```

Output:
```
error[E0382]: borrow of moved value: `greeting`
```

## Related Errors

- [Borrow Checker]({{< relref "/languages/rust/borrow-checker" >}}) — cannot borrow as mutable because already borrowed.
- [Clone]({{< relref "/languages/rust/clone" >}}) — value doesn't live long enough.
- [Lifetime]({{< relref "/languages/rust/lifetime" >}}) — references don't live long enough.
