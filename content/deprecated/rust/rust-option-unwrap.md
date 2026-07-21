---
title: "[Solution] Deprecated Function Migration: Option::unwrap() to expect()"
description: "Migrate from deprecated Option::unwrap() to expect()."
deprecated_function: "option.unwrap()"
replacement_function: "option.expect()"
languages: ["rust"]
deprecated_since: "Rust 1.0+"
---

# [Solution] Deprecated Function Migration: Option::unwrap() to expect()

The `option.unwrap()` has been deprecated in favor of `option.expect("message")`.

## Migration Guide

expect provides better error messages.

## Before (Deprecated)

```rust
let val = some_option.unwrap();
```

## After (Modern)

```rust
let val = some_option.expect("Expected Some value");
```

## Key Differences

- expect provides better error messages
