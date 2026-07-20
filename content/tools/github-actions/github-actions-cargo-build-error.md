---
title: "[Solution] GitHub Actions Cargo Build Error"
description: "Fix GitHub Actions cargo build failures in Rust workflow."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Cargo build errors occur during Rust compilation in the workflow:

```
error[E0433]: failed to resolve: use of undeclared crate or module
```

## Common Causes

- Missing Rust toolchain setup.
- Dependencies not downloaded.
- Missing system libraries for native crates.

## How to Fix

**Set up Rust properly:**

```yaml
steps:
  - uses: actions/checkout@v4
  - uses: dtolnay/rust-toolchain@stable
  - uses: Swatinem/rust-cache@v2
  - run: cargo build --release
```

## Examples

```yaml
steps:
  - uses: actions/checkout@v4
  - uses: dtolnay/rust-toolchain@stable
    with:
      components: clippy, rustfmt
  - uses: Swatinem/rust-cache@v2
  - run: cargo clippy -- -D warnings
```
