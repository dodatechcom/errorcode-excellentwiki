---
title: "[Solution] Cargo Missing Feature -- Fix Feature Flag Not Enabled"
description: "Fix cargo missing feature errors when using a crate feature that is not enabled in Cargo.toml. Enable the feature flag."
tools: ["cargo"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means you are trying to use a feature of a crate that is not enabled in your dependency configuration.

## Common Causes

- The feature requires explicit enablement in Cargo.toml
- Feature name is misspelled
- Feature was removed in newer version
- Conditional compilation hides the feature

## How to Fix

### 1. Enable the Feature

```toml
[dependencies]
tokio = { version = "1", features = ["full"] }
```

### 2. Check Available Features

```bash
cargo metadata --format-version 1 | jq '.packages[] | select(.name == "tokio") | .features'
```

### 3. Use --features Flag

```bash
cargo build --features "tokio/full"
```

### 4. Enable Multiple Features

```toml
[dependencies]
serde = { version = "1", features = ["derive", "rc"] }
```

## Examples

```bash
$ cargo build
error[E0432]: unresolved import `tokio::fs`

$ cargo add tokio --features full
$ cargo build
```
