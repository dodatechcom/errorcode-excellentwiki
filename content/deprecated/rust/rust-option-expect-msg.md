---
title: "[Solution] Deprecated Function Migration: expect with string to unwrap_or_else"
description: "Migrate from deprecated expect with complex message to unwrap_or_else."
deprecated_function: "option.expect()"
replacement_function: "option.unwrap_or_else()"
languages: ["rust"]
deprecated_since: "Rust 1.0+"
---

# [Solution] Deprecated Function Migration: expect with string to unwrap_or_else

The `option.expect("message")` has been deprecated in favor of `option.unwrap_or_else(|| panic!("message"))`.

## Migration Guide

unwrap_or_else is lazy.

## Before (Deprecated)

```rust
let val = option.expect("value must exist");
```

## After (Modern)

```rust
let val = option.unwrap_or_else(|| {
    panic!("value must exist")
});
```

## Key Differences

- unwrap_or_else is lazy
