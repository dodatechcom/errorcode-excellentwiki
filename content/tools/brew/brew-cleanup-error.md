---
title: "[Solution] Brew Cleanup Error — Fix Permission Denied or Cleanup Failed"
description: "Fix Homebrew cleanup errors when brew cleanup fails due to permissions or locked files. Resolve ownership issues and safely remove old formula versions."
tools: ["brew"]
error-types: ["cleanup-error"]
severities: ["warning"]
weight: 5
---

This error means `brew cleanup` could not remove old versions of formulae, cached downloads, or temporary files. The cleanup process encountered a permission error or a locked resource.

## What This Error Means

Homebrew cleanup deletes old formula versions, stale lock files, and cached downloads. When it fails:

```
Error: Permission denied @ dir_s_mkdir - /usr/local/Cellar/<formula>/1.0
Error: While cleaning up <formula>, permission was denied
```

Or:

```
Warning: Skipping <formula>: most recent version 1.0 installed but 0.9 remains
Cleanup had to skip some files because of permissions or locked files
```

## Why It Happens

- Previous `sudo brew install` commands created files owned by root
- Another brew process is running and holding locks
- The Cellar or Caskroom directory has incorrect ownership
- A formula pin prevents cleanup from removing old versions
- The disk is full and cleanup cannot write temporary metadata
- macOS SIP (System Integrity Protection) protects certain paths

## How to Fix It

### Run Cleanup with Verbose Output

```bash
brew cleanup -v
```

### Fix Cellar Ownership

```bash
sudo chown -R $(whoami) /usr/local/Cellar
sudo chown -R $(whoami) /usr/local/Homebrew
brew cleanup
```

### Check and Remove Stale Locks

```bash
ls -la /usr/local/var/homebrew/locks/
rm -f /usr/local/var/homebrew/locks/*
brew cleanup
```

### List Pinned Formulae

```bash
brew pin list
brew unpin <formula>
brew cleanup
```

### Cleanup Specific Formulae

```bash
brew cleanup <formula>
```

### Dry Run First

```bash
brew cleanup -n  # shows what would be removed
```

### Force Cleanup with Sudo

```bash
sudo brew cleanup
```

## Common Mistakes

- Running `sudo brew cleanup` regularly instead of fixing permissions
- Pinning formulae for too long, accumulating old versions
- Not running `brew cleanup` periodically, letting old versions fill the disk
- Ignoring the `Warning: Skipping` messages that indicate cleaned-by-sudo issues

## Related Pages

- [Brew Permission Error]({{< relref "/tools/brew/brew-permission-error" >}}) -- permission issues
- [Brew Install Error]({{< relref "/tools/brew/brew-install-error" >}}) -- install failures
- [Brew Update Error]({{< relref "/tools/brew/brew-update-error" >}}) -- update problems
