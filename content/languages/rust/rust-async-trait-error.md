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

Async trait errors occur when using `async fn` in trait definitions or when using the `async-trait` crate incorrectly. Common issues include lifetime problems, Send/Sync bounds, and object safety violations.

## Common Causes

```rust
// Object safety: async fn in trait is not object-safe (pre-1.75)
trait DynAsync { async fn run(&self); } // Not object-safe

// Missing Send bound — cannot spawn on tokio runtime
trait MyService { async fn handle(&self, req: String) -> String; }

#[tokio::main]
async fn main() {
    let service = MyServiceImpl;
    tokio::spawn(service.handle("hello".into())); // ERROR: !Send
}

// Lifetime issues with async trait returning borrowed data
trait Parser {
    async fn parse<'a>(&'a self, input: &'a str) -> &'a str; // Higher-ranked lifetime issues
}
```

## How to Fix

1. **Use Rust 1.75+ native async fn in trait**

```rust
trait Service: Send + Sync {
    async fn execute(&self, input: &str) -> String;
}

struct MyService;
impl Service for MyService {
    async fn execute(&self, input: &str) -> String {
        format!("Processed: {}", input)
    }
}
```

2. **Add `Send` bound for multi-threaded runtimes**

```rust
trait Service: Send + Sync {
    async fn execute(&self, input: &str) -> String;
}

struct MyService;
impl Service for MyService {
    async fn execute(&self, input: &str) -> String { format!("OK: {}", input) }
}

#[tokio::main]
async fn main() {
    let svc = MyService;
    tokio::spawn(async move {
        println!("{}", svc.execute("data").await);
    }).await.unwrap();
}
```

3. **Use `Pin<Box<dyn Future>>` for trait objects**

```rust
use std::future::Future;
use std::pin::Pin;

trait DynService: Send + Sync {
    fn execute(&self, input: String) -> Pin<Box<dyn Future<Output = String> + Send + '_>>;
}

struct MyService;
impl DynService for MyService {
    fn execute(&self, input: String) -> Pin<Box<dyn Future<Output = String> + Send + '_>> {
        Box::pin(async move { format!("Processed: {}", input) })
    }
}
```

## Examples

```rust
trait Repository: Send + Sync {
    async fn find(&self, id: u64) -> Option<String>;
    async fn save(&self, id: u64, data: &str) -> Result<(), String>;
}

struct PostgresRepo;
impl Repository for PostgresRepo {
    async fn find(&self, id: u64) -> Option<String> { Some(format!("Record {}", id)) }
    async fn save(&self, id: u64, data: &str) -> Result<(), String> {
        println!("Saving {} -> {}", id, data);
        Ok(())
    }
}

#[tokio::main]
async fn main() {
    let repo = PostgresRepo;
    if let Some(r) = repo.find(42).await { println!("Found: {}", r); }
    repo.save(42, "hello").await.unwrap();
}
```

## Related Errors

- [Future Error]({{< relref "/languages/rust/rust-future-error" >}}) — future/poll issues
- [Pin Error]({{< relref "/languages/rust/rust-pin-error" >}}) — pinning issues
- [Tokio Runtime Error]({{< relref "/languages/rust/rust-tokio-runtime-error" >}}) — runtime config
