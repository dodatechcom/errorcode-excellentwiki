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

Closure borrow errors occur when a closure captures a variable by reference while the variable is already mutably borrowed, or when the closure outlives the borrowed data.

## Common Causes

```rust
// Mutable and immutable borrow in same scope
let mut v = vec![1, 2, 3];
let closure = || println!("{:?}", v); // immutable borrow
v.push(4); // ERROR: cannot borrow `v` as mutable because it is also borrowed by closure
drop(closure);

// Closure captures by move but data is borrowed
let mut s = String::from("hello");
let append = || s.push_str(" world");
let r = &s; // immutable borrow
append(); // ERROR: cannot borrow `s` as mutable
println!("{}", r);

// Moving a borrowed value into a closure
let list = vec![1, 2, 3];
let r = &list;
let closure = move || println!("{:?}", r); // moves the reference, which may outlive data
```

## How to Fix

1. **Complete borrows before using closures**

```rust
let mut v = vec![1, 2, 3];
let closure = || println!("{:?}", v);
closure(); // Use closure first
v.push(4); // Then mutate
```

2. **Clone data if closure needs to outlive the borrow**

```rust
let data = vec![1, 2, 3];
let data_clone = data.clone();
std::thread::spawn(move || {
    println!("Thread: {:?}", data_clone);
});
println!("Main: {:?}", data);
```

3. **Use `Fn`, `FnMut`, or `FnOnce` appropriately**

```rust
// Fn — closure captures by shared reference
let x = 10;
let add = |y| x + y;
println!("{}", add(5)); // 15

// FnMut — closure captures by mutable reference
let mut count = 0;
let mut increment = || { count += 1; count };
println!("{}", increment()); // 1
println!("{}", increment()); // 2

// FnOnce — closure takes ownership
let name = String::from("Rust");
let greet = move || format!("Hello, {}!", name);
println!("{}", greet());
// name is no longer accessible
```

## Examples

```rust
fn main() {
    let mut names = vec!["Alice", "Bob", "Charlie"];

    // Collect first, then iterate
    let upper: Vec<String> = names.iter().map(|n| n.to_uppercase()).collect();
    println!("Upper: {:?}", upper);

    // Use the original after closure usage
    names.push("Diana");
    println!("Names: {:?}", names);

    // Thread-safe closure with explicit clones
    let data = std::sync::Arc::new(vec![1, 2, 3]);
    let data_clone = std::sync::Arc::clone(&data);
    std::thread::spawn(move || {
        println!("Thread sees: {:?}", data_clone);
    }).join().unwrap();
    println!("Main sees: {:?}", data);
}
```

## Related Errors

- [Closure Borrow Error]({{< relref "/languages/rust/rust-closure-borrow-error" >}}) — closure borrowing
- [Lifetime Error]({{< relref "/languages/rust/lifetime-error" >}}) — lifetime issues
- [Mutex Error]({{< relref "/languages/rust/rust-mutex-error" >}}) — concurrent access
