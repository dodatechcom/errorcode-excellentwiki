---
title: "[Solution] Rust Async Trait Error — How to Fix"
description: "Fix Rust async trait errors. Resolve issues with async functions in traits, dyn dispatch, and the async-trait crate for trait objects."
languages: ["rust"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
comments: true
---

# Async Trait Error

Async functions in traits require special handling in Rust because the compiler desugars async fn into a generic Future, making trait objects impossible without boxing.

## Why It Happens

- Async functions in traits are not directly supported with dyn dispatch
- The `async_trait` macro is not applied to the trait definition
- Return types involve lifetimes that conflict with async desugaring
- `Pin<Box<dyn Future>>` lifetime bounds are incorrect

## Common Error Messages

- `async fn in traits is not object-safe`
- `cannot be sent between threads safely`
- `the trait Send cannot be made into an object`
- `lifetime mismatch in async trait return type`

## How to Fix It

### Fix 1: Use the async-trait crate

```rust
use async_trait::async_trait;

#[async_trait]
trait Database {
    async fn get(&self, key: &str) -> Option<String>;
}

struct MemDb;

#[async_trait]
impl Database for MemDb {
    async fn get(&self, key: &str) -> Option<String> {
        Some(format!("value for {}", key))
    }
}
```

### Fix 2: Use return-position impl Trait in traits (Rust 1.75+)

```rust
trait Database {
    fn get(&self, key: &str) -> impl std::future::Future<Output = Option<String>> + Send;
}
```

### Fix 3: Manually box the future

```rust
use std::future::Future;
use std::pin::Pin;

trait Database {
    fn get(&self, key: &str) -> Pin<Box<dyn Future<Output = Option<String>> + Send + '_>>;
}
```

## Common Scenarios

1. A service trait used across async boundaries
2. Dynamic dispatch with async trait methods
3. Returning different async futures from trait implementations

## Prevent It

- Enable the `async-trait` feature in your Cargo.toml for trait objects
- Consider RPITIT (Rust 1.75+) for concrete type async traits
- Always add Send + 'static bounds when using async traits with spawn
