---
title: "[Solution] Deprecated Function Migration: format! macro to println! inline"
description: "Migrate from deprecated format! to direct println! with format strings."
deprecated_function: "let s = format!();"
replacement_function: "println!();"
languages: ["rust"]
deprecated_since: "Rust 1.0+"
---

# [Solution] Deprecated Function Migration: format! macro to println! inline

The `let s = format!("{}", x);` has been deprecated in favor of `println!("{}", x);`.

## Migration Guide

Direct println! avoids unnecessary string allocation

format! creates a String. println! writes directly to stdout without allocation.

## Before (Deprecated)

```rust
let msg = format!("Hello, {}!", name);
println!("{}", msg);  // extra allocation
```

## After (Modern)

```rust
println!("Hello, {}!", name);  // direct output

// Or for dynamic strings
let msg = format!("Hello, {}!", name);  // still needed sometimes
```

## Key Differences

- println! writes directly to stdout
- format! allocates a String
- Use format! when you need the String
- Use println! for direct output
