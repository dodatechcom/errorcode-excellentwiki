---
title: "[Solution] Linux apt install Failed — Package Install Fix"
description: "Fix Linux 'apt install failed' errors. Resolve package dependency issues, broken packages, and installation conflicts."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["apt-install", "package-installation", "dependencies", "broken-packages", "apt"]
weight: 5
---

# Linux: apt install failed

The `apt install` command fails when the package manager cannot satisfy dependencies, a package is already broken, or the requested package does not exist in configured repositories.

## Common Causes

- Unmet dependencies between packages
- Broken packages from a previous interrupted installation
- Package not available in configured repositories
- Package name misspelled or version mismatch
- Conflicting packages installed from different sources
- Architecture mismatch (i686 vs amd64)

## How to Fix

### 1. Fix Broken Packages First

```bash
# Fix broken dependencies
sudo apt --fix-broken install

# Configure any half-installed packages
sudo dpkg --configure -a
```

### 2. Search for the Correct Package Name

```bash
# Search for the package
apt search <keyword>

# Check if the package is available in any repository
apt policy <package-name>

# Show package details
apt show <package-name> 2>/dev/null || echo "Package not found"
```

### 3. Check and Fix Dependencies

```bash
# Simulate installation to see dependency issues
sudo apt install -s <package-name>

# Install with missing dependencies
sudo apt install --install-recommends <package-name>

# Forcibly install without dependencies (use with caution)
sudo dpkg -i --force-depends <package>.deb
sudo apt --fix-broken install
```

### 4. Add Missing Repository

```bash
# If the package is not found, you may need to add a repository
# For example, adding a PPA for Ubuntu
sudo add-apt-repository ppa:<ppa-name>
sudo apt update
sudo apt install <package-name>

# For Debian, check backports
sudo apt install -t bullseye-backports <package-name>
```

### 5. Handle Conflicting Packages

```bash
# Check what conflicts with the package
apt-cache showpkg <package-name> | grep Conflicts

# Remove the conflicting package
sudo apt remove <conflicting-package>

# Use apt to replace
sudo apt install <package-name> --allow-change-held-packages
```

### 6. Install from a Local .deb File

```bash
# Download the .deb and dependencies
sudo apt build-dep <package-name>

# Install the .deb with dependencies
sudo dpkg -i /path/to/package.deb
sudo apt --fix-broken install
```

### 7. Use aptitude for Advanced Resolution

```bash
# Install aptitude
sudo apt install aptitude

# Use it to resolve complex dependencies
sudo aptitude install <package-name>

# aptitude offers interactive resolution suggestions
```

### 8. Clear the Package Cache

```bash
# Remove cached package files
sudo apt clean

# Remove partial downloads
sudo rm -rf /var/cache/apt/archives/partial/*
sudo apt update
```

## Examples

```bash
$ sudo apt install nginx
The following packages have unmet dependencies:
 nginx : Depends: nginx-core (< 1.24.0-1ubuntu2.1) but 1.24.0-1ubuntu2.2 is to be installed
E: Unable to correct problems, you have held broken packages.

$ sudo apt --fix-broken install
$ sudo apt install nginx
Reading package lists... Done
Building dependency tree... Done
nginx is already the newest version (1.24.0-1ubuntu2.2).
```

```bash
$ sudo apt install nonexistent-package
E: Unable to locate package nonexistent-package

$ apt search nonexistent
Sorting... Done
Full Text Search... Done
# No results — package does not exist in any repository
```

## Related Errors

- [apt update failed]({{< relref "/os/linux/linux-apt-update-error" >}}) — Repository sync failures
- [dpkg error]({{< relref "/os/linux/linux-dpkg-error" >}}) — Package processing errors
- [apt locked]({{< relref "/os/linux/apt-locked" >}}) — Package manager lock issues
