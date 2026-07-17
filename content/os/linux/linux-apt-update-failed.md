---
title: "[Solution] Linux apt update Failed — Repository Not Available"
description: "Fix Linux 'apt update' repository errors. Resolve failed updates, unreachable mirrors, and GPG key issues."
platforms: ["linux"]
severities: ["warning"]
error-types: ["system-error"]
tags: ["apt", "update", "repository", "mirror", "gpg", "package-manager"]
weight: 5
---

# Linux: apt update — repository not available

The `apt update` repository errors such as `Failed to fetch`, `Repository not available`, or `404 Not Found` indicate that the APT package manager cannot reach one or more configured software repositories. This prevents installing or updating packages from those sources.

## What This Error Means

APT maintains a list of repository URLs in `/etc/apt/sources.list` and `/etc/apt/sources.list.d/`. When you run `apt update`, it downloads package indices from each repository. Errors occur when the repository URL is wrong, the mirror is down, the distribution codename is incorrect, or GPG signing keys are missing or expired.

## Common Causes

- Repository URL is incorrect or the mirror is offline
- Distribution codename mismatch (e.g., using `focal` on `jammy`)
- GPG signing key missing or expired
- Network/proxy issues blocking access
- Repository moved or archived (old release)
- Firewall or proxy filtering HTTPS traffic

## How to Fix

### 1. Identify the Failing Repository

```bash
# Run update and capture errors
sudo apt update 2>&1 | grep -E 'Err:|Failed|404|403|503'

# Check configured repositories
cat /etc/apt/sources.list
ls /etc/apt/sources.list.d/
```

### 2. Fix Incorrect Repository URLs

```bash
# Edit the problematic source file
sudo nano /etc/apt/sources.list

# Verify the correct codename
lsb_release -cs

# Correct format:
# deb https://archive.ubuntu.com/ubuntu/ jammy main restricted
# deb https://archive.ubuntu.com/ubuntu/ jammy-updates main restricted
```

### 3. Fix GPG Key Issues

```bash
# Import missing key
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys <KEY_ID>

# Or download and install the keyring
sudo curl -fsSL https://repo.example.com/gpg-key.asc | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/example.gpg

# Remove expired keys
sudo apt-key list
sudo apt-key del <KEY_ID>
```

### 4. Clean and Refresh

```bash
# Clear local cache
sudo apt clean
sudo rm -rf /var/lib/apt/lists/*

# Update again
sudo apt update
```

### 5. Use a Different Mirror

```bash
# Replace with a working mirror
sudo sed -i 's|archive.ubuntu.com|mirror.math.princeton.edu|g' /etc/apt/sources.list

# Or use the main archive
sudo sed -i 's|http://|https://|g' /etc/apt/sources.list

sudo apt update
```

### 6. Handle Archived Repositories

```bash
# For old Ubuntu releases, use old-releases
sudo sed -i 's|archive.ubuntu.com|old-releases.ubuntu.com|g' /etc/apt/sources.list
sudo sed -i 's|security.ubuntu.com|old-releases.ubuntu.com|g' /etc/apt/sources.list

sudo apt update
```

### 7. Disable Problematic Repositories Temporarily

```bash
# Disable a source file
sudo mv /etc/apt/sources.list.d/problematic.list /etc/apt/sources.list.d/problematic.list.disabled

# Or comment out the line
sudo sed -i 's/^deb/# deb/' /etc/apt/sources.list.d/problematic.list

sudo apt update
```

## Examples

```bash
$ sudo apt update
Err:1 https://repo.example.com/ubuntu jammy Release
  404  Not Found [IP: 203.0.113.50 443]
Reading package lists... Done
E: The repository 'https://repo.example.com/ubuntu jammy Release' does not have a Release file.

$ sudo sed -i 's/repo.example.com/archive.ubuntu.com/' /etc/apt/sources.list.d/example.list
$ sudo apt update
Hit:1 https://archive.ubuntu.com/ubuntu jammy InRelease
Reading package lists... Done
```

## Related Errors

- [apt install conflict]({{< relref "/os/linux/linux-apt-install-conflict" >}}) — Dependency conflicts
- [apt locked]({{< relref "/os/linux/linux-apt-locked-v2" >}}) — APT lock errors
- [dpkg reconfigure]({{< relref "/os/linux/linux-dpkg-reconfigure" >}}) — dpkg configuration errors
