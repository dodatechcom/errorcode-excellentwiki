---
title: "[Solution] Rust Cargo Workspace Error — How to Fix"
description: "Fix Cargo workspace errors. Resolve workspace configuration, dependency resolution, and member issues."
languages: ["rust"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
comments: true
---

# Cargo Workspace Error

Cargo workspace errors occur when configuring or building multi-crate workspaces. Issues include circular dependencies, inconsistent versions, and incorrect path specifications.

## Common Causes

```toml
# Circular dependency between workspace members
[workspace]
members = ["crate-a", "crate-b"]
# crate-a depends on crate-b, crate-b depends on crate-a — ERROR

# Missing resolver for edition 2021
[workspace]
members = ["crate-a", "crate-b"]
# Missing: resolver = "2"

# Path to member doesn't exist
[workspace]
members = ["crates/my-crate"]  # ERROR: directory not found
```

## How to Fix

1. **Use `workspace.dependencies` for centralized version management**

```toml
# Root Cargo.toml
[workspace]
members = ["crates/*"]
resolver = "2"

[workspace.dependencies]
serde = { version = "1.0", features = ["derive"] }
tokio = { version = "1", features = ["full"] }

# In member Cargo.toml
[dependencies]
serde = { workspace = true }
tokio = { workspace = true }
```

2. **Avoid circular dependencies by extracting shared code**

```toml
# Create a shared crate
[workspace]
members = ["crates/core", "crates/api", "crates/shared"]

# crates/core/Cargo.toml
[dependencies]
shared = { path = "../shared" }  # Shared depends on nothing

# crates/api/Cargo.toml
[dependencies]
core = { path = "../core" }
```

3. **Use proper path specifications**

```toml
[workspace]
members = [
    "crates/my-crate",
    "apps/my-app",
    "libs/my-lib",
]
exclude = ["old-crates"]
```

## Examples

```toml
# Complete workspace Cargo.toml
[workspace]
members = ["crates/*"]
resolver = "2"

[workspace.dependencies]
serde = { version = "1.0", features = ["derive"] }
tokio = { version = "1", features = ["full"] }
thiserror = "1.0"

[workspace.package]
edition = "2021"
license = "MIT"
```

```bash
# Build all workspace members
$ cargo build --workspace

# Test all members
$ cargo test --workspace

# Build specific member
$ cargo build -p my-crate
```

## Related Errors

- [Cargo Audit Error]({{< relref "/languages/rust/rust-cargo-audit-error" >}}) — security vulnerabilities
- [Cargo Publish Error]({{< relref "/languages/rust/rust-cargo-publish-error" >}}) — publishing failures
- [Cargo Vendor Error]({{< relref "/languages/rust/rust-cargo-vendor-error" >}}) — vendoring issues
