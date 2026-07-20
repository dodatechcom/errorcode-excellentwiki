---
title: "[Solution] Rust No Std Error — How to Fix"
description: "Fix no_std errors. Resolve missing standard library, allocator, and platform-specific issues."
languages: ["rust"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
comments: true
---

# No Std Error

No_std errors occur when developing for `#![no_std]` environments — missing allocator, unavailable standard library features, and incompatible crate dependencies.

## Common Causes

```rust
#![no_std]

// Using std types in no_std
use std::collections::HashMap; // ERROR: std not available

// Using println! without a logging backend
println!("Hello"); // ERROR: no stdio in no_std

// Crate requires std feature
use serde::Serialize; // May need std feature disabled

// Missing global allocator
// #[global_allocator] not defined
```

## How to Fix

1. **Use no_std-compatible alternatives**

```rust
#![no_std]
#![no_main]

extern crate alloc;
use alloc::vec::Vec;
use alloc::string::String;
use alloc::collections::BTreeMap; // BTreeMap works in no_std

// Use defmt or log for logging in embedded
use defmt::println;

#[cortex_m_rt::entry]
fn main() -> ! {
    let mut map = BTreeMap::new();
    map.insert(1, "one");
    defmt::println!("Map has {} entries", map.len());
    loop { cortex_m::asm::wfi(); }
}
```

2. **Use `#![no_std]` with `extern crate alloc` for heap allocations**

```rust
#![no_std]
#![no_main]

extern crate alloc;
use alloc::vec::Vec;

#[global_allocator]
static ALLOC: wee_alloc::WeeAlloc = wee_alloc::WeeAlloc::INIT;

#[cortex_m_rt::entry]
fn main() -> ! {
    let mut v: Vec<i32> = Vec::new();
    v.push(1);
    v.push(2);
    loop { cortex_m::asm::wfi(); }
}
```

3. **Use `default-features = false` for std-dependent crates**

```toml
[dependencies]
serde = { version = "1.0", default-features = false, features = ["derive"] }
```

```rust
#![no_std]

use serde::{Serialize, Deserialize};

#[derive(Serialize, Deserialize)]
struct Config { name: [u8; 32] }
```

## Examples

```rust
#![no_std]
#![no_main]

extern crate alloc;
use alloc::vec::Vec;
use alloc::string::String;

use cortex_m_rt::entry;
use panic_halt as _;

#[entry]
fn main() -> ! {
    let numbers: Vec<i32> = (0..10).collect();
    let sum: i32 = numbers.iter().sum();

    // Use a logging framework for no_std output
    defmt::println!("Sum: {}", sum);

    loop { cortex_m::asm::wfi(); }
}
```

## Related Errors

- [Embedded Error]({{< relref "/languages/rust/rust-embedded-error" >}}) — embedded targets
- [ESP-IDF Error]({{< relref "/languages/rust/rust-esp-idf-error" >}}) — ESP-IDF
- [Heapless Error]({{< relref "/languages/rust/rust-heapless-error" >}}) — stack allocations
