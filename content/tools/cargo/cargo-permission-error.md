---
title: "[Solution] Cargo Permission Error — Fix Permission Denied Writing to Target"
description: "Fix cargo permission denied errors when building or writing to the target directory. Remove root-owned files and configure custom target directories safely."
tools: ["cargo"]
error-types: ["permission-error"]
severities: ["error"]
weight: 5
---

This error means cargo cannot write to the `target/` directory or another build output path because the current user lacks file permissions.

## What This Error Means

cargo writes compiled artifacts, fingerprints, and build scripts into the `target/` directory. When the directory is owned by root or another user, cargo fails with:

```
error: couldn't create a temp file: Permission denied (os error 13)
```

Or:

```
error: failed to open `target/debug/.fingerprint/...`
Caused by: Permission denied (os error 13)
```

## Why It Happens

- A previous `sudo cargo build` created root-owned files in `target/`
- The project directory is shared and different users have different permissions
- A mounted filesystem (NFS, Docker volume) has restrictive permissions
- SELinux or AppArmor is blocking access to the build directory
- The `target/` directory was created by a CI runner with a different UID

## How to Fix It

### Remove and Rebuild

```bash
sudo rm -rf target/
cargo build
```

### Fix Ownership of the Project Directory

```bash
sudo chown -R $(whoami) target/
```

### Fix Ownership for an Entire Project

```bash
sudo chown -R $(whoami) /path/to/project/
```

### Use a Custom Target Directory

In `.cargo/config.toml`:

```toml
[build]
target-dir = "/tmp/my-cargo-target"
```

Or via environment variable:

```bash
CARGO_TARGET_DIR=/tmp/my-cargo-target cargo build
```

### Run in a Docker Container with Matching UID

```bash
docker run --user $(id -u):$(id -g) -v $(pwd):/app -w /app rust:latest cargo build
```

### Check SELinux Context

```bash
ls -Z target/
```

If the context is wrong:

```bash
sudo restorecon -Rv target/
```

## Common Mistakes

- Running `sudo cargo build` once and leaving root-owned files behind
- Not checking Docker volume ownership when building inside containers
- Using `chmod 777` as a blanket fix instead of targeting the specific user
- Ignoring the error and retrying without fixing the permissions
- Setting `CARGO_TARGET_DIR` to a path on a read-only filesystem
- Forgetting that NFS or network mounts may have different UID mappings

## Related Pages

- [Cargo Compilation Error]({{< relref "/tools/cargo/cargo-compilation-error" >}}) -- build failures
- [Cargo Network Error]({{< relref "/tools/cargo/cargo-network-error" >}}) -- fetch errors
- [Cargo OpenSSL Error]({{< relref "/tools/cargo/cargo-openssl-error" >}}) -- OpenSSL linking issues
