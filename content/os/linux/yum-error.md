---
title: "[Solution] Linux: yum-error — yum error"
description: "Fix Linux yum-error errors. yum error with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["package-manager"]
weight: 8
---
# Linux: YUM Error

YUM (Yellowdog Updater Modified) errors occur when the package manager fails to install, update, or remove packages on RHEL/CentOS 7 and older.

## Common Causes

- YUM cache corrupted or outdated
- Repository metadata expired or unreachable
- GPG key verification failure
- Package dependency issues
- Lock file from another YUM process

## How to Fix

### 1. Clean YUM Cache

```bash
sudo yum clean all
sudo rm -rf /var/cache/yum/*
```

### 2. Rebuild Metadata

```bash
sudo yum makecache
```

### 3. Clear Lock File

```bash
sudo rm -f /var/run/yum.pid
```

### 4. Fix GPG Keys

```bash
sudo yum update --nogpgcheck
```

## Examples

```bash
$ sudo yum install httpd
Loaded plugins: fastestmirror
Error: Cannot find a valid baseurl for repo: base/7/x86_64

$ sudo yum clean all
$ sudo yum makecache
$ sudo yum install httpd
# Now succeeds
```
