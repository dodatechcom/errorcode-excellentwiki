---
title: "[Solution] Rust Variance Error — How to Fix"
description: "Fix variance errors in generic types. Resolve covariance, contravariance, and invariance mismatches."
languages: ["rust"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
comments: true
---

# Variance Error

Variance errors occur when type parameters have incorrect variance (covariant, contravariant, invariant) — causing type mismatches in function signatures or trait implementations.

## Common Causes

```rust
// Invariant when covariance is expected
use std::cell::Cell;

struct MyType<'a, T> {
    data: &'a T,
    cell: Cell<&'a T>, // Cell makes it invariant in T
}

// Contravariance issues with function pointers
fn process(f: fn(i32) -> i32) -> i32 { f(42) }
// fn(i32) -> i32 is contravariant in i32 (but i32 is concrete, so no issue)

// Lifetime variance confusion
struct Ref<'a> { data: &'a str }
// Ref<'a> is covariant in 'a — can coerce &'long str to Ref<'long>
```

## How to Fix

1. **Understand variance rules**

```rust
// Covariant: Can use &'long for &'short (longer lives are subtypes)
// &T is covariant in T

// Contravariant: fn(T) reverses variance
// fn(T) is contravariant in T

// Invariant: Cell<&T> makes T invariant
// Cannot coerce between lifetimes

struct Covariant<'a, T> {
    data: &'a T, // Covariant in both 'a and T
}

struct InvariantCell<T> {
    cell: Cell<T>, // Cell makes T invariant
}
```

2. **Use the correct wrapper for desired variance**

```rust
use std::marker::PhantomData;

// Covariant in T
struct Covariant<T> { _marker: PhantomData<T> }

// Contravariant in T
struct Contravariant<T> { _marker: PhantomData<fn(T)> }

// Invariant in T
struct Invariant<T> { _marker: PhantomData<fn(T) -> T> }
```

3. **Use `*const T` for invariance when needed**

```rust
use std::marker::PhantomData;

// Invariant in T
struct MyPtr<T> {
    ptr: *const T,
    _marker: PhantomData<fn(T) -> T>, // Makes T invariant
}
```

## Examples

```rust
use std::marker::PhantomData;

struct Covariant<'a, T> {
    data: &'a T,
    _marker: PhantomData<&'a T>,
}

struct Invariant<'a, T> {
    cell: std::cell::Cell<&'a T>,
}

fn main() {
    // Covariant: can coerce to longer lifetime
    let long-lived = String::from("hello");
    let cov: Covariant<'_, str> = Covariant {
        data: &long_live,
        _marker: PhantomData,
    };

    println!("Covariant data: {}", cov.data);
}
```

## Related Errors

- [Lifetime Error]({{< relref "/languages/rust/lifetime-error" >}}) — lifetime issues
- [Generics Error]({{< relref "/languages/rust/rust-generics-error-rs" >}}) — generics
- [Phantom Data Error]({{< relref "/languages/rust/rust-phantom-data-error" >}}) — PhantomData
