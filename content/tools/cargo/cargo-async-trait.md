---
title: "[Solution] Cargo Async Trait Not Object Safe Error Fix"
description: "Fix 'async trait not object safe' errors in Cargo. Resolve object safety and dynamic dispatch issues with async traits in Rust."
tools: ["cargo"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
---

# Cargo Async Trait Not Object Safe Error Fix

The async trait not object safe error occurs when trying to use dynamic dispatch (trait objects) with async traits, which are not object-safe by default in Rust.

## What This Error Means

Rust traits with async methods cannot be used as trait objects (dyn Trait) because async methods return opaque futures that are not object-safe. This prevents using Box<dyn MyTrait> with async methods.

A typical error:

```
error[E0038]: the trait `MyTrait` cannot be made into an object
```

## Why It Happens

Common causes include:

- **Async methods in trait** — async fn makes trait not object-safe.
- **Generic methods** — Generics prevent object safety.
- **Return impl Trait** — Opaque return types are not object-safe.
- **Missing async-trait crate** — Need crate for async trait objects.

## How to Fix It

### Fix 1: Use async-trait crate

```toml
# Cargo.toml
[dependencies]
async-trait = "0.1"
```

```rust
use async_trait::async_trait;

#[async_trait]
trait MyTrait {
    async fn do_something(&self) -> String;
}

struct MyStruct;

#[async_trait]
impl MyTrait for MyStruct {
    async fn do_something(&self) -> String {
        "Hello".to_string()
    }
}

// Now works with trait objects
async fn use_trait(obj: Box<dyn MyTrait>) {
    println!("{}", obj.do_something().await);
}
```

### Fix 2: Use generics instead of trait objects

```rust
// RIGHT: Static dispatch with generics
fn process<T: MyTrait>(obj: &T) {
    // Compile-time dispatch, no object safety needed
}
```

### Fix 3: Use enum dispatch

```rust
// RIGHT: Enum-based dispatch
enum MyEnum {
    VariantA(StructA),
    VariantB(StructB),
}

impl MyEnum {
    async fn do_something(&self) -> String {
        match self {
            MyEnum::VariantA(s) => s.do_something().await,
            MyEnum::VariantB(s) => s.do_something().await,
        }
    }
}
```

### Fix 4: Manual boxing of futures

```rust
use std::pin::Pin;
use std::future::Future;

trait MyTrait {
    fn do_something(&self) -> Pin<Box<dyn Future<Output = String> + Send + '_>>;
}
```

## Common Mistakes

- **Forgetting async-trait crate** — Required for dyn Trait with async.
- **Not using Box::pin for manual approach** — Futures must be pinned.
- **Assuming all async traits need object safety** — Use generics when possible.

## Related Pages

- [Cargo Tokio Error](cargo-tokio-error) — Tokio runtime issues
- [Cargo Lifetime Error](cargo-lifetime-error) — Lifetime issues
- [Cargo Unsafe Error](cargo-unsafe-error) — unsafe block issues
