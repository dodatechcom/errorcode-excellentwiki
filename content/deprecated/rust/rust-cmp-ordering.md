---
title: "[Solution] Deprecated Function Migration: manual comparison to cmp()"
description: "Migrate from deprecated manual comparison to cmp()."
deprecated_function: "if a < b { Ordering::Less }"
replacement_function: "a.cmp(&b)"
languages: ["rust"]
deprecated_since: "Rust 1.0+"
---

# [Solution] Deprecated Function Migration: manual comparison to cmp()

The `if a < b { Ordering::Less }` has been deprecated in favor of `a.cmp(&b)`.

## Migration Guide

cmp is more idiomatic.

## Before (Deprecated)

```rust
if a < b {
    return Ordering::Less;
} else if a > b {
    return Ordering::Greater;
}
return Ordering::Equal;
```

## After (Modern)

```rust
a.cmp(&b)
```

## Key Differences

- cmp is more idiomatic
