---
title: "[Solution] Linux pacman Package Not Found — Fix"
description: "Fix Linux 'pacman: package not found' errors. Resolve Arch Linux package issues, sync databases, and fix repository configuration."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["pacman", "package-not-found", "arch-linux", "aur", "package-manager", "database"]
weight: 5
---

# Linux: pacman: package not found

The `pacman: error: target not found` or `error: could not find or read package` error means the Pacman package manager cannot find the specified package in any configured repository. This typically happens when the package database is outdated, the package name is wrong, or the package exists only in the AUR (Arch User Repository).

## What This Error Means

Pacman maintains local databases of all available packages in `/var/lib/pacman/sync/`. When you run `pacman -S <package>`, it searches these databases. If the package isn't found, the database may be out of sync, the package may have been removed from the repository, or it may be in the AUR (which requires a different tool like `yay` or `paru`).

## Common Causes

- Package database not synced (needs `pacman -Sy`)
- Package name is misspelled
- Package exists only in AUR, not official repositories
- Package was removed from the repository
- Custom repository not properly configured
- Database corruption
- Package is in a different architecture

## How to Fix

### 1. Sync Package Databases

```bash
# Sync and update package databases
sudo pacman -Sy

# Full system update (recommended before installing)
sudo pacman -Syu

# Search for the package
pacman -Ss <keyword>
```

### 2. Search for the Correct Package Name

```bash
# Search official repositories
pacman -Ss <keyword>

# Search installed packages
pacman -Qs <keyword>

# Search AUR (if using yay)
yay -Ss <keyword>

# Get detailed info about a package
pacman -Si <package-name>
```

### 3. Check if Package is in AUR

```bash
# If not found in official repos, check AUR
# Using yay
yay <package-name>

# Using paru
paru <package-name>

# Or search AUR manually
# https://aur.archlinux.org/packages/?K=<package-name>
```

### 4. Fix Database Corruption

```bash
# If database errors occur
sudo pacman -Syy    # Force database refresh

# Check database integrity
sudo pacman -Dk

# If database is severely corrupted
sudo rm /var/lib/pacman/sync/*.db
sudo pacman -Sy
```

### 5. Add Third-Party Repository

```bash
# Edit pacman.conf
sudo nano /etc/pacman.conf

# Add the repository at the end:
# [myrepo]
# SigLevel = Optional TrustAll
# Server = https://myrepo.example.com/$arch

# Update databases
sudo pacman -Sy
```

### 6. Use a Different Mirror

```bash
# Edit mirrorlist
sudo nano /etc/pacman.d/mirrorlist

# Uncomment a faster mirror or add a new one
# Rank mirrors by speed
sudo pacman -Syy
sudo pacman -S reflector
sudo reflector --latest 10 --sort rate --save /etc/pacman.d/mirrorlist
```

### 7. Install Specific Version or from Cache

```bash
# Check local package cache
ls /var/cache/pacman/pkg/<package>*

# Install from cache
sudo pacman -U /var/cache/pacman/pkg/<package>-<version>.pkg.tar.zst

# Check if package was in cache
pacman -Sl | grep <package>
```

## Examples

```bash
$ sudo pacman -S visual-studio-code
error: target not found: visual-studio-code

# Package is in AUR
$ yay -S visual-studio-code
:: There are 2 providers available for visual-studio-code:
:: Repository AUR
    1) visual-studio-code  2) visual-studio-code-bin

# Package name differs in AUR
$ sudo pacman -S firefox
error: target not found: firefox

$ sudo pacman -Syu
$ sudo pacman -S firefox
# Success after database sync
```

## Related Errors

- [pacman database error]({{< relref "/os/linux/linux-pacman-error" >}}) — Database corruption
- [dnf dependency error]({{< relref "/os/linux/linux-dnf-error" >}}) — Dependency resolution issues
- [apt update failed]({{< relref "/os/linux/linux-apt-update-error" >}}) — Repository sync failures
