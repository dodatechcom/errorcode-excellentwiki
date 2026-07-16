---
title: "[Solution] Rust Missing Field — Struct Initialization Error"
description: "Fix Rust missing field in struct. Learn why all struct fields must be initialized and how to use Default, Option, or update syntax."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
tags: ["struct", "field", "initialization", "default", "missing"]
weight: 5
---

# Missing Field — Struct Initialization Error

A compiler error with the message "missing field `X` in struct" occurs when you create a struct without initializing all required fields.

## Description

Rust requires every field in a struct to be explicitly set during creation. There are no implicit default values. This compile-time check prevents accidentally forgetting critical configuration or data fields. You can work around this with `Default`, struct update syntax, or by making fields optional with `Option<T>`.

Common scenarios:

- **Forgetting a field** — new struct with many fields.
- **Partial initialization** — want defaults for some fields.
- **Conditional construction** — different fields set in different branches.
- **Struct update syntax** — copying from another struct.

## Common Causes

```rust
struct Config {
    host: String,
    port: u16,
    debug: bool,
}

// Cause 1: Forgetting a field
let config = Config {
    host: String::from("localhost"),
    port: 8080,
    // Error: missing field `debug`
};

// Cause 2: Partial struct update without Default
let default = Config {
    host: String::from("0.0.0.0"),
    port: 80,
    debug: false,
};
let config = Config {
    port: 9000,
    ..default // host and debug taken from default, but host was moved
};

// Cause 3: Conditional branches with missing fields
let debug = true;
let config = Config {
    host: String::from("localhost"),
    port: 8080,
    // Error: missing `debug` in some paths
};
```

## Solutions

### Fix 1: Provide all fields

```rust
let config = Config {
    host: String::from("localhost"),
    port: 8080,
    debug: true,
};
```

### Fix 2: Implement Default

```rust
#[derive(Default)]
struct Config {
    host: String,
    port: u16,
    debug: bool,
}

fn main() {
    let config = Config {
        host: String::from("localhost"),
        ..Default::default()
    };
    println!("{}:{} debug={}", config.host, config.port, config.debug);
}
```

### Fix 3: Use Option for truly optional fields

```rust
struct Config {
    host: String,
    port: u16,
    log_file: Option<String>,
}

fn main() {
    let config = Config {
        host: String::from("localhost"),
        port: 8080,
        log_file: None,
    };
}
```

### Fix 4: Use a builder pattern

```rust
struct Config {
    host: String,
    port: u16,
    debug: bool,
}

struct ConfigBuilder {
    host: String,
    port: u16,
    debug: bool,
}

impl ConfigBuilder {
    fn new() -> Self {
        ConfigBuilder {
            host: String::from("localhost"),
            port: 8080,
            debug: false,
        }
    }
    fn host(mut self, host: &str) -> Self { self.host = host.to_string(); self }
    fn port(mut self, port: u16) -> Self { self.port = port; self }
    fn debug(mut self, debug: bool) -> Self { self.debug = debug; self }
    fn build(self) -> Config {
        Config { host: self.host, port: self.port, debug: self.debug }
    }
}

fn main() {
    let config = ConfigBuilder::new().port(9000).debug(true).build();
    println!("{}:{} debug={}", config.host, config.port, config.debug);
}
```

## Examples

```rust
struct User {
    name: String,
    email: String,
    age: u32,
}

fn main() {
    let user = User {
        name: String::from("Alice"),
        email: String::from("alice@example.com"),
    };
}
```

Output:
```
error[E0063]: missing field `age` in initializer of `User`
```

## Related Errors

- [Type Mismatch]({{< relref "/languages/rust/type-mismatch-2" >}}) — wrong type in field assignment.
- [Variant Not Found]({{< relref "/languages/rust/variant-not-found-2" >}}) — wrong enum variant.
- [Unwrap None]({{< relref "/languages/rust/unwrap-none-2" >}}) — accessing an optional field that is None.
