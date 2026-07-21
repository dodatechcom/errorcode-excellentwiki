---
title: "[Solution] Deprecated Function Migration: try!() macro to ? operator"
description: "Migrate from deprecated try!() macro to the ? operator in Rust."
deprecated_function: "try!(expr)"
replacement_function: "expr?"
languages: ["rust"]
deprecated_since: "Rust 1.13+"
---

# [Solution] Deprecated Function Migration: try!() macro to ? operator

The `try!(expr)` has been deprecated in favor of `expr?`.

## Migration Guide

The try!() macro was deprecated in favor of the ? operator which is syntactically cleaner.

## Before (Deprecated)

```rust
use std::fs::File;
use std::io::{self, Read};

fn read_file() -> io::Result<String> {
    let mut file = try!(File::open("data.txt"));
    let mut contents = String::new();
    try!(file.read_to_string(&mut contents));
    Ok(contents)
}
```

## After (Modern)

```rust
use std::fs::File;
use std::io::{self, Read};

fn read_file() -> io::Result<String> {
    let mut file = File::open("data.txt")?;
    let mut contents = String::new();
    file.read_to_string(&mut contents)?;
    Ok(contents)
}
```

## Key Differences

- Replace try!(expr) with expr?
- ? works in functions returning Result or Option
- Can chain multiple ? operators
