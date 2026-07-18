---
title: "[Solution] Rust Phantom Data Error — How to Fix"
description: "Fix Rust PhantomData errors. Learn how to use PhantomData correctly for variance, drop check, and marker types in generics."
languages: ["rust"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
comments: true
---

# Phantom Data Error

PhantomData errors occur when you use `PhantomData<T>` incorrectly, typically when the compiler needs phantom type parameters for variance or drop checking but the implementation is incomplete.

## Why It Happens

- A generic type parameter is not used in any field but is not marked with `PhantomData`
- `PhantomData` is used with a type that does not need to be inferred
- The marker type conflicts with the actual usage of the generic parameter
- Drop checking requires phantom ownership but it is missing

## Common Error Messages

- `parameter `T` is never used`
- `struct has unused type parameter `T``
- `PhantomData` type mismatch in generic context
- `cannot move out of `PhantomData` value`

## How to Fix It

### Fix 1: Add PhantomData for unused type parameters

```rust
use std::marker::PhantomData;

struct Id<T> {
    value: u64,
    _marker: PhantomData<T>,
}

impl<T> Id<T> {
    fn new(value: u64) -> Self {
        Id { value, _marker: PhantomData }
    }
}

fn main() {
    let user_id: Id<String> = Id::new(42);
    let _ = user_id;
}
```

### Fix 2: Use PhantomData for variance control

```rust
use std::marker::PhantomData;

struct Covariant<'a, T: 'a> {
    data: &'a T,
    _marker: PhantomData<T>,
}
```

### Fix 3: Use PhantomData for drop checking

```rust
use std::marker::PhantomData;

struct IntrusiveList<T> {
    next: *mut IntrusiveList<T>,
    _marker: PhantomData<T>,
}
```

## Common Scenarios

1. **Generic newtypes** — wrapper types with unused type parameters
2. **FFI bindings** — opaque pointers that need type safety without storage
3. **Variance control** — explicitly marking covariant or contravariant relationships

## Prevent It

- Always pair `PhantomData<T>` with a `T` that is either used or explicitly documented as unused
- Use `PhantomData<*const T>` for invariance when needed
- Document the reason for phantom type parameters with comments
