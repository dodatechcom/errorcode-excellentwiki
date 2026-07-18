---
title: "[Solution] Cargo Target Triple Error — Fix No Matching Package Found"
description: "Fix cargo target triple errors when no package matches the current build target. Configure cross-compilation target triples and resolve platform mismatch issues."
tools: ["cargo"]
error-types: ["build-error"]
severities: ["error"]
weight: 5
---

This error means the crate you are building has no source files or dependencies that match your current target triple. Cargo cannot find compatible code for your platform.

## What This Error Means

Every Rust target has a triple like `x86_64-unknown-linux-gnu` or `aarch64-apple-darwin`. When a crate uses conditional compilation with `cfg(target_os)` or `cfg(target_arch)` and no match exists:

```
error: no matching package found
  searched package name: `my-crate`
  maybe you meant:       my-crate-linux

error[E0433]: failed to resolve: use of undeclared type
```

Or when the target triple is not installed:

```
error: could not compile `crate` due to previous error
error: linker `cc` not found
```

## Why It Happens

- You are cross-compiling and the target triple is not installed via rustup
- The crate has platform-specific code paths but none for your OS or architecture
- The `--target` flag specifies a triple that does not match your toolchain
- The linker for the target platform is missing from your system
- A dependency uses `cfg` attributes that exclude your target

## How to Fix It

### Check the Default Target

```bash
rustup show
rustc -vV | grep host
```

### Install the Required Target

```bash
rustup target add aarch64-unknown-linux-gnu
cargo build --target aarch64-unknown-linux-gnu
```

### List All Available Targets

```bash
rustup target list
rustup target list --installed
```

### Set the Default Target

```bash
rustup default stable-x86_64-unknown-linux-gnu
```

Or in `.cargo/config.toml`:

```toml
[build]
target = "x86_64-unknown-linux-gnu"
```

### Install the Cross-Compilation Linker

For Linux to ARM:

```bash
sudo apt install gcc-aarch64-linux-gnu
```

For macOS to Linux:

```bash
brew install filosottile/musl-cross/musl-cross
```

### Add a .cargo/config.toml for Cross-Compilation

```toml
[target.aarch64-unknown-linux-gnu]
linker = "aarch64-linux-gnu-gcc"
```

## Common Mistakes

- Forgetting that cross-compilation requires both the target std library and a compatible linker
- Using `--target` without first running `rustup target add`
- Assuming the host target is always x86_64-unknown-linux-gnu on Linux
- Not checking the crate's `cfg` gates before attempting a cross-compile

## Related Pages

- [Cargo Compilation Error]({{< relref "/tools/cargo/cargo-compilation-error" >}}) -- compilation failures
- [Cargo Dependency Error]({{< relref "/tools/cargo/cargo-dependency-error" >}}) -- dependency issues
- [Cargo Feature Error]({{< relref "/tools/cargo/cargo-feature-error" >}}) -- feature flag problems
