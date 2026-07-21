---
title: "[Solution] Cargo Duplicate Package -- Fix Duplicate Crate Names"
description: "Fix cargo duplicate package errors when two crates in a workspace have the same name. Rename one of them."
tools: ["cargo"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means two packages in the same workspace have the same `name` field in their `Cargo.toml`.

## Common Causes

- Copy-pasted Cargo.toml without changing the name
- Workspace members were renamed without updating metadata
- Two different crates have the same name

## How to Fix

### 1. Rename the Package

```toml
[package]
name = "my-crate-v2"  # was "my-crate"
```

### 2. Check All Member Names

```bash
grep -r "^name" */Cargo.toml
```

### 3. Use Different Crate Names

```toml
[package]
name = "my-app"     # Binary crate
name = "my-lib"     # Library crate
```

### 4. Use Path Dependencies

```toml
[dependencies]
my-lib = { path = "../my-lib" }
```

## Examples

```bash
$ cargo build
error: the package `mylib` is provided twice

# Rename one member in its Cargo.toml:
[package]
name = "mylib-core"
```
