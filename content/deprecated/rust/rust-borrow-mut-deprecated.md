---
title: "[Solution] Deprecated Function Migration: &mut to cow for read-only mutations"
description: "Migrate from deprecated &mut patterns to Cow for conditional mutation."
deprecated_function: "let mut s = String::from();"
replacement_function: "Cow::from(x) or Cow::Borrowed"
languages: ["rust"]
deprecated_since: "Rust 1.0+"
---

# [Solution] Deprecated Function Migration: &mut to cow for read-only mutations

The `let mut s = String::from(x); s.push_str(" suffix");` has been deprecated in favor of `Cow::from(x) or Cow::Borrowed`.

## Migration Guide

Cow avoids unnecessary allocation.

## Before (Deprecated)

```rust
let mut s = String::from(input);
if needs_modification {
    s.push_str(" modified");
}
```

## After (Modern)

```rust
let s = if needs_modification {
    Cow::Owned(format!("{input} modified"))
} else {
    Cow::Borrowed(input)
};
```

## Key Differences

- Cow avoids unnecessary allocation
