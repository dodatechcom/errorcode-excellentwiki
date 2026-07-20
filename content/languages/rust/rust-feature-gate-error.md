---
title: "[Solution] Rust Feature Gate Error — How to Fix"
description: "Fix feature gate errors. Resolve unstable feature usage, feature flags, and compiler version issues."
languages: ["rust"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
comments: true
---

# Feature Gate Error

Feature gate errors occur when using nightly-only features without enabling the corresponding feature gate, or when features are incorrectly declared in `Cargo.toml`.

## Common Causes

```rust
// Using nightly feature without enabling it
#![feature(once_cell)] // ERROR: requires nightly toolchain

// Feature not declared in Cargo.toml
#[cfg(feature = "advanced")]
fn advanced() {} // Fails if "advanced" not in [features]

// Feature name mismatch between Cargo.toml and code
// Cargo.toml: my-feature = []
#[cfg(feature = "my_feature")] // Wrong name: should be "my-feature"
fn my_feature() {}

// Feature dependency cycle
[features]
a = ["b"]
b = ["a"]  // Circular dependency
```

## How to Fix

1. **Declare features properly in Cargo.toml**

```toml
[features]
default = ["basic"]
basic = []
advanced = ["dep:serde"]
unstable = ["tokio/unstable"]

[dependencies]
serde = { version = "1.0", optional = true }
tokio = { version = "1", features = ["rt"] }
```

2. **Use `cfg` correctly with the exact feature name**

```rust
#[cfg(feature = "basic")]
fn basic_feature() { println!("Basic mode"); }

#[cfg(feature = "advanced")]
fn advanced_feature() { println!("Advanced mode"); }

#[cfg(not(feature = "advanced"))]
fn fallback() { println!("Using fallback"); }
```

3. **Use nightly toolchain only when needed**

```rust
// Switch to nightly for unstable features
// $ rustup override set nightly
// $ rustup override unset  # Revert to stable

// Conditional compilation for nightly features
#![cfg_attr(feature = "nightly", feature(specialization))]
```

## Examples

```bash
# Build with specific features
$ cargo build --features "advanced"
$ cargo build --no-default-features
$ cargo build --all-features

# Test with specific features
$ cargo test --features "advanced"
```

```toml
# Cargo.toml
[features]
default = ["json"]
json = ["dep:serde_json"]
xml = ["dep:quick-xml"]
full = ["json", "xml"]
```

```rust
#[cfg(feature = "json")]
pub fn parse_json(input: &str) -> serde_json::Value {
    serde_json::from_str(input).unwrap()
}

#[cfg(feature = "xml")]
pub fn parse_xml(input: &str) -> quick_xml::events::BytesStart {
    let mut reader = quick_xml::Reader::from_str(input);
    reader.read_event().unwrap().unwrap()
}
```

## Related Errors

- [Cfg Error]({{< relref "/languages/rust/rust-cfg-error" >}}) — conditional compilation
- [Cargo Workspace Error]({{< relref "/languages/rust/rust-cargo-workspace-error" >}}) — workspace features
- [Cargo Publish Error]({{< relref "/languages/rust/rust-cargo-publish-error" >}}) — publishing features
