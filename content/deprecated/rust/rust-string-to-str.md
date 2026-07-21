---
title: "[Solution] Deprecated Function Migration: manual string conversion to .into()/.as_str()"
description: "Migrate from deprecated manual String conversions to Into/AsRef traits in Rust."
deprecated_function: "String::from(s) or s.to_string()"
replacement_function: ".into() / .as_str()"
languages: ["rust"]
deprecated_since: "Rust 1.0+"
---

# [Solution] Deprecated Function Migration: manual string conversion to .into()/.as_str()

The `String::from(s) or s.to_string()` has been deprecated in favor of `.into() / .as_str()`.

## Migration Guide

Use .into() for owned conversion and .as_str() for borrowing.

## Before (Deprecated)

```rust
fn greet(name: &str) {
    let owned = String::from(name);
    let again = name.to_string();
}
```

## After (Modern)

```rust
fn greet(name: &str) {
    let owned: String = name.into();
    let again = name.to_owned();
}

fn process(input: &str) {
    let s: String = input.into();
}
```

## Key Differences

- .into() uses From/Into traits
- .to_owned() creates owned copy
- .as_str() borrows from String
- Prefer &str parameters for flexibility
