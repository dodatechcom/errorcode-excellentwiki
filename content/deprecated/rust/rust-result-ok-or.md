---
title: "[Solution] Deprecated Function Migration: match on Option to ok_or/ok_or_else"
description: "Migrate from verbose Option matching to ok_or."
deprecated_function: "match opt { Some(v) => ..., None => ... }"
replacement_function: "opt.ok_or(err)"
languages: ["rust"]
deprecated_since: "Rust 1.0+"
---

# [Solution] Deprecated Function Migration: match on Option to ok_or/ok_or_else

The `match opt { Some(v) => ..., None => ... }` has been deprecated in favor of `opt.ok_or(err)`.

## Migration Guide

ok_or converts Option to Result

ok_or converts Option<T> to Result<T, E>.

## Before (Deprecated)

```rust
let value = match optional_value {
    Some(v) => v,
    None => return Err(MyError::NotFound),
};
```

## After (Modern)

```rust
let value = optional_value
    .ok_or(MyError::NotFound)?;
```

## Key Differences

- ok_or for simple error conversion
- ok_or_else for lazy error computation
