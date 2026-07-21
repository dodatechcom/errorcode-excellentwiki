---
title: "[Solution] Deprecated Function Migration: .parse().expect() to .parse().unwrap_or_else"
description: "Migrate from deprecated .parse().expect() to .parse().unwrap_or_else()."
deprecated_function: "s.parse()"
replacement_function: "s.parse().unwrap_or_else(|_| default)"
languages: ["rust"]
deprecated_since: "Rust 1.0+"
---

# [Solution] Deprecated Function Migration: .parse().expect() to .parse().unwrap_or_else

The `s.parse().expect("invalid")` has been deprecated in favor of `s.parse().unwrap_or_else(|_| default)`.

## Migration Guide

unwrap_or_else is lazy.

## Before (Deprecated)

```rust
let n: i32 = s.parse().expect("invalid number");
```

## After (Modern)

```rust
let n: i32 = s.parse().unwrap_or_else(|_| {
    eprintln!("invalid number: {s}");
    0
});
```

## Key Differences

- unwrap_or_else is lazy
