---
title: "[Solution] Cargo Fetch Failed -- Fix Dependency Download Error"
description: "Fix cargo fetch failed errors when cargo cannot download dependencies from the registry. Check network and registry access."
tools: ["cargo"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means `cargo fetch` failed to download dependency sources from crates.io or configured registries.

## Common Causes

- No internet connection
- crates.io is down or rate-limited
- Corporate firewall blocks cargo
- Registry authentication failed

## How to Fix

### 1. Check Network

```bash
curl -I https://crates.io/
```

### 2. Configure Registry Mirror

```toml
# .cargo/config.toml
[source.crates-io]
replace-with = "sparse+https://index.something.com/"

[source.sparse+https://index.something.com/]
registry = "https://index.something.com/"
```

### 3. Use Sparse Protocol

```toml
[source.crates-io]
replace-with = "sparse+https://index.crates.io/"
```

### 4. Retry

```bash
cargo fetch 2>&1
```

## Examples

```bash
$ cargo fetch
error: failed to fetch `https://github.com/rust-lang/crates.io-index`

# Configure sparse index:
$ cargo fetch
    Fetching crates.io index
```
