---
title: "[Solution] Deprecated Function Migration: .parse().unwrap() to proper error handling"
description: "Migrate from deprecated .parse().unwrap() to proper error handling."
deprecated_function: "s.parse().unwrap()"
replacement_function: "s.parse()?"
languages: ["rust"]
deprecated_since: "Rust 1.0+"
---

# [Solution] Deprecated Function Migration: .parse().unwrap() to proper error handling

The `s.parse().unwrap()` has been deprecated in favor of `s.parse()?`.

## Migration Guide

unwrap panics on invalid input.

## Before (Deprecated)

```rust
let n: i32 = "42".parse().unwrap();
```

## After (Modern)

```rust
let n: i32 = "42".parse()?;

let n = "42".parse().unwrap_or(0);
```

## Key Differences

- parse() returns Result
