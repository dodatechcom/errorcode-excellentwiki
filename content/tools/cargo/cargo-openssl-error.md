---
title: "[Solution] Cargo OpenSSL Error — Fix Unable to Find OpenSSL Libraries"
description: "Fix cargo errors when linking to OpenSSL fails because system libraries or development headers are missing. Install packages and configure build paths now."
tools: ["cargo"]
error-types: ["linking-error"]
severities: ["error"]
weight: 5
---

This error means the linker cannot find the OpenSSL libraries or headers needed to compile crates that depend on TLS (such as `reqwest`, `openssl`, or `native-tls`). The build fails at the link step.

## What This Error Means

Many Rust crates that use HTTPS rely on OpenSSL through the `openssl-sys` crate. The build fails with:

```
error: failed to run custom build command for `openssl-sys v0.9.80`

--- stderr
thread 'main' panicked at 'called `Result::unwrap()` on an `Err` value:
  Couldn't find organization of OpenSSL installation.'
```

Or:

```
error: could not find directory of OpenSSL installation
```

## Why It Happens

- The OpenSSL development headers (`libssl-dev`) are not installed
- OpenSSL is installed in a non-standard location that `pkg-config` cannot find
- You are on a minimal Docker image that does not include OpenSSL headers
- The `OPENSSL_DIR` environment variable is not set for a custom installation
- You are cross-compiling and the target architecture OpenSSL is not available

## How to Fix It

### Install OpenSSL Development Packages

```bash
# Debian/Ubuntu
sudo apt install libssl-dev pkg-config

# Fedora/RHEL
sudo dnf install openssl-devel pkg-config

# Alpine
sudo apk add openssl-dev pkgconf

# macOS
brew install openssl
```

### Set OPENSSL_DIR for Non-Standard Locations

```bash
export OPENSSL_DIR=/usr/local/opt/openssl
cargo build
```

### Use vendored OpenSSL

The `openssl-sys` crate can compile OpenSSL from source:

```toml
[dependencies]
openssl = { version = "0.10", features = ["vendored"] }
```

This bundles OpenSSL into the build and avoids system library issues.

### Use rustls Instead of OpenSSL

Many crates offer `rustls` as a TLS backend:

```toml
[dependencies]
reqwest = { version = "0.11", default-features = false, features = ["rustls-tls"] }
```

`rustls` is written in pure Rust and does not need system OpenSSL.

### Set pkg-config Path

```bash
export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig:/usr/lib/pkgconfig
cargo build
```

### Verify pkg-config Can Find OpenSSL

```bash
pkg-config --libs openssl
pkg-config --cflags openssl
```

If both return paths, cargo should find OpenSSL automatically.

## Common Mistakes

- Installing `openssl` but not `libssl-dev` (the headers package)
- Setting `OPENSSL_DIR` to the wrong path (it should point to the installation root, not the `lib/` directory)
- Using the vendored feature in CI without increasing the build timeout
- Not installing `pkg-config` alongside the OpenSSL development files

## Related Pages

- [Cargo Compilation Error]({{< relref "/tools/cargo/cargo-compilation-error" >}}) -- build failures
- [Cargo Permission Error]({{< relref "/tools/cargo/cargo-permission-error" >}}) -- permission issues
- [Cargo Dependency Error]({{< relref "/tools/cargo/cargo-dependency-error" >}}) -- version selection failures
