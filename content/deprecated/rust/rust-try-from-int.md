---
title: "[Solution] Deprecated Function Migration: as casts to TryFrom"
description: "Migrate from deprecated as casts to TryFrom for integer conversion."
deprecated_function: "as i32 / as u32"
replacement_function: "i32::try_from(val)"
languages: ["rust"]
deprecated_since: "Rust 1.34+"
---

# [Solution] Deprecated Function Migration: as casts to TryFrom

The `as i32 / as u32` has been deprecated in favor of `i32::try_from(val)`.

## Migration Guide

TryFrom prevents silent truncation

As casts silently truncate.

## Before (Deprecated)

```rust
let big: i64 = 1000000;
let small = big as i32;  // truncation!
```

## After (Modern)

```rust
let big: i64 = 1000000;
let small = i32::try_from(big)?;
```

## Key Differences

- TryFrom returns Result
- No silent truncation
