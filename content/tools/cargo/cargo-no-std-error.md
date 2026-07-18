---
title: "[Solution] Cargo No Std Crate Linking Error Fix"
description: "Fix 'no_std crate linking error' in Cargo. Resolve no_std compilation issues and embedded Rust linking problems."
tools: ["cargo"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
---

# Cargo No Std Crate Linking Error Fix

The `no_std crate linking error` occurs when a no_std Rust crate fails to link due to missing allocator, wrong target, or incompatible dependencies.

## What This Error Means

`no_std` crates do not use the standard library, targeting embedded or bare-metal environments. When linking fails, it is usually because the allocator is not defined or the target lacks required features.

A typical error:

```
error[E0152]: duplicate lang item in crate `alloc`
```

Or:

```
error: `#[global_allocator]` requires `alloc` crate
```

## Why It Happens

Common causes include:

- **Missing allocator** — no_std requires custom allocator.
- **Wrong target** — Target does not support no_std.
- **Dependency uses std** — One dependency requires std.
- **Duplicate lang items** — Multiple allocators defined.
- **Missing panic handler** — no_std needs custom panic handler.
- **Feature flags wrong** — Dependencies not configured for no_std.

## How to Fix It

### Fix 1: Define allocator

```rust
// RIGHT: Custom allocator for no_std
#![no_std]
#![no_main]

use core::panic::PanicInfo;

#[panic_handler]
fn panic(_info: &PanicInfo) -> ! {
    loop {}
}

// Use a custom allocator if needed
extern crate alloc;
```

### Fix 2: Use correct target

```bash
# RIGHT: Use no_std compatible target
rustup target add thumbv7em-none-eabihf
cargo build --target thumbv7em-none-eabihf

# Or x86_64 target
rustup target add x86_64-unknown-none
cargo build --target x86_64-unknown-none
```

### Fix 3: Configure dependencies for no_std

```toml
# Cargo.toml
[dependencies]
my-crate = { version = "1.0", default-features = false }

# Enable only no_std-compatible features
[dependencies.my-crate]
version = "1.0"
default-features = false
features = ["no_std"]
```

### Fix 4: Check for std dependencies

```bash
# RIGHT: Find std dependencies
cargo tree -e features

# Check if any dependency requires std
cargo tree | grep std
```

### Fix 5: Use no_std-compatible crates

```rust
// RIGHT: Common no_std crates
// Use these instead of std equivalents:
// - `heapless` instead of `Vec`
// - `nb` for non-blocking I/O
// - `embedded-hal` for hardware abstraction
```

## Common Mistakes

- **Forgetting `#![no_std]`** — Must be at crate root.
- **Using std crates without `default-features = false`** — Disable std features.
- **Not providing panic handler** — Required for no_std binaries.

## Related Pages

- [Cargo Build Script Error](cargo-build-script) — build.rs issues
- [Cargo Cross Compile Error](cargo-cross-compile) — Cross-compilation issues
- [Cargo Unsafe Error](cargo-unsafe-error) — unsafe block issues
