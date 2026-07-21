---
title: "[Solution] Deprecated Function Migration: unwrap() to unwrap_or_else for lazy evaluation"
description: "Migrate from deprecated unwrap() to unwrap_or_else for lazy default computation."
deprecated_function: "unwrap()"
replacement_function: "unwrap_or_else(|| ...)"
languages: ["rust"]
deprecated_since: "Rust 1.0+"
---

# [Solution] Deprecated Function Migration: unwrap() to unwrap_or_else for lazy evaluation

The `unwrap()` has been deprecated in favor of `unwrap_or_else(|| ...)`.

## Migration Guide

unwrap_or_else computes defaults lazily

unwrap() panics on None/Err. unwrap_or_else computes the default lazily only when needed.

## Before (Deprecated)

```rust
let value = optional_value.unwrap();  // panics if None
let config = config_result.unwrap();  // panics if Err
```

## After (Modern)

```rust
let value = optional_value.unwrap_or_else(|| {
    log::warn!("Using default value");
    default_value
});

let config = config_result.unwrap_or_else(|e| {
    eprintln!("Config error: {}", e);
    Config::default()
});
```

## Key Differences

- unwrap_or_else computes default lazily
- unwrap() panics immediately
- Better error context with logging
- Use unwrap for prototyping only
