---
title: "[Solution] Brew Permission Error — Fix EACCES and Access Denied in Homebrew"
description: "Fix Homebrew permission denied errors when brew cannot write to its directories. Fix ownership of /usr/local and avoid using sudo with any brew commands."
tools: ["brew"]
error-types: ["permission-error"]
severities: ["error"]
weight: 5
---

This error means Homebrew cannot read or write to its own directories because the current user does not have the required file permissions. This is the most common Homebrew error on shared or misconfigured systems.

## What This Error Means

Homebrew owns its files under `/usr/local/` (Intel Mac) or `/opt/homebrew/` (Apple Silicon). When those directories are owned by root or another user, brew operations fail with:

```
Error: Permission denied - /usr/local/Cellar/<formula>
```

Or:

```
Error: Could not create /usr/local/Cellar
Check permissions for /usr/local
```

## Why It Happens

- A previous `sudo brew install` created root-owned files
- The system was upgraded and `/usr/local` ownership changed
- A shared Mac has multiple users with different UIDs
- Homebrew was moved or copied manually instead of using `brew install`
- macOS System Integrity Protection (SIP) is blocking writes to system directories

## How to Fix It

### Check Ownership

```bash
ls -la /usr/local
# or on Apple Silicon:
ls -la /opt/homebrew
```

The first column should show your username, not `root`.

### Fix Ownership of /usr/local

```bash
sudo chown -R $(whoami) /usr/local
```

On Apple Silicon:

```bash
sudo chown -R $(whoami) /opt/homebrew
```

### Fix Specific Cellar Files

```bash
sudo chown -R $(whoami) /usr/local/Cellar/<formula>
```

### Fix Permissions After a Sudo Install

```bash
sudo chown -R $(whoami) /usr/local/*
```

### Never Use sudo with brew

Homebrew is designed to run as a normal user. Remove sudo from any brew alias or script:

```bash
# Bad
sudo brew install <formula>

# Good
brew install <formula>
```

### If macOS SIP Is Blocking Access

Check SIP status:

```bash
csrutil status
```

On Apple Silicon, you may need to adjust the ownership of `/opt/homebrew` with:

```bash
sudo chown -R $(whoami) /opt/homebrew
```

SIP does not protect `/opt/homebrew` by default.

## Common Mistakes

- Running `sudo brew install` as a quick fix, which breaks everything else
- Not noticing that `/usr/local` is root-owned until multiple operations fail
- Using `chmod 777` instead of targeted `chown`
- Ignoring the error and retrying the same command with `sudo`

## Related Pages

- [Brew Install Error]({{< relref "/tools/brew/brew-install-error" >}}) -- formula installation failures
- [Brew Update Error]({{< relref "/tools/brew/brew-update-error" >}}) -- brew update failures
- [Brew Dependency Error]({{< relref "/tools/brew/brew-dependency-error" >}}) -- missing dependencies
