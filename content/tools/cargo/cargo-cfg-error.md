---
title: "[Solution] Cargo cfg Attribute Error — Fix Unknown cfg or Conditional Compilation Error"
description: "Fix cargo cfg attribute errors when conditional compilation checks fail. Resolve unknown cfg predicates and platform-specific compilation issues."
tools: ["cargo"]
error-types: ["compilation-error"]
severities: ["error"]
weight: 5
---

This error means a `cfg()` attribute in the source code references a condition that is not recognized by the compiler or is misspelled. The compiler warns or errors on unknown cfg predicates.

## What This Error Means

Rust uses `#[cfg(...)]` for conditional compilation. When you use an unknown or misspelled cfg key:

```
error: unexpected `cfg` condition name: `my_feature`
  --> src/lib.rs:10:7
   |
10 | #[cfg(my_feature)]
   |       ^^^^^^^^^^ help: there is an expected value with this name: `feature = "my_feature"`
```

Or a warning followed by ignored code:

```
warning: unknown `cfg` predicate: `target_os = "macosx"`
```

## Why It Happens

- A cfg attribute key is misspelled (e.g., `target_os` vs `target_os` typo)
- Using a non-standard cfg name that was never defined via `--cfg` flag
- Forgetting the `feature = "...",` syntax for Cargo features
- A build script uses `cargo:rustc-cfg=...` with an incorrect value
- The cfg key was removed or renamed in a Rust edition update

## How to Fix It

### Check Common cfg Names

```rust
// Correct
#[cfg(target_os = "linux")]
#[cfg(feature = "my-feature")]
#[cfg(debug_assertions)]
#[cfg(unix)]
#[cfg(windows)]

// Wrong
#[cfg(linux)]               // should be target_os = "linux"
#[cfg(my_feature)]          // should be feature = "my_feature"
```

### List All Defined cfg Values

```bash
rustc --print cfg
```

For a specific target:

```bash
rustc --target x86_64-unknown-linux-gnu --print cfg
```

### Define Custom cfg Values in Cargo.toml

```toml
[features]
my-feature = []

[build]
rustflags = ["--cfg", "my_custom_cfg"]
```

### Define Custom cfg in Build Scripts

```rust
// build.rs
fn main() {
    println!("cargo:rustc-cfg=my_custom_cfg");
}
```

### Check Feature Names

```toml
# Cargo.toml
[features]
default = []
my_feature = []   # <-- note underscore, not hyphen
```

When referencing it:

```rust
#[cfg(feature = "my_feature")]  // use the exact name from Cargo.toml
```

## Common Mistakes

- Using `#[cfg(target_os = "macos")]` instead of `"macos"` (correct is `"macos"`)
- Confusing `#[cfg(foo)]` with `#[cfg(feature = "foo")]` -- they are completely different
- Not running `rustc --print cfg` to verify available cfg keys
- Adding cfg checks without testing them on the intended platform

## Related Pages

- [Cargo Feature Error]({{< relref "/tools/cargo/cargo-feature-error" >}}) -- feature flag problems
- [Cargo Compilation Error]({{< relref "/tools/cargo/cargo-compilation-error" >}}) -- compilation errors
- [Cargo Dependency Error]({{< relref "/tools/cargo/cargo-dependency-error" >}}) -- dependency issues
