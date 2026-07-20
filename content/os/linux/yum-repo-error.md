---
title: "[Solution] Linux: yum-repo-error — yum repository error"
description: "Fix Linux yum-repo-error errors. yum repository error with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["package-manager"]
weight: 8
---
# Linux: YUM Repository Error

YUM repository errors occur when YUM cannot access or validate configured software repositories.

## Common Causes

- Repository URL changed or not accessible
- Network connectivity issues reaching the repo
- Repository metadata expired or corrupted
- GPG key missing or expired
- Repository configuration file has errors

## How to Fix

### 1. List Repos and Check Errors

```bash
sudo yum repolist all
sudo yum repolist -v
```

### 2. Check Repo Files

```bash
ls -la /etc/yum.repos.d/
cat /etc/yum.repos.d/*.repo
```

### 3. Clean and Refresh

```bash
sudo yum clean all
sudo yum makecache
```

### 4. Disable Problematic Repo

```bash
sudo yum --disablerepo=<repo> update
```

## Examples

```bash
$ sudo yum update
Loaded plugins: fastestmirror
Could not retrieve mirrorlist http://mirrorlist.centos.org/?release=7&arch=x86_64&repo=os&infra=stock error was
14: curl#6 - "Could not resolve host: mirrorlist.centos.org; Unknown error"

$ cat /etc/yum.repos.d/CentOS-Base.repo
# Check baseurl/mirrorlist settings
```
