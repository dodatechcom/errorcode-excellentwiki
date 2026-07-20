---
title: "[Solution] Rust Deref Coercion Error — How to Fix"
description: "Fix Rust deref coercion errors. Understand Deref trait implementation issues, automatic dereferencing failures, and smart pointer coercion."
languages: ["rust"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
comments: true
---

# Deref Coercion Error

Deref coercion errors occur when Rust's automatic deref coercion fails — typically when the compiler cannot infer which deref path to take, or when custom `Deref` implementations conflict.

## Common Causes

```rust
use std::ops::Deref;

// Ambiguous deref — multiple Deref paths
struct MyString(String);
struct Wrapper(MyString);

impl Deref for MyString {
    type Target = str;
    fn deref(&self) -> &str { &self.0 }
}

impl Deref for Wrapper {
    type Target = MyString;
    fn deref(&self) -> &MyString { &self.0 }
}

// Deref into a type that doesn't implement the needed trait
fn takes_str(s: &str) {}
let my = MyString(String::from("hello"));
takes_str(&my); // Works via Deref

// Infinite deref chain
struct A(B);
struct B(A);
impl Deref for A { type Target = B; fn deref(&self) -> &B { &self.0 } }
impl Deref for B { type Target = A; fn deref(&self) -> &A { &self.0 } }
```

## How to Fix

1. **Implement Deref targeting str or [T] for custom string/slice types**

```rust
use std::ops::Deref;

struct SmartString { data: Vec<u8> }

impl Deref for SmartString {
    type Target = str;
    fn deref(&self) -> &str {
        std::str::from_utf8(&self.data).unwrap()
    }
}

fn main() {
    let s = SmartString { data: b"hello".to_vec() };
    println!("Length: {}", s.len()); // Deref to str, then len()
    println!("Uppercase: {}", s.to_uppercase());
}
```

2. **Avoid infinite deref cycles**

```rust
struct Wrapper(String);

impl std::ops::Deref for Wrapper {
    type Target = str;
    fn deref(&self) -> &str { &self.0 }
}

// This works: deref to str, then call str methods
let w = Wrapper("hello".to_string());
assert_eq!(w.len(), 5);
assert!(w.starts_with("hel"));
```

3. **Use explicit method calls when deref is ambiguous**

```rust
struct Container(Vec<i32>);

impl std::ops::Deref for Container {
    type Target = Vec<i32>;
    fn deref(&self) -> &Vec<i32> { &self.0 }
}

let c = Container(vec![1, 2, 3]);

// Explicit calls avoid ambiguity
let len = (*c).len(); // or c.len() which works via deref
let first = (*c).first(); // explicit
```

## Examples

```rust
use std::ops::Deref;

struct UniquePtr<T> { value: Box<T> }

impl<T> UniquePtr<T> {
    fn new(value: T) -> Self { UniquePtr { value: Box::new(value) } }
}

impl<T> Deref for UniquePtr<T> {
    type Target = T;
    fn deref(&self) -> &T { &self.value }
}

fn main() {
    let name = UniquePtr::new(String::from("Rust"));
    // Deref to String, then to str
    println!("Length: {}", name.len());
    println!("Contains 'u': {}", name.contains('u'));
}
```

## Related Errors

- [Deref Coercion Error]({{< relref "/languages/rust/rust-deref-coercion-error" >}}) — deref coercion issues
- [Trait Object Error]({{< relref "/languages/rust/rust-trait-object-error" >}}) — trait object issues
- [Box Error]({{< relref "/languages/rust/rust-box-error" >}}) — smart pointer issues
