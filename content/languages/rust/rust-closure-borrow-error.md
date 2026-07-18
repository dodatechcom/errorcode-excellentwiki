---
title: "[Solution] Rust Closure Borrow Error — How to Fix"
description: "Fix Rust closure borrow errors. Learn why closures capture references incorrectly and how to use move, clone, or lifetime annotations."
languages: ["rust"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
comments: true
---

# Closure Borrow Error

Closures in Rust capture variables from their surrounding scope. A closure borrow error occurs when a closure tries to borrow a variable mutably while another immutable borrow exists, or when the captured reference outlives the closure.

## Why It Happens

- The closure borrows a variable that is already immutably borrowed elsewhere
- The closure captures a reference by reference instead of by move
- A mutable closure is called while an immutable reference to its capture is still in use
- The closure is passed to a function that requires `'static` but captures a short-lived reference

## Common Error Messages

- `cannot borrow as mutable because it is also borrowed as immutable`
- `closure may outlive the current function, but it borrows`
- `expected a `Fn` closure, but this closure mutably borrows`
- `moved value does not implement Copy`

## How to Fix It

### Fix 1: Use `move` to transfer ownership into the closure

```rust
fn main() {
    let name = String::from("Alice");
    let greet = move || println!("Hello, {}", name);
    greet();
}
```

### Fix 2: Clone the captured variable

```rust
fn main() {
    let data = vec![1, 2, 3];
    let data_clone = data.clone();
    let handle = std::thread::spawn(move || println!("{:?}", data_clone));
    println!("Original: {:?}", data);
    handle.join().unwrap();
}
```

### Fix 3: Restructure borrows to avoid overlap

```rust
fn main() {
    let mut v = vec![1, 2, 3];
    {
        let r = &v;
        println!("Borrowed: {:?}", r);
    }
    v.push(4);
    let closure = || println!("After push: {:?}", v);
    closure();
}
```

## Common Scenarios

1. **Threading** — passing closures to `thread::spawn` requires `move` to ensure `'static` lifetime
2. **Iterator chains** — closures in `filter` or `map` borrowing mutable state from the outer scope
3. **Callback patterns** — storing closures that capture references in struct fields

## Prevent It

- Prefer `move` closures when passing to threads or async tasks
- Clone expensive data before capturing if ownership is needed by both the closure and the outer scope
- Use `Fn`, `FnMut`, and `FnOnce` trait bounds explicitly to clarify capture requirements
