---
title: "[Solution] Cargo Network Error — Fix Failed to Fetch Registry or Crate"
description: "Fix cargo network errors when cargo cannot reach crates.io or fetch crate data. Configure proxies, clear registry cache, and switch to sparse protocol."
tools: ["cargo"]
error-types: ["network-error"]
severities: ["error"]
weight: 5
---

This error means Cargo could not download crate metadata or source tarballs from the registry. The build or update fails before any compilation begins.

## What This Error Means

Cargo connects to `https://crates.io/` (or a configured sparse/registry index) to download package information and source code. When the connection fails, you see:

```
error: failed to fetch `https://github.com/rust-lang/crates.io-index`

Caused by:
  network error: failed to resolve
```

Or:

```
error: unable to get packages from source
```

## Why It Happens

- You are behind a firewall or corporate proxy that blocks crates.io
- DNS resolution fails for `crates.io` or the GitHub-hosted git index
- The crates.io registry is temporarily down or rate-limiting your IP
- A VPN is interfering with the connection
- Your `CARGO_HOME` directory has a corrupted index cache
- SSH keys are missing for private registries hosted on GitHub

## How to Fix It

### Test Connectivity

```bash
curl -I https://crates.io/api/v1/crates
```

If this fails, the problem is at the network level.

### Configure Proxy Settings

```bash
export HTTP_PROXY=http://proxy-server:8080
export HTTPS_PROXY=http://proxy-server:8080
cargo build
```

Or in `~/.cargo/config.toml`:

```toml
[net]
git-fetch-with-cli = true
```

### Use the Sparse Index Protocol

The sparse protocol avoids cloning the entire git index:

```toml
# ~/.cargo/config.toml
[registries.crates-io]
protocol = "sparse"
```

Or set the environment variable:

```bash
export CARGO_REGISTRIES_CRATES_IO_PROTOCOL=sparse
```

### Clear the Corrupted Index Cache

```bash
cargo clean
rm -rf ~/.cargo/registry
cargo build
```

### Increase Timeout

```bash
cargo build 2>&1
```

For slow connections, configure git timeout:

```bash
git config --global http.lowSpeedLimit 0
git config --global http.lowSpeedTime 999999
```

### Use a Mirror Registry

```toml
# ~/.cargo/config.toml
[source.crates-io]
replace-with = "tuna"

[source.tuna]
registry = "sparse+https://mirrors.tuna.tsinghua.edu.cn/crates.io-index/"
```

## Common Mistakes

- Not setting both `HTTP_PROXY` and `HTTPS_PROXY`
- Using the git protocol for the index when the sparse protocol is faster and more reliable
- Forgetting to clear the registry cache after a corrupted download
- Blaming cargo when the VPN or corporate firewall is the actual blocker

## Related Pages

- [Cargo Lock Error]({{< relref "/tools/cargo/cargo-lock-error" >}}) -- lock file issues
- [Cargo OpenSSL Error]({{< relref "/tools/cargo/cargo-openssl-error" >}}) -- OpenSSL linking issues
- [Cargo Protocol Error]({{< relref "/tools/cargo/cargo-protocol-error" >}}) -- protocol version errors
