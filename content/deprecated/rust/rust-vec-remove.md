---
title: "[Solution] Deprecated Function Migration: Vec::remove to retain or drain"
description: "Migrate from deprecated Vec::remove for filtering to retain."
deprecated_function: "vec.remove(index)"
replacement_function: "vec.retain(|x| *x != value)"
languages: ["rust"]
deprecated_since: "Rust 1.0+"
---

# [Solution] Deprecated Function Migration: Vec::remove to retain or drain

The `vec.remove(index)` has been deprecated in favor of `vec.retain(|x| *x != value)`.

## Migration Guide

retain filters in place.

## Before (Deprecated)

```rust
vec.retain(|&x| x != value);
```

## After (Modern)

```rust
vec.retain(|x| *x != value);
```

## Key Differences

- retain filters in place
