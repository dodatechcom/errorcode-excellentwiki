---
title: "[Solution] Deprecated Function Migration: str.lines() to str.split_whitespace for whitespace"
description: "Migrate from deprecated str.lines() for whitespace splitting to split_whitespace."
deprecated_function: "str.lines()"
replacement_function: "str.split_whitespace()"
languages: ["rust"]
deprecated_since: "Rust 1.0+"
---

# [Solution] Deprecated Function Migration: str.lines() to str.split_whitespace for whitespace

The `str.lines()` has been deprecated in favor of `str.split_whitespace()`.

## Migration Guide

split_whitespace handles multiple spaces.

## Before (Deprecated)

```rust
for line in text.lines() {
    // splits on \n only
}
```

## After (Modern)

```rust
for word in text.split_whitespace() {
    // splits on any whitespace
}
```

## Key Differences

- split_whitespace handles multiple spaces
