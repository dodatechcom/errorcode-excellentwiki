---
title: "[Solution] Rust Phantom Data Error — How to Fix"
description: "Fix Rust PhantomData errors. Learn how to use PhantomData correctly for variance, drop check, and marker types in generics."
languages: ["rust"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
comments: true
---

# PhantomData Error

PhantomData errors occur when using `PhantomData` incorrectly — type marker misuse, variance violations, or missing drop semantics.

## Common Causes

```rust
use std::marker::PhantomData;

// PhantomData without clear purpose
struct Container<T> {
    data: Vec<T>,
    _marker: PhantomData<T>, // Unnecessary — Vec<T> already owns T
}

// Variance issues with PhantomData
struct Covariant<'a, T> {
    _marker: PhantomData<&'a T>, // Covariant in 'a and T
}

// Using wrong PhantomData for variance
struct Invariant<'a, T> {
    _marker: PhantomData<fn(&'a T) -> &'a T>, // Should use fn(*const T) for invariance
}
```

## How to Fix

1. **Use PhantomData only when needed for ownership or lifetime tracking**

```rust
use std::marker::PhantomData;

// PhantomData needed when type isn't stored but needs to be "used"
struct TypedId<T> {
    id: u64,
    _marker: PhantomData<T>,
}

struct User;
struct Post;

let user_id: TypedId<User> = TypedId { id: 1, _marker: PhantomData };
let post_id: TypedId<Post> = TypedId { id: 1, _marker: PhantomData };
// user_id and post_id cannot be mixed up
```

2. **Use PhantomData for variance control**

```rust
use std::marker::PhantomData;

// Covariant in T
struct Covariant<T> { _marker: PhantomData<T> }

// Contravariant in T
struct Contravariant<T> { _marker: PhantomData<fn(T)> }

// Invariant in T
struct Invariant<T> { _marker: PhantomData<fn(T) -> T> }

// Covariant in 'a
struct Borrowed<'a, T> { data: &'a T, _marker: PhantomData<&'a T> }
```

3. **Use PhantomData for drop check**

```rust
use std::marker::PhantomData;

struct Inspector<T> {
    data: Vec<T>,
    _marker: PhantomData<T>, // Ensures T is checked for drop even if not stored directly
}

impl<T> Drop for Inspector<T> {
    fn drop(&mut self) {
        println!("Inspector dropping {} items", self.data.len());
    }
}
```

## Examples

```rust
use std::marker::PhantomData;

// Type-safe ID system
struct UserId;
struct PostId;

struct Id<T> {
    value: u64,
    _marker: PhantomData<T>,
}

impl<T> Id<T> {
    fn new(value: u64) -> Self { Id { value, _marker: PhantomData } }
}

fn get_user(id: Id<UserId>) -> String { format!("User {}", id.value) }
fn get_post(id: Id<PostId>) -> String { format!("Post {}", id.value) }

fn main() {
    let user_id: Id<UserId> = Id::new(42);
    let post_id: Id<PostId> = Id::new(100);

    println!("{}", get_user(user_id));
    println!("{}", get_post(post_id));
    // get_user(post_id); // Compile error — type safety!
}
```

## Related Errors

- [Generics Error]({{< relref "/languages/rust/rust-generics-error-rs" >}}) — generic types
- [Variance Error]({{< relref "/languages/rust/rust-variance-error-rs" >}}) — variance
- [Const Generics Error]({{< relref "/languages/rust/rust-const-generics-error" >}}) — const generics
