---
title: "[Solution] Deprecated Function Migration: manual HashMap insert/check to entry API"
description: "Migrate from deprecated manual HashMap patterns to entry API."
deprecated_function: "if !map.contains_key(k) { map.insert(k, v); }"
replacement_function: "map.entry(k).or_insert(v)"
languages: ["rust"]
deprecated_since: "Rust 1.0+"
---

# [Solution] Deprecated Function Migration: manual HashMap insert/check to entry API

The `if !map.contains_key(k) { map.insert(k, v); }` has been deprecated in favor of `map.entry(k).or_insert(v)`.

## Migration Guide

entry API is atomic and avoids double lookup

Manual contains_key + insert is not atomic.

## Before (Deprecated)

```rust
let mut map = HashMap::new();
if !map.contains_key("key") {
    map.insert("key".to_string(), value);
}
```

## After (Modern)

```rust
let mut map = HashMap::new();
map.entry("key".to_string()).or_insert(value);
```

## Key Differences

- entry API is atomic
- or_insert for specific default
- Avoids double lookup
