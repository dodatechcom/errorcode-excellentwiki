---
title: "[Solution] Deprecated Function Migration: Vec::with_capacity + push to vec![; n]"
description: "Migrate from deprecated Vec::with_capacity to vec![; n]."
deprecated_function: "Vec::with_capacity(n)"
replacement_function: "vec![x; n]"
languages: ["rust"]
deprecated_since: "Rust 1.0+"
---

# [Solution] Deprecated Function Migration: Vec::with_capacity + push to vec![; n]

The `Vec::with_capacity(n)` has been deprecated in favor of `vec![x; n]`.

## Migration Guide

vec![; n] is more concise.

## Before (Deprecated)

```rust
let mut v = Vec::with_capacity(10);
for i in 0..10 {
    v.push(i);
}
```

## After (Modern)

```rust
let v = vec![0; 10];
```

## Key Differences

- vec![; n] is concise
