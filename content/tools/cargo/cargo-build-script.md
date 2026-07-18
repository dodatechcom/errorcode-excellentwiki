---
title: "[Solution] Cargo Build Script Failed Build.rs Error Fix"
description: "Fix 'build script failed' and build.rs errors in Cargo. Resolve Rust build script compilation and execution issues."
tools: ["cargo"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
---

# Cargo Build Script Failed Build.rs Error Fix

The `build script failed` or `build.rs error` occurs when a Rust crate's build script encounters compilation errors, fails to execute, or encounters system dependency issues.

## What This Error Means

Rust crates can include a `build.rs` file that runs before compilation. When this script fails (compilation error, missing system library, or runtime error), the entire build fails.

A typical error:

```
error: failed to run custom build script for `my-crate v0.1.0`
```

## Why It Happens

Common causes include:

- **Missing system libraries** — build.rs links to C libraries not installed.
- **Compiler not found** — No C compiler for build script.
- **build.rs compilation error** — Rust code in build.rs has errors.
- **Missing pkg-config** — build.rs uses pkg-config for library detection.
- **Wrong environment variables** — build.rs expects specific env vars.
- **Network issues** — build.rs downloads dependencies.

## How to Fix It

### Fix 1: Install system dependencies

```bash
# Ubuntu/Debian
sudo apt-get install build-essential pkg-config libssl-dev

# macOS
xcode-select --install

# CentOS/RHEL
sudo yum install gcc openssl-devel pkg-config
```

### Fix 2: Check build.rs output

```bash
# RIGHT: See build script output
cargo build --verbose 2>&1 | grep "build script"

# Or run build script manually
cargo build -vv
```

### Fix 3: Fix build.rs code

```rust
// RIGHT: Common build.rs patterns
fn main() {
    // Link to system library
    println!("cargo:rustc-link-lib=ssl");
    
    // Set include path
    println!("cargo:rustc-link-search=/usr/local/lib");
    
    // Re-run if file changes
    println!("cargo:rerun-if-changed=build.rs");
}
```

### Fix 4: Install specific build tools

```bash
# Ubuntu: Install all build essentials
sudo apt-get install build-essential cmake pkg-config

# macOS: Install developer tools
xcode-select --install
```

### Fix 5: Use cargo build with features

```bash
# RIGHT: Disable features that need system libraries
cargo build --no-default-features

# Or enable specific features
cargo build --features "vendored"
```

## Common Mistakes

- **Not reading the full error message** — build.rs errors usually say what is missing.
- **Forgetting pkg-config** — Many Rust crates use it for library detection.
- **Not running `cargo clean` before rebuild** — Stale build artifacts cause issues.

## Related Pages

- [Cargo Proc Macro Error](cargo-proc-macro-error) — Proc macro issues
- [Cargo No Std Error](cargo-no-std-error) — no_std linking issues
- [Cargo Cross Compile Error](cargo-cross-compile) — Cross-compilation issues
