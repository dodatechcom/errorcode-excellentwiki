---
title: "[Solution] Rust Cfg Error — How to Fix"
description: "Fix cfg attribute and cfg! macro errors. Resolve conditional compilation, feature detection, and target configuration."
languages: ["rust"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
comments: true
---

# Cfg Error

Cfg errors occur when using `#[cfg(...)]` conditional compilation attributes incorrectly, with invalid conditions, missing features, or mismatched target specifications.

## Common Causes

```rust
// Typo in cfg condition
#[cfg(linix)]  // ERROR: should be "linux"
fn init() {}

// Missing feature flag
#[cfg(feature = "advanced")]
fn advanced_feature() {} // Fails if "advanced" feature not enabled

// Invalid target_arch value
#[cfg(target_arch = "x86-64")]  // ERROR: should be "x86_64"
fn specific() {}

// Conflicting cfg attributes
#[cfg(target_os = "linux")]
fn linux_fn() {}

#[cfg(target_os = "windows")]
fn windows_fn() {}

// Trying to use cfg! in const context (limited in older Rust)
```

## How to Fix

1. **Use correct cfg condition names**

```rust
// Correct target_os values: linux, windows, macos, freebsd, etc.
#[cfg(target_os = "linux")]
fn linux_only() {}

#[cfg(target_arch = "x86_64")]
fn x86_specific() {}

#[cfg(target_arch = "aarch64")]
fn arm_specific() {}
```

2. **Declare features in Cargo.toml and use consistent names**

```toml
[features]
default = ["basic"]
basic = []
advanced = []
unstable = ["dep:nightly-only-crate"]
```

```rust
#[cfg(feature = "basic")]
fn basic_feature() { println!("Basic mode"); }

#[cfg(feature = "advanced")]
fn advanced_feature() { println!("Advanced mode"); }

#[cfg(not(feature = "advanced"))]
fn fallback() { println!("Fallback mode"); }
```

3. **Use `cfg_if` crate for complex conditional compilation**

```rust
cfg_if::cfg_if! {
    if #[cfg(target_os = "linux")] {
        fn get_os() -> &'static str { "Linux" }
    } else if #[cfg(target_os = "macos")] {
        fn get_os() -> &'static str { "macOS" }
    } else if #[cfg(target_os = "windows")] {
        fn get_os() -> &'static str { "Windows" }
    } else {
        fn get_os() -> &'static str { "Unknown" }
    }
}
```

## Examples

```rust
// Conditional compilation in practice
#[cfg(target_pointer_width = "64")]
type PlatformPtr = u64;

#[cfg(target_pointer_width = "32")]
type PlatformPtr = u32;

// Testing cfg
#[cfg(test)]
mod tests {
    #[test]
    fn it_works() { assert_eq!(2 + 2, 4); }
}

// Feature-gated modules
#[cfg(feature = "json")]
pub mod json_support {
    pub fn parse_json(input: &str) -> serde_json::Value {
        serde_json::from_str(input).unwrap()
    }
}
```

```bash
# Build with specific features
$ cargo build --features "advanced,unstable"
$ cargo build --no-default-features
$ cargo build --target x86_64-unknown-linux-gnu
```

## Related Errors

- [Feature Gate Error]({{< relref "/languages/rust/rust-feature-gate-error" >}}) — feature gate issues
- [Const Fn Error]({{< relref "/languages/rust/rust-const-fn-error" >}}) — const fn limitations
- [Embedded Error]({{< relref "/languages/rust/rust-embedded-error" >}}) — cross-compilation issues
