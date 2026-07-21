---
title: "[Result] Deprecated Function Migration: Result::unwrap() to expect() or ? operator"
description: "Migrate from deprecated Result::unwrap() to expect() or ? operator."
deprecated_function: "result.unwrap()"
replacement_function: "result.expect()"
languages: ["rust"]
deprecated_since: "Rust 1.0+"
---

# [Result] Deprecated Function Migration: Result::unwrap() to expect() or ? operator

The `result.unwrap()` has been deprecated in favor of `result.expect("message")`.

## Migration Guide

expect/? are safer than unwrap.

## Before (Deprecated)

```rust
let val = result.unwrap();
```

## After (Modern)

```rust
let val = result.expect("Operation failed");
let val = result?;
```

## Key Differences

- expect/? are safer than unwrap
