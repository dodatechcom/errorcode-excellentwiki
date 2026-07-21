---
title: "[Solution] Cargo Unresolved Import -- Fix Missing Use Statement"
description: "Fix cargo unresolved import errors when Rust cannot find the specified import path. Check module structure and dependencies."
tools: ["cargo"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means the Rust compiler cannot resolve a `use` statement or import path in your code.

## Common Causes

- The imported item does not exist in the crate
- Module path is wrong
- Missing `pub` visibility on the imported item
- The dependency is not in Cargo.toml

## How to Fix

### 1. Check the Import Path

```rust
// Instead of:
use my_crate::Foo;

// Try:
use my_crate::module::Foo;
```

### 2. Add Missing Dependency

```toml
[dependencies]
my_crate = "1.0"
```

### 3. Check Module Structure

```rust
// lib.rs
pub mod module;

// module.rs
pub struct Foo;
```

### 4. Use Extern Crate (Legacy)

```rust
extern crate my_crate;
use my_crate::Foo;
```

## Examples

```bash
$ cargo build
error[E0432]: unresolved import `my_crate::Foo`

# Fix the import path:
use my_crate::module::Foo;
```
