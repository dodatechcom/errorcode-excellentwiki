---
title: "[Solution] Deprecated Function Migration: #![feature()] to stable alternatives"
description: "Migrate from deprecated unstable feature gates to stable Rust APIs."
deprecated_function: "#![feature(name)]"
replacement_function: "Stable API alternatives"
languages: ["rust"]
deprecated_since: "Varies"
---

# [Solution] Deprecated Function Migration: #![feature()] to stable alternatives

The `#![feature(name)]` has been deprecated in favor of `Stable API alternatives`.

## Migration Guide

Feature gates enable unstable APIs. Always use stable APIs for production code.

## Before (Deprecated)

```rust
#![feature(box_syntax)]
#![feature(step_by)]

fn main() {
    let _boxed = box 42;
    let _iter = (0..10).step_by(2);
}
```

## After (Modern)

```rust
fn main() {
    let _boxed = Box::new(42);
    let _iter = (0..10).step_by(2);
}
```

## Key Differences

- box_syntax -> Box::new
- step_by -> Iterator::step_by (stable 1.28+)
- Never ship code with feature gates
