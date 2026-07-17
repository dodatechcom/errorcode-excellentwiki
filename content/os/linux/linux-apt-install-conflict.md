---
title: "[Solution] Linux apt install Dependency Conflict"
description: "Fix Linux 'apt install' dependency conflict errors. Resolve broken dependencies, version conflicts, and package installation issues."
platforms: ["linux"]
severities: ["error"]
error-types: ["system-error"]
weight: 5
---

# Linux: apt install — dependency conflict

The `apt install` dependency conflict error such as `Unmet dependencies`, `has pre-dependency problem`, or `but <package> is not going to be installed` means APT cannot resolve the package dependency tree. Two packages require incompatible versions of the same dependency, or a dependency chain is broken.

## What This Error Means

APT uses a SAT solver to resolve package dependencies. When you request a package installation, APT checks all transitive dependencies. A conflict occurs when package A requires `libfoo >= 2.0` but package B requires `libfoo < 2.0`, or when an upgrade would break an existing installed package that cannot be upgraded simultaneously.

## Common Causes

- Third-party PPA or repository introducing version conflicts
- Partial upgrade left inconsistent state
- Pinned package version incompatible with new dependencies
- Conflicting packages (e.g., two web servers competing for port 80)
- Held packages preventing dependency resolution
- Architecture mismatch (i386 vs amd64)

## How to Fix

### 1. Read the Error Carefully

```bash
# Run with verbose output
sudo apt install -V <package>

# Show what would be changed
sudo apt install --dry-run <package>

# Check why the conflict exists
sudo apt-cache policy <package>
sudo apt-cache depends <package>
```

### 2. Fix Broken Dependencies

```bash
# Attempt automatic fix
sudo apt --fix-broken install

# Or the older command
sudo apt-get -f install
```

### 3. Remove the Conflicting Package

```bash
# If a specific package is causing the conflict
sudo apt remove <conflicting-package>

# Then retry the installation
sudo apt install <package>

# Force removal if needed
sudo dpkg --remove --force-remove-reinstreq <package>
```

### 4. Update All Packages First

```bash
# Ensure all packages are up to date
sudo apt update
sudo apt upgrade

# Full distribution upgrade
sudo apt dist-upgrade

# Then retry
sudo apt install <package>
```

### 5. Remove Problematic PPA

```bash
# List third-party PPAs
ls /etc/apt/sources.list.d/

# Remove a problematic PPA
sudo add-apt-repository --remove ppa:user/repo

# Or manually remove the source file
sudo rm /etc/apt/sources.list.d/problematic-ppa.list
sudo apt update
```

### 6. Use aptitude as Alternative Solver

```bash
# Install aptitude
sudo apt install aptitude

# Try resolving with aptitude's solver
sudo aptitude install <package>

# aptitude explores more solution paths than apt
# It may find a working combination that apt misses
```

### 7. Pin a Specific Version

```bash
# Hold a package at current version
sudo apt-mark hold <package>

# Or pin a specific version
echo 'Package: <package>
Pin: version 1.2.3-1
Pin-Priority: 1001' | sudo tee /etc/apt/preferences.d/<package>

sudo apt update
sudo apt install <package>
```

## Examples

```bash
$ sudo apt install nginx
Reading package lists... Done
Building dependency tree... Done
Some packages could not be installed. This may mean that you have
requested an impossible situation or if you are using the unstable
distribution that some required packages have not yet been created.
The following packages have unmet dependencies:
 nginx : Depends: nginx-core (< 1.18.0-0ubuntu1.2) but 1.20.0-0ubuntu1 is to be installed
E: Unable to correct problems, you have held broken packages.

$ sudo apt-cache policy nginx-core
nginx-core:
  Installed: 1.20.0-0ubuntu1
  Candidate: 1.20.0-0ubuntu1

$ sudo apt remove nginx-core
$ sudo apt install nginx
# Installs successfully
```

## Related Errors

- [apt update failed]({{< relref "/os/linux/linux-apt-update-failed" >}}) — Repository not available
- [apt locked]({{< relref "/os/linux/linux-apt-locked-v2" >}}) — APT lock errors
- [dpkg reconfigure]({{< relref "/os/linux/linux-dpkg-reconfigure" >}}) — dpkg configuration errors
