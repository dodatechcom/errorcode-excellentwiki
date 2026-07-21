---
title: "[Solution] Cargo Login Failed -- Fix crates.io Authentication"
description: "Fix cargo login failed errors when crate.io token authentication fails. Generate a new token and configure it correctly."
tools: ["cargo"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means `cargo login` failed to authenticate with crates.io. The token may be invalid or expired.

## Common Causes

- Token was revoked on crates.io
- Token was generated for a different account
- Network issues during authentication
- Token format is wrong

## How to Fix

### 1. Generate New Token

Visit https://crates.io/settings/tokens and create a new token.

### 2. Login with Token

```bash
cargo login <your-new-token>
```

### 3. Check Token is Saved

```bash
cat ~/.cargo/credentials.toml
```

### 4. Use Environment Variable

```bash
export CARGO_REGISTRY_TOKEN=<your-token>
```

## Examples

```bash
$ cargo login abc123token
error: failed to login: Unauthorized

# Generate new token at crates.io/settings/tokens
$ cargo login newtoken456
Login token for `crates.io` saved
```
