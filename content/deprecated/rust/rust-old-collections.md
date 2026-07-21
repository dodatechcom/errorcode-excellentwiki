---
title: "[Solution] Deprecated Function Migration: std::collections::hash_map::Entry to entry API"
description: "Migrate from deprecated manual HashMap patterns to entry API in Rust."
deprecated_function: "Manual HashMap insert/check"
replacement_function: "HashMap::entry().or_insert()"
languages: ["rust"]
deprecated_since: "Rust 1.0+"
---

# [Solution] Deprecated Function Migration: std::collections::hash_map::Entry to entry API

The `Manual HashMap insert/check` has been deprecated in favor of `HashMap::entry().or_insert()`.

## Migration Guide

The entry API provides atomic check-and-insert operations without double lookup.

## Before (Deprecated)

```rust
let mut counts = HashMap::new();
for word in words {
    if counts.contains_key(word) {
        *counts.get_mut(word).unwrap() += 1;
    } else {
        counts.insert(word.to_string(), 1);
    }
}
```

## After (Modern)

```rust
let mut counts = HashMap::new();
for word in words {
    *counts.entry(word.to_string()).or_insert(0) += 1;
}

// or_default for Default-constructible types
*counts.entry(word.to_string()).or_default() += 1;
```

## Key Differences

- entry API is atomic (no double lookup)
- or_insert for specific default
- or_default for Default::default()
- or_insert_with for lazy computation
