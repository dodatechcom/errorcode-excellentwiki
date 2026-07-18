---
title: "[Solution] Cargo MSRV Error — Fix Package Requires Rust Version >= X"
description: "Fix cargo MSRV errors when a crate requires a newer Rust compiler version. Upgrade Rust, pin compatible crate versions, or use rust-toolchain.toml."
tools: ["cargo"]
error-types: ["rust-version-error"]
severities: ["error"]
weight: 5
---

This error means a crate declares a minimum supported Rust version (MSRV) higher than your installed compiler. Cargo refuses to build the crate with an incompatible toolchain.

## What This Error Means

Crates specify `rust-version` in Cargo.toml. When your rustc is too old:

```
error: package `my-crate v1.0.0` cannot be built because it requires rustc >= 1.70.0, while the currently active rustc version is 1.65.0
Either update rustc or use a locked (non-MSRV) version
```

## Why It Happens

- Your system-installed Rust is older than the crate's MSRV
- The crate uses language features or library APIs not available in older Rust versions
- A recent version of a dependency raised its MSRV, pulling in the requirement
- You are using the distro-packaged Rust instead of rustup-managed Rust
- The CI runner or Docker image has an outdated Rust toolchain

## How to Fix It

### Upgrade Rust with rustup

```bash
rustup update stable
rustc --version
```

### Install a Specific Rust Version

```bash
rustup install 1.75.0
rustup default 1.75.0
```

### Pin the Rust Version in the Project

```toml
# rust-toolchain.toml
[toolchain]
channel = "1.75.0"
```

### Use an Older Compatible Crate Version

```bash
cargo update -p my-crate --precise 1.2.0
```

Or pin in Cargo.toml:

```toml
[dependencies]
my-crate = "=1.2.0"
```

### Check the System Rust Version

```bash
# Distro rustc is often behind
which rustc
rustc --version
# If not rustup, install via rustup
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

### Respect MSRV in CI

```yaml
# .github/workflows/ci.yml
- uses: actions-rs/toolchain@v1
  with:
    toolchain: stable
    override: true
```

## Common Mistakes

- Using the system package manager's Rust instead of rustup for development
- Not pinning the toolchain in projects that need reproducibility
- Ignoring MSRV bumps when upgrading dependencies in Cargo.toml
- Assuming all crate versions support the same Rust version

## Related Pages

- [Cargo Feature Error]({{< relref "/tools/cargo/cargo-feature-error" >}}) -- feature flag issues
- [Cargo Dependency Error]({{< relref "/tools/cargo/cargo-dependency-error" >}}) -- dependency resolution
- [Cargo Compilation Error]({{< relref "/tools/cargo/cargo-compilation-error" >}}) -- compilation errors
