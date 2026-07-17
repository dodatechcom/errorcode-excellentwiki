---
title: "[Solution] Linux rpm Package Not Found — Fix"
description: "Fix Linux 'rpm: package not found' and RPM installation errors. Resolve missing packages, dependency issues, and repository problems."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["rpm", "package-not-found", "rpmdb", "dependency", "redhat", "package-manager"]
weight: 5
---

# Linux: rpm: package not found

The `rpm: error: package not found` error means the RPM package manager cannot find the specified package in its database or in configured repositories. This can happen when the package name is wrong, the RPM database is corrupted, dependencies are missing, or the package isn't available in any enabled repository.

## What This Error Means

RPM (Red Hat Package Manager) maintains a local database of all installed packages in `/var/lib/rpm/`. When you run `rpm -i` or `rpm -U`, RPM checks this database and resolves dependencies against installed packages. If a required package isn't in the database and can't be found in repositories, the operation fails.

## Common Causes

- Package name is misspelled or incorrect
- RPM database is corrupted
- Required dependencies not installed
- Package not available in enabled repositories
- Architecture mismatch (x86_64 vs noarch)
- Repository GPG key not imported
- rpmdb version mismatch after system update

## How to Fix

### 1. Search for the Correct Package Name

```bash
# Search installed packages
rpm -qa | grep <keyword>

# Search available packages
yum search <keyword>        # YUM
dnf search <keyword>        # DNF

# Check if package exists
rpm -q <package-name>

# Show package details
rpm -qi <package-name>
```

### 2. Rebuild the RPM Database

```bash
# Stop any running package managers
sudo fuser -k /var/lib/rpm/.rpm.lock 2>/dev/null

# Rebuild the database
sudo rpm --rebuilddb

# Verify database integrity
sudo rpm -Va
```

### 3. Install Missing Dependencies

```bash
# Check dependencies of a package
rpm -qpR package.rpm

# Install with YUM (resolves dependencies automatically)
sudo yum install ./package.rpm

# Install with DNF
sudo dnf install ./package.rpm

# Or use rpm with nodeps (not recommended)
sudo rpm -ivh --nodeps package.rpm
```

### 4. Fix Repository Issues

```bash
# Check enabled repositories
yum repolist
dnf repolist

# Clean and rebuild cache
sudo yum clean all
sudo yum makecache

sudo dnf clean all
sudo dnf makecache

# Import GPG key
sudo rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-*
```

### 5. Install from Local RPM File

```bash
# Install from a downloaded RPM
sudo rpm -ivh package.rpm

# Upgrade from RPM
sudo rpm -Uvh package.rpm

# Force install (use with caution)
sudo rpm -ivh --force package.rpm
```

### 6. Check Architecture

```bash
# Check system architecture
uname -m
rpm --eval '%{_arch}'

# List available architectures for a package
yum search --archlist=x86_64,noarch <package>

# Install specific architecture
sudo yum install <package>.x86_64
```

### 7. Fix rpmdb Version Mismatch

```bash
# If you see "rpmdb version mismatch"
sudo rm -f /var/lib/rpm/__db.*
sudo rpm --rebuilddb

# Then retry the operation
sudo rpm -ivh package.rpm
```

## Examples

```bash
$ sudo rpm -ivh nginx-1.24.0.rpm
error: Failed dependencies:
    libpcre.so.1()(64bit) is needed by nginx-1.24.0

$ sudo yum install pcre
$ sudo rpm -ivh nginx-1.24.0.rpm
# Success

$ rpm -q nginx
package nginx is not installed
```

```bash
$ sudo rpm --rebuilddb
$ sudo yum clean all
$ sudo yum install nginx
Last metadata expiration check: 0:01:23 ago.
Dependencies resolved.
Installing nginx...
```

## Related Errors

- [yum repository error]({{< relref "/os/linux/linux-yum-error" >}}) — YUM repository issues
- [dnf dependency error]({{< relref "/os/linux/linux-dnf-error" >}}) — DNF dependency resolution failures
- [dpkg error]({{< relref "/os/linux/linux-dpkg-error" >}}) — Debian package processing errors
