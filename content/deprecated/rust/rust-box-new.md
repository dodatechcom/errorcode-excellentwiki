---
title: "[Solution] Deprecated Function Migration: Box::new() to Box::pin()"
description: "Migrate from deprecated Box::new() for pinning to Box::pin()."
deprecated_function: "Box::new(value)"
replacement_function: "Box::pin(value)"
languages: ["rust"]
deprecated_since: "Rust 1.0+"
---

# [Solution] Deprecated Function Migration: Box::new() to Box::pin()

The `Box::new(value)` has been deprecated in favor of `Box::pin(value)`.

## Migration Guide

Box::pin creates pinned heap allocation.

## Before (Deprecated)

```rust
let pinned = Box::new(value);
```

## After (Modern)

```rust
let pinned = Box::pin(value);
```

## Key Differences

- Box::pin creates pinned allocation
