---
title: "[Solution] Deprecated Function Migration: error_chain! to thiserror/anyhow"
description: "Migrate from deprecated error_chain! macro to thiserror/anyhow."
deprecated_function: "error_chain! { }"
replacement_function: "thiserror::Error / anyhow::Error"
languages: ["rust"]
deprecated_since: "Rust 2018+"
---

# [Solution] Deprecated Function Migration: error_chain! to thiserror/anyhow

The `error_chain! { }` has been deprecated in favor of `thiserror::Error / anyhow::Error`.

## Migration Guide

thiserror and anyhow are more ergonomic

error_chain! was the standard before 2018.

## Before (Deprecated)

```rust
error_chain! {
    errors {
        NotFound(msg: String) {
            description("not found")
        }
    }
}
```

## After (Modern)

```rust
use thiserror::Error;

#[derive(Error, Debug)]
enum MyError {
    #[error("not found: {0}")]
    NotFound(String),
}
```

## Key Differences

- thiserror for library error types
- anyhow for application error handling
