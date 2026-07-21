---
title: "[Solution] Deprecated Function Migration: str.as_bytes() to .as_ref()"
description: "Migrate from deprecated .as_bytes() to .as_ref() for byte conversion."
deprecated_function: "str.as_bytes()"
replacement_function: "str.as_ref()"
languages: ["rust"]
deprecated_since: "Rust 1.0+"
---

# [Solution] Deprecated Function Migration: str.as_bytes() to .as_ref()

The `str.as_bytes()` has been deprecated in favor of `str.as_ref()`.

## Migration Guide

as_ref() is more idiomatic.

## Before (Deprecated)

```rust
let bytes: &[u8] = s.as_bytes();
```

## After (Modern)

```rust
let bytes: &[u8] = s.as_ref();
```

## Key Differences

- as_ref() is more idiomatic
