---
title: "[Solution] Cargo Symlink Error — Fix Failed to Create Symlink"
description: "Fix cargo symlink creation errors during crate builds and installs. Resolve permission issues, filesystem limitations, and Windows developer mode conflicts."
tools: ["cargo"]
error-types: ["filesystem-error"]
severities: ["error"]
weight: 5
---

This error means Cargo or a build script tried to create a symbolic link but the filesystem or OS permissions prevented it. Build scripts, cargo install, and certain crate operations rely on symlinks.

## What This Error Means

Cargo creates symlinks for various purposes: build script outputs, cargo-installed binaries, and crate-level links. When symlink creation fails:

```
error: failed to create symbolic link
  --> /home/user/.cargo/bin/my-tool

Caused by:
  Permission denied (os error 13)
```

Or on Windows:

```
error: could not create symlink: required privileges not held
```

## Why It Happens

- The filesystem does not support symlinks (FAT32, exFAT, some network mounts)
- The user does not have permission to create symlinks in the target directory
- On Windows, Developer Mode is not enabled (required for unprivileged symlink creation)
- The target path is on a read-only filesystem
- SELinux or AppArmor policies block symlink creation
- The CARGO_HOME directory has restrictive permissions

## How to Fix It

### Check Filesystem Type

```bash
df -T ~/.cargo
# Avoid FAT32, exFAT, or NTFS without symlink support
```

### Fix Permission on CARGO_HOME

```bash
sudo chown -R $(whoami) ~/.cargo
chmod -R 755 ~/.cargo
```

### Enable Windows Developer Mode

On Windows 10/11, go to Settings > Update & Security > For Developers and enable Developer Mode.

### Use a Filesystem that Supports Symlinks

Move CARGO_HOME to a native Linux filesystem:

```bash
export CARGO_HOME=/home/$USER/.cargo
mkdir -p $CARGO_HOME
```

### Disable Symlinks in Cargo Config

```toml
# ~/.cargo/config.toml
[install]
locked = true
```

### Run as Administrator (Windows)

```cmd
# Run command prompt or PowerShell as Administrator
cargo install <crate>
```

## Common Mistakes

- Running cargo on a WSL project located on the Windows filesystem (/mnt/c/) where symlinks are restricted
- Not enabling Developer Mode on Windows before using cargo
- Storing cargo projects on network-mounted drives without symlink support
- Using sudo for cargo commands which writes files as root

## Related Pages

- [Cargo Permission Error]({{< relref "/tools/cargo/cargo-permission-error" >}}) -- permission denied
- [Cargo Network Error]({{< relref "/tools/cargo/cargo-network-error" >}}) -- network issues
- [Cargo Compilation Error]({{< relref "/tools/cargo/cargo-compilation-error" >}}) -- build failures
