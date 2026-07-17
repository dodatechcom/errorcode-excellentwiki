---
title: "[Solution] Linux dnf Dependency Error — Fix"
description: "Fix Linux 'dnf: dependency error' and package installation failures. Resolve DNF dependency conflicts, broken packages, and repository issues."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["dnf", "dependency-error", "package-manager", "fedora", "rhel", "conflict"]
weight: 5
---

# Linux: dnf: dependency error

The `dnf: dependency error` message means DNF (Dandified YUM) cannot satisfy the dependencies required by a requested package. This can happen when a required dependency is not available, there are version conflicts between packages, or a dependency is provided by a package that conflicts with already installed packages.

## What This Error Means

DNF is the next-generation package manager for Fedora, RHEL 8+, and CentOS Stream. It uses SAT-based dependency resolution. When it finds that a package's dependencies cannot be resolved — due to missing packages, version conflicts, or conflicting requirements — it reports the error and refuses to install the package.

## Common Causes

- Required dependency package not available in any repository
- Version conflict between installed and requested packages
- Package requires a newer/older version than what's available
- Conflicting packages already installed
- Repository metadata is outdated
- Package from third-party repo conflicts with system packages

## How to Fix

### 1. Check Available Versions

```bash
# Show all available versions of a package
dnf list available <package> --showduplicates

# Check what provides a dependency
dnf provides "libfoo.so.1"

# Show package dependencies
dnf repoquery --requires <package>
```

### 2. Update Repository Metadata

```bash
# Clean and refresh all repos
sudo dnf clean all
sudo dnf makecache

# Update all packages first
sudo dnf update
```

### 3. Allow Dependency Overrides

```bash
# Skip broken packages
sudo dnf install --skip-broken <package>

# Allow older versions
sudo dnf downgrade <package>

# Remove conflicting packages
sudo dnf remove <conflicting-package>
```

### 4. Install with All Dependencies

```bash
# Install recommended packages too
sudo dnf install --setopt=install_weak_deps=True <package>

# Install build dependencies
sudo dnf builddep <package>
```

### 5. Use Module Streams (Fedora/RHEL 8+)

```bash
# Check available module streams
dnf module list <module-name>

# Enable a specific stream
sudo dnf module enable <module>:<stream>

# Reset a module
sudo dnf module reset <module>
```

### 6. Use DNF History for Rollback

```bash
# View installation history
dnf history list

# Undo a problematic transaction
sudo dnf history undo <transaction-id>

# Rollback to a specific transaction
sudo dnf history rollback <transaction-id>
```

### 7. Install from RPM Fusion or Third-Party Repos

```bash
# Enable RPM Fusion
sudo dnf install \
  https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm \
  https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm

# Then retry the install
sudo dnf install <package>
```

## Examples

```bash
$ sudo dnf install nginx
Error: Transaction test error:
  package nginx-1.24.0-1.fc39.x86_64 requires libpcre.so.1()(64bit), but none of the providers can be installed

$ dnf provides "libpcre.so.1"
pcre2-10.42-2.fc39.x86_64 : Perl-compatible regular expressions library
Matched from:
    provide: libpcre2-8.so.0()(64bit)

$ sudo dnf install pcre2
$ sudo dnf install nginx
# Success
```

```bash
$ sudo dnf install python3-flask
Error: problem with installed package python3-2.7-58.fc29.x86_64

$ sudo dnf install python3-flask --allowerasing
# Resolves the conflict
```

## Related Errors

- [yum repository error]({{< relref "/os/linux/linux-yum-error" >}}) — YUM repository issues
- [rpm package not found]({{< relref "/os/linux/linux-rpm-error" >}}) — RPM database issues
- [apt install failed]({{< relref "/os/linux/linux-apt-install-error" >}}) — Debian package installation failures
