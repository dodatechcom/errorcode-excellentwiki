---
title: "[Solution] Cargo Clippy Error — Fix Clippy Lint Denied Warnings"
description: "Fix cargo clippy lint errors when the build treats clippy warnings as errors. Configure clippy levels, suppress false positives, and maintain code quality."
tools: ["cargo"]
error-types: ["lint-error"]
severities: ["warning"]
weight: 5
---

This error means clippy found a lint violation that is configured as an error. Clippy either ran with `clippy::pedantic` or the project has `deny(clippy::...)` attributes.

## What This Error Means

Clippy is Rust's official linter. When it finds issues:

```
error: unreadable literal
  --> src/main.rs:5:21
   |
5  |     let x = 1000000;
   |             ^^^^^^^ help: use `1_000_000` instead
   |
   = note: `-D clippy::unreadable-literal` implied by `-D clippy::all`
```

Or when CI rejects clippy warnings:

```
error: could not compile `my-crate` due to previous error
warning: clippy::some-lint triggered but not denied by project settings
```

## Why It Happens

- The project or CI sets `#![deny(clippy::all)]` or `#![deny(warnings)]`
- A new clippy lint was added in a newer Rust version that triggers on existing code
- Code that was acceptable when written now triggers a lint after a clippy update
- The `.cargo/config.toml` has `rustflags = ["-D", "clippy::all"]`
- A specific lint was manually denied with `#[deny(clippy::lint_name)]`

## How to Fix It

### Run Clippy and See All Issues

```bash
cargo clippy
cargo clippy --all-targets --all-features
```

### Fix Specific Lint Violations

```rust
// Before
let x = 1000000;

// After
let x = 1_000_000;
```

### Allow a Lint at the Crate Level

```rust
// lib.rs or main.rs
#![allow(clippy::unreadable_literal)]
```

### Allow a Lint on a Specific Item

```rust
#[allow(clippy::too_many_arguments)]
fn my_function(a: i32, b: i32, c: i32, d: i32, e: i32, f: i32) {}
```

### Configure Clippy in Cargo.toml

```toml
[lints.clippy]
unreadable_literal = "allow"
too_many_arguments = "allow"
```

### Run Clippy with Warnings Instead of Deny

```bash
# Override deny to warn
cargo clippy -- -W clippy::all
```

### Set Clippy Level per Workspace

```toml
# Cargo.toml at workspace root
[workspace.lints.clippy]
all = "warn"
pedantic = "deny"
```

## Common Mistakes

- Adding `#![deny(warnings)]` to crates without pinning Rust/clippy versions
- Allowing lints globally instead of fixing the underlying code
- Not running clippy in CI to catch new lint violations before merging
- Ignoring clippy::pedantic lints until they become deny by default in a new Rust version

## Related Pages

- [Cargo Compilation Error]({{< relref "/tools/cargo/cargo-compilation-error" >}}) -- compilation failures
- [Cargo Feature Error]({{< relref "/tools/cargo/cargo-feature-error" >}}) -- feature flag issues
- [Cargo cfg Error]({{< relref "/tools/cargo/cargo-cfg-error" >}}) -- conditional compilation
