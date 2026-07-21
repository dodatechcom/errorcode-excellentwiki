---
title: "[Solution] Deprecated Function Migration: Vec::new() with push to vec! macro"
description: "Migrate from deprecated Vec::new() + push to vec! macro."
deprecated_function: "let mut v = Vec::new(); v.push(x);"
replacement_function: "let v = vec![x];"
languages: ["rust"]
deprecated_since: "Rust 1.0+"
---

# [Solution] Deprecated Function Migration: Vec::new() with push to vec! macro

The `let mut v = Vec::new(); v.push(x);` has been deprecated in favor of `let v = vec![x];`.

## Migration Guide

vec! macro is more concise.

## Before (Deprecated)

```rust
let mut v = Vec::new();
v.push(1);
v.push(2);
v.push(3);
```

## After (Modern)

```rust
let v = vec![1, 2, 3];
```

## Key Differences

- vec! macro is concise
