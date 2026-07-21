---
title: "[Solution] Deprecated Function Migration: .clone() on iterators to .copied()"
description: "Migrate from deprecated .clone() to .copied() for Copy types."
deprecated_function: "iter.clone()"
replacement_function: "iter.copied()"
languages: ["rust"]
deprecated_since: "Rust 1.35+"
---

# [Solution] Deprecated Function Migration: .clone() on iterators to .copied()

The `iter.clone()` has been deprecated in favor of `iter.copied()`.

## Migration Guide

copied() is more explicit for Copy types

.clone() works but .copied() is more explicit.

## Before (Deprecated)

```rust
let v = vec![1, 2, 3];
let cloned: Vec<i32> = v.iter().cloned().collect();
```

## After (Modern)

```rust
let v = vec![1, 2, 3];
let copied: Vec<i32> = v.iter().copied().collect();
```

## Key Differences

- .copied() for Copy types
- .cloned() for Clone types
