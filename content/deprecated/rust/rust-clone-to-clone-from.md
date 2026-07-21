---
title: "[Solution] Deprecated Function Migration: dst = src.clone() to dst.clone_from(&src)"
description: "Migrate from deprecated clone assignment to clone_from."
deprecated_function: "dst = src.clone()"
replacement_function: "dst.clone_from(&src)"
languages: ["rust"]
deprecated_since: "Rust 1.0+"
---

# [Solution] Deprecated Function Migration: dst = src.clone() to dst.clone_from(&src)

The `dst = src.clone()` has been deprecated in favor of `dst.clone_from(&src)`.

## Migration Guide

clone_from can reuse allocations.

## Before (Deprecated)

```rust
let mut a = String::from("hello");
a = b.clone();
```

## After (Modern)

```rust
let mut a = String::from("hello");
a.clone_from(&b);
```

## Key Differences

- clone_from can reuse allocations
