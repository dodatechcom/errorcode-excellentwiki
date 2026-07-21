---
title: "[Solution] Cargo Workspace Conflict -- Fix Workspace Dependency Issues"
description: "Fix cargo workspace conflict errors when workspace members have conflicting dependency versions. Unify versions in workspace."
tools: ["cargo"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means workspace members have incompatible version requirements for the same dependency.

## Common Causes

- Different workspace members pin different versions of the same crate
- Feature flags conflict between members
- Platform-specific dependencies clash

## How to Fix

### 1. Use Workspace Dependencies

```toml
# Cargo.toml (workspace root)
[workspace.dependencies]
serde = { version = "1.0", features = ["derive"] }

# Member Cargo.toml
[dependencies]
serde.workspace = true
```

### 2. Update All Members

```bash
cargo update --workspace
```

### 3. Check Dependency Tree

```bash
cargo tree --workspace
```

### 4. Pin Shared Version

```bash
cargo add serde@1.0.193 --workspace
```

## Examples

```bash
$ cargo check --workspace
error: package `serde v1.0.152` cannot be used because it depends on `serde_derive v1.0.152`
  which cannot coexist with `serde_derive v1.0.193`

# Fix: use workspace dependency
[workspace.dependencies]
serde = "1.0.193"
```
