---
title: "[Solution] Cargo Dependency Error — Fix Version Selection Failures"
description: "Fix cargo dependency errors when cargo cannot select a compatible version for a crate. Use cargo tree to inspect conflicts and patch broken dependencies."
tools: ["cargo"]
error-types: ["dependency-error"]
severities: ["error"]
weight: 5
---

This error means Cargo's resolver could not find a version of a dependency that satisfies every requirement in the dependency tree. The build stops before any compilation begins.

## What This Error Means

Cargo uses a SAT-solver to pick compatible versions of all crates. When no valid combination exists, you get:

```
error: failed to select a version for `serde`.
    ... required by package myapp v0.1.0
    versions that meet the requirements `serde = "^1.0.152"` are: 1.0.152, 1.0.153, ...
    all available versions: 0.8.0, 0.8.1, ...
```

The error names the crate, the constraints, and the available versions.

## Why It Happens

- Two dependencies require incompatible semver ranges of the same crate
- You specified a version range that does not exist on crates.io
- A dependency requires a feature that only exists in a pre-release version
- The crate was yanked and is no longer available for new resolution
- You are using `path` and `git` dependencies that clash with a crates.io version

## How to Fix It

### Read the Constraint Chain

The error message lists every crate and its version requirement. Identify which two crates have overlapping but incompatible ranges.

### Relax Version Requirements

In `Cargo.toml`:

```toml
[dependencies]
serde = "1"
```

Using `"1"` instead of `"=1.0.152"` gives the resolver more room.

### Update All Dependencies

```bash
cargo update
```

This finds the latest compatible versions for everything.

### Use `[patch]` to Override a Dependency

```toml
[patch.crates-io]
serde = { git = "https://github.com/serde-rs/serde", branch = "main" }
```

Or point to a specific version:

```toml
[patch.crates-io]
serde = { version = "1.0.155" }
```

### Check for Yanked Versions

```bash
cargo search serde
```

If the version you need was yanked, `cargo update` will skip it automatically.

### Use `cargo tree` to Inspect the Dependency Graph

```bash
cargo tree -i serde
```

This shows every crate that depends on `serde` and what version range it requires.

## Common Mistakes

- Pinning exact versions in `Cargo.toml` without understanding semver compatibility
- Not running `cargo update` after changing `Cargo.toml`
- Ignoring the full error trace and guessing which crate to update
- Using `[patch]` as a permanent fix instead of updating to a released version

## Related Pages

- [Cargo Compilation Error]({{< relref "/tools/cargo/cargo-compilation-error" >}}) -- build failures
- [Cargo Feature Error]({{< relref "/tools/cargo/cargo-feature-error" >}}) -- missing feature flags
- [Cargo Lock Error]({{< relref "/tools/cargo/cargo-lock-error" >}}) -- lock file issues
