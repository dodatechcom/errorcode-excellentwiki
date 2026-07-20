---
title: "[Solution] Linux: yum-dependency-error — yum dependency error"
description: "Fix Linux yum-dependency-error errors. yum dependency error with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["package-manager"]
weight: 8
---
# Linux: YUM Dependency Error

YUM dependency errors occur when package requirements cannot be satisfied.

## Common Causes

- Repository missing required package versions
- Third-party repositories with incompatible packages
- EPEL not enabled but package needs it
- Package version conflicts from multiple repositories

## How to Fix

### 1. Check Dependencies

```bash
sudo yum deplist <package>
sudo yum whatrequires <package>
```

### 2. Enable EPEL

```bash
sudo yum install epel-release
sudo yum update
```

### 3. Skip Broken (Temporary)

```bash
sudo yum install <package> --skip-broken
```

### 4. Update All Packages First

```bash
sudo yum update
```

## Examples

```bash
$ sudo yum install myapp
Error: Package: myapp-1.0-1.el7.x86_64 (epel)
           Requires: libfoo >= 2.0
           Installed: libfoo-1.5-1.el7.x86_64 (@base)

$ sudo yum update libfoo
```
