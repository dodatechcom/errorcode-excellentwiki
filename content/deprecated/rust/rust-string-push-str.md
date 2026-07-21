---
title: "[Solution] Deprecated Function Migration: String::push_str to format!"
description: "Migrate from deprecated String::push_str for complex building to format!."
deprecated_function: "s.push_str();"
replacement_function: "s = format!()"
languages: ["rust"]
deprecated_since: "Rust 1.0+"
---

# [Solution] Deprecated Function Migration: String::push_str to format!

The `s.push_str("hello"); s.push_str(" world");` has been deprecated in favor of `s = format!("{s} hello world")`.

## Migration Guide

format! is more readable.

## Before (Deprecated)

```rust
let mut s = String::new();
s.push_str("hello");
s.push_str(" world");
```

## After (Modern)

```rust
let s = format!("hello world");
```

## Key Differences

- format! is more readable
