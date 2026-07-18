---
title: "[Solution] Cargo Cross Compilation Target Not Found Error Fix"
description: "Fix 'cross-compilation target not found' in Cargo. Set up cross-compilation toolchains for Rust embedded and cross-platform builds."
tools: ["cargo"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
---

# Cargo Cross Compilation Target Not Found Error Fix

The `cross-compilation target not found` error occurs when Cargo cannot find the specified target or the required linker and tools for cross-compilation.

## What This Error Means

Rust supports cross-compilation to different architectures. When the target is not installed, the linker is missing, or system libraries are unavailable for the target, compilation fails.

A typical error:

```
error: linker `arm-linux-gnueabihf-gcc` not found
```

Or:

```
error[E0463]: can't find crate for `core`
```

## Why It Happens

Common causes include:

- **Target not installed** — `rustup target add` not run.
- **Linker missing** — Cross-compiler not installed on system.
- **System libraries unavailable** — Target arch libraries not installed.
- **Wrong Cargo config** — Linker not configured for target.
- **Build script issues** — build.rs cannot find target libraries.

## How to Fix It

### Fix 1: Install target

```bash
# RIGHT: Add cross-compilation target
rustup target add arm-unknown-linux-gnueabihf
rustup target add aarch64-unknown-linux-gnu
rustup target add x86_64-pc-windows-gnu

# List available targets
rustup target list
```

### Fix 2: Install cross-compiler

```bash
# RIGHT: Install cross-compiler for target
# ARM Linux
sudo apt-get install gcc-arm-linux-gnueabihf

# AArch64 Linux
sudo apt-get install gcc-aarch64-linux-gnu

# Windows (from Linux)
sudo apt-get install gcc-mingw-w64
```

### Fix 3: Configure linker in Cargo

```toml
# .cargo/config.toml
[target.arm-unknown-linux-gnueabihf]
linker = "arm-linux-gnueabihf-gcc"

[target.aarch64-unknown-linux-gnu]
linker = "aarch64-linux-gnu-gcc"
```

### Fix 4: Use cross for complex targets

```bash
# RIGHT: Use cross for easy cross-compilation
cargo install cross
cross build --target arm-unknown-linux-gnueabihf

# Cross uses Docker for clean environments
```

### Fix 5: Set environment variables

```bash
# RIGHT: Set target-specific env vars
export CC_arm_unknown_linux_gnueabihf=arm-linux-gnueabihf-gcc
export CARGO_TARGET_ARM_UNKNOWN_LINUX_GNUEABIHF_LINKER=arm-linux-gnueabihf-gcc
cargo build --target arm-unknown-linux-gnueabihf
```

## Common Mistakes

- **Forgetting `rustup target add`** — Target must be installed first.
- **Not installing system cross-compiler** — Rust target alone is not enough.
- **Using wrong linker** — Must match target architecture exactly.

## Related Pages

- [Cargo No Std Error](cargo-no-std-error) — no_std linking issues
- [Cargo Wasm Error](cargo-wasm-error) — WASM compilation issues
- [Cargo Build Script Error](cargo-build-script) — build.rs issues
