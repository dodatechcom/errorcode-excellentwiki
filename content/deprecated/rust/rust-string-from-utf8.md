---
title: "[Solution] Deprecated Function Migration: String::from_utf8_unchecked to from_utf8"
description: "Migrate from deprecated from_utf8_unchecked to from_utf8."
deprecated_function: "String::from_utf8_unchecked(bytes)"
replacement_function: "String::from_utf8(bytes)"
languages: ["rust"]
deprecated_since: "Rust 1.0+"
---

# [Solution] Deprecated Function Migration: String::from_utf8_unchecked to from_utf8

The `String::from_utf8_unchecked(bytes)` has been deprecated in favor of `String::from_utf8(bytes)`.

## Migration Guide

from_utf8 is safe.

## Before (Deprecated)

```rust
let s = unsafe { String::from_utf8_unchecked(bytes) };
```

## After (Modern)

```rust
let s = String::from_utf8(bytes)?;
```

## Key Differences

- from_utf8 is safe
