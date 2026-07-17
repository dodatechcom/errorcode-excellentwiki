---
title: "[Solution] Rust Does Not Live Long Enough — Borrowed Value Dropped"
description: "Fix Rust 'does not live long enough' error. Learn why references must outlive their data and how to return owned values or extend lifetimes."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Does Not Live Long Enough — Borrowed Value Dropped

A compiler error with the message "does not live long enough" occurs when a reference outlives the data it points to — the data is dropped before the reference stops being used.

## Description

Rust guarantees references are always valid by ensuring the referenced data lives at least as long as the reference. The borrow checker enforces this by comparing scopes. If the data is dropped (e.g., when leaving a block) while a reference to it still exists, the compiler rejects the code.

This prevents dangling pointers — a critical class of bugs in C/C++ that leads to undefined behavior.

Common scenarios:

- **Reference escapes a block** — data dropped at block end, reference used after.
- **Returning reference to local** — local variable dropped when function returns.
- **Thread with borrowed data** — thread outlives the borrowed data.
- **Storing reference in struct** — struct outlives the borrowed source.

## Common Causes

```rust
// Cause 1: Reference escapes block
let r;
{
    let x = 5;
    r = &x; // Error: x doesn't live long enough
}
println!("{}", r);

// Cause 2: Returning reference to local
fn create() -> &str {
    let s = String::from("hello");
    &s // Error: s dropped at function end
}

// Cause 3: Struct outlives data
struct Holder<'a> { data: &'a str }
let holder;
{
    let s = String::from("hi");
    holder = Holder { data: &s };
} // s dropped here
println!("{}", holder.data); // Error

// Cause 4: Thread outlives data
let r;
let s = String::from("hello");
let handle = std::thread::spawn(move || {
    r = &s; // Error: s is moved but r is created outside
});
```

## Solutions

### Fix 1: Return owned values

```rust
fn create() -> String {
    String::from("hello")
}

fn main() {
    let s = create();
    println!("{}", s);
}
```

### Fix 2: Return 'static references

```rust
fn create() -> &'static str {
    "hello" // string literal has 'static lifetime
}

fn main() {
    let s = create();
    println!("{}", s);
}
```

### Fix 3: Own the data in the struct

```rust
struct Holder {
    data: String,
}

fn main() {
    let holder;
    {
        let s = String::from("hello");
        holder = Holder { data: s }; // struct owns the String
    }
    println!("{}", holder.data); // OK
}
```

### Fix 4: Extend the data's scope

```rust
fn main() {
    let s = String::from("hello");
    let r = &s;
    println!("{}", r); // r used here
    // s dropped here — fine, r no longer used
}
```

## Examples

```rust
fn main() {
    let reference;
    {
        let value = 42;
        reference = &value;
    }
    println!("{}", reference);
}
```

Output:
```
error[E0597]: `value` does not live long enough
```

## Related Errors

- [Lifetime]({{< relref "/languages/rust/lifetime-2" >}}) — missing lifetime specifier.
- [Borrow Checker]({{< relref "/languages/rust/borrow-checker-2" >}}) — mutable/immutable conflict.
- [Move]({{< relref "/languages/rust/move-2" >}}) — using a value after it was moved.
