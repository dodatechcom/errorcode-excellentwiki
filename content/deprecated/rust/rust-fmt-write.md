---
title: "[Solution] Deprecated Function Migration: write! to writeln!"
description: "Migrate from deprecated write! with newline to writeln!."
deprecated_function: "write!()"
replacement_function: "writeln!()"
languages: ["rust"]
deprecated_since: "Rust 1.0+"
---

# [Solution] Deprecated Function Migration: write! to writeln!

The `write!(stdout, "{}\n", msg)` has been deprecated in favor of `writeln!(stdout, "{}", msg)`.

## Migration Guide

writeln! adds newline automatically

write! requires manual newline.

## Before (Deprecated)

```rust
use std::io::Write;
write!(handle, "{}\n", msg);
```

## After (Modern)

```rust
use std::io::Write;
writeln!(handle, "{}", msg);
```

## Key Differences

- writeln! adds newline automatically
- write! for no newline
