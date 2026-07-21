---
title: "[Solution] Deprecated Function Migration: manual Clone impl to derive macro"
description: "Migrate from deprecated manual Clone to derive."
deprecated_function: "impl Clone for T { }"
replacement_function: "#[derive(Clone)]"
languages: ["rust"]
deprecated_since: "Rust 1.0+"
---

# [Solution] Deprecated Function Migration: manual Clone impl to derive macro

The `impl Clone for T { }` has been deprecated in favor of `#[derive(Clone)]`.

## Migration Guide

derive macro auto-generates implementation

Manual Clone implementations are error-prone.

## Before (Deprecated)

```rust
impl Clone for MyStruct {
    fn clone(&self) -> Self {
        MyStruct { data: self.data.clone() }
    }
}
```

## After (Modern)

```rust
#[derive(Clone, Debug)]
struct MyStruct {
    data: Vec<i32>,
}
```

## Key Differences

- derive auto-generates Clone
- Less boilerplate
- Less error-prone
