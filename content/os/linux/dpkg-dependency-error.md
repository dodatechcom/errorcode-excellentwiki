---
title: "[Solution] Linux: dpkg-dependency-error — dpkg dependency conflict"
description: "Fix Linux dpkg-dependency-error errors. dpkg dependency conflict with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["package-manager"]
weight: 8
---
# Linux: dpkg Dependency Error

dpkg dependency errors occur when a package requires another package to be installed or configured first.

## Common Causes

- Package dependencies not installed or broken
- Version conflicts between packages from different repositories
- Held packages preventing dependency resolution
- Mixed package sources (testing/stable/unstable)

## How to Fix

### 1. Fix Broken Dependencies

```bash
sudo apt --fix-broken install
```

### 2. Check Package Dependencies

```bash
dpkg -s <package>
apt-cache depends <package>
```

### 3. Force Install (Last Resort)

```bash
sudo dpkg --ignore-depends=<dependency> -i <package>.deb
```

## Examples

```bash
$ sudo dpkg -i mypackage.deb
dpkg: dependency problems prevent configuration of mypackage:
 mypackage depends on libfoo (>= 1.0); however:
  Package libfoo is not installed.

$ sudo apt --fix-broken install
# Resolves dependencies
```
