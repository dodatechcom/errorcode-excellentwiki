---
title: "[Solution] Cargo Yanked Crate Error — Fix Yanked Version in Cargo.toml"
description: "Fix cargo yanked crate version errors when a dependency version was removed from the registry. Update Cargo.lock or pin to a non-yanked version."
tools: ["cargo"]
error-types: ["dependency-error"]
severities: ["error"]
weight: 5
---

This error means a crate version you depend on has been yanked from the registry. Yanked versions are not deleted but are marked as unfit for new use, and Cargo refuses to use them.

## What This Error Means

A crate author can yank a version to prevent new projects from depending on it. When you try to build:

```
error: failed to select a version for the requirement `my-dep = "^1.0"`
  candidate versions which were yanked: 1.0.0
  all valid versions: 1.0.1
```

Or during `cargo generate-lockfile`:

```
error: the crate `my-dep` has been yanked (version 1.0.0)
```

## Why It Happens

- The crate author yanked a version due to a security vulnerability
- A bug was found in a published version and the author retracted it
- The yanked version has a broken dependency that cannot be resolved
- Your Cargo.lock was generated before the yank and you are building in a new environment
- A transitive dependency transitively depends on the yanked version

## How to Fix It

### Update the Dependency to a Non-Yanked Version

```bash
cargo update -p my-dep
```

Or update everything:

```bash
cargo update
```

### Manually Pin to a Specific Version

```toml
# Cargo.toml
[dependencies]
my-dep = "1.0.1"
```

### Check What Versions Are Yanked

```bash
cargo search my-dep
# Or visit https://crates.io/crates/my-dep
```

### Use a Git Dependency as Fallback

If the maintainer has not published a fix:

```toml
[dependencies]
my-dep = { git = "https://github.com/user/my-dep", branch = "main" }
```

### Downgrade to the Last Good Version

```bash
cargo update -p my-dep --precise 0.9.0
```

### Check for Transitive Yanked Crates

```bash
cargo tree -i my-dep  # find what depends on the yanked crate
cargo update -p <transitive-dep>
```

## Common Mistakes

- Manually editing Cargo.lock instead of running `cargo update`
- Pinning to a yanked version with `=` instead of using the replacement
- Not checking whether the yank was intentional or accidental
- Assuming yanked crates are completely removed from the registry

## Related Pages

- [Cargo Dependency Error]({{< relref "/tools/cargo/cargo-dependency-error" >}}) -- dependency issues
- [Cargo Lock Error]({{< relref "/tools/cargo/cargo-lock-error" >}}) -- lock file problems
- [Cargo Network Error]({{< relref "/tools/cargo/cargo-network-error" >}}) -- network issues
