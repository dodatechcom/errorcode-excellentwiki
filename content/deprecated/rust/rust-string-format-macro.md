---
title: "[Solution] Deprecated Function Migration: format! macro to string interpolation"
description: "Migrate from deprecated format! macro to string interpolation."
deprecated_function: "format!()"
replacement_function: "format!()"
languages: ["rust"]
deprecated_since: "Rust 1.58+"
---

# [Solution] Deprecated Function Migration: format! macro to string interpolation

The `format!("{} is {}", name, age)` has been deprecated in favor of `format!("{name} is {age}")`.

## Migration Guide

String interpolation is more readable.

## Before (Deprecated)

```rust
let s = format!("{} is {}", name, age);
```

## After (Modern)

```rust
let s = format!("{name} is {age}");
```

## Key Differences

- String interpolation is more readable
