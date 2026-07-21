---
title: "[Solution] Deprecated Function Migration: external mutability to RefCell"
description: "Migrate from deprecated patterns to RefCell for interior mutability."
deprecated_function: "let mut x = val"
replacement_function: "RefCell::new(val)"
languages: ["rust"]
deprecated_since: "Rust 1.0+"
---

# [Solution] Deprecated Function Migration: external mutability to RefCell

The `let mut x = val` has been deprecated in favor of `RefCell::new(val)`.

## Migration Guide

RefCell provides runtime borrow checking

Sometimes you need mutable access through shared reference.

## Before (Deprecated)

```rust
struct Node {
    data: i32,
    children: Vec<Node>,
}
```

## After (Modern)

```rust
use std::cell::RefCell;
use std::rc::Rc;
struct Node {
    data: i32,
    children: RefCell<Vec<Rc<Node>>>,
}
```

## Key Differences

- RefCell for interior mutability
- Rc for shared ownership
- Runtime borrow checking
