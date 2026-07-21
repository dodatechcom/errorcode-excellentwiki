---
title: "[Solution] Cargo Publish Failed -- Fix crates.io Upload Error"
description: "Fix cargo publish failed errors when uploading a crate to crates.io fails. Check crate metadata and authentication."
tools: ["cargo"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means `cargo publish` failed to upload your crate to crates.io.

## Common Causes

- The crate version already exists on crates.io
- Authentication token is invalid
- Crate metadata is invalid
- The crate exceeds the size limit

## How to Fix

### 1. Check Version

```bash
cargo publish --dry-run
```

### 2. Bump Version

```bash
cargo edit --version 1.0.1
```

### 3. Verify Metadata

```toml
[package]
name = "my-crate"
version = "1.0.1"
description = "A description"
license = "MIT"
```

### 4. Login and Publish

```bash
cargo login <token>
cargo publish
```

## Examples

```bash
$ cargo publish
error: crate version 1.0.0 already exists

$ cargo edit --version 1.0.1
$ cargo publish
   Packaging my-crate v1.0.1
   Uploading my-crate v1.0.1
```
