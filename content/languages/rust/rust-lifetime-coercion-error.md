---
title: "[Solution] Rust Lifetime Coercion Error — How to Fix"
description: "Fix lifetime coercion errors. Resolve lifetime elision, outlives bounds, and inference failures."
languages: ["rust"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
comments: true
---

# Lifetime Coercion Error

Lifetime coercion errors occur when the compiler cannot automatically coerce between different lifetime parameters, typically with references, closures, or trait objects.

## Common Causes

```rust
// Lifetime mismatch in function signatures
fn first<'a>(list: &'a Vec<String>) -> &str { // Missing lifetime on return
    &list[0]
}

// Returning reference with shorter lifetime
fn create_and_return<'a>() -> &'a str {
    let local = String::from("hello");
    &local // ERROR: returning reference to local variable
}

// Closures capturing references with wrong lifetimes
fn make_closure<'a>(data: &'a str) -> Box<dyn Fn() -> &'a str + 'a> {
    Box::new(move || data) // Works, but callers may fail
}

// Trait object lifetime coercion
fn process<'a>(data: &'a dyn std::fmt::Display) -> &'a str {
    // Cannot coerce Display to str
}
```

## How to Fix

1. **Use explicit lifetime annotations**

```rust
fn first<'list>(list: &'list [String]) -> &'list str {
    &list[0]
}

fn create_owned() -> String {
    String::from("hello") // Return owned data instead of references
}
```

2. **Use `'static` for long-lived references**

```rust
fn get_static() -> &'static str {
    "hello" // String literals have 'static lifetime
}

static GLOBAL: &str = "global data";

fn get_global() -> &'static str {
    GLOBAL
}
```

3. **Return owned data instead of references**

```rust
// Instead of returning &str, return String
fn process(input: &str) -> String {
    format!("Processed: {}", input)
}

fn main() {
    let result = process("hello");
    println!("{}", result);
}
```

## Examples

```rust
use std::fmt::Display;

fn annotate<'a, T: Display>(item: &'a T) -> String {
    format!("Annotated: {}", item)
}

struct Container<'a> {
    data: &'a str,
}

impl<'a> Container<'a> {
    fn new(data: &'a str) -> Self {
        Container { data }
    }

    fn get(&self) -> &str {
        self.data
    }
}

fn main() {
    let data = String::from("hello world");
    let container = Container::new(&data);
    println!("{}", container.get());
}
```

## Related Errors

- [Lifetime Error]({{< relref "/languages/rust/lifetime-error" >}}) — lifetime issues
- [Deref Coercion Error]({{< relref "/languages/rust/rust-deref-coercion-error" >}}) — deref coercion
- [Trait Object Error]({{< relref "/languages/rust/rust-trait-object-error" >}}) — trait object issues
