---
title: "[Solution] Cargo Add Already Dep -- Fix Duplicate Dependency"
description: "Fix cargo add already dep errors when adding a dependency that already exists in Cargo.toml. Update the existing entry instead."
tools: ["cargo"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means you tried to add a dependency that is already listed in `Cargo.toml`. cargo refuses to add a duplicate entry.

## Common Causes

- You forgot the dependency was already added
- The dependency was added under a different name
- A workspace member already defines it

## How to Fix

### 1. Update Existing Dependency

```bash
cargo update <package>
```

### 2. Check Cargo.toml

```toml
[dependencies]
serde = "1.0"
# Don't add serde again
```

### 3. Add Different Version

```bash
cargo add serde@1.0.185
```

### 4. Use --dry-run

```bash
cargo add <package> --dry-run
```

## Examples

```bash
$ cargo add serde
warning: package `serde` is already in Cargo.toml

$ cargo update serde
    Updating crates.io index
```
