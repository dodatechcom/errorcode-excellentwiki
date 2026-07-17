---
title: "[Solution] Linux yum Repository Error — Fix"
description: "Fix Linux 'yum: repository error' and YUM installation failures. Resolve repo configuration, GPG key, and cache issues."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["yum", "repository-error", "repo", "gpg-key", "package-manager", "centos"]
weight: 5
---

# Linux: yum: repository error

The `yum: repository error` message means YUM cannot access or process one or more configured package repositories. This prevents installing, updating, or searching for packages. Errors may include `Cannot retrieve repository metadata`, `GPG key retrieval failed`, or `Repository not found`.

## What This Error Means

YUM (Yellowdog Updater Modified) reads repository configurations from `/etc/yum.repos.d/` and fetches package metadata from remote servers. When a repository is unreachable, misconfigured, has an expired GPG key, or its metadata is corrupted, YUM reports a repository error and may refuse to operate.

## Common Causes

- Repository URL is incorrect or unreachable
- GPG key missing or expired
- Repository metadata cache is corrupted
- Network connectivity issues
- Repository is disabled or removed
- DNS resolution failure for repository server
- Proxy configuration blocking repository access

## How to Fix

### 1. Check Repository Configuration

```bash
# List all repositories
yum repolist

# List all repositories including disabled
yum repolist all

# Check repository details
yum repoinfo <repo-name>

# Check repository files
ls /etc/yum.repos.d/
cat /etc/yum.repos.d/CentOS-Base.repo
```

### 2. Clean and Rebuild Cache

```bash
# Clean all caches
sudo yum clean all

# Clean specific cache
sudo yum clean metadata
sudo yum clean packages

# Rebuild cache
sudo yum makecache
```

### 3. Fix GPG Key Issues

```bash
# Import GPG keys
sudo rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7
sudo rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7

# Disable GPG check temporarily (less secure)
sudo yum install --nogpgcheck <package>

# Or disable in repo config
sudo sed -i 's/gpgcheck=1/gpgcheck=0/' /etc/yum.repos.d/myrepo.repo
```

### 4. Fix Repository URLs

```bash
# Edit the problematic repository
sudo nano /etc/yum.repos.d/myrepo.repo

# Common URL fixes:
# - CentOS 7: use vault.centos.org instead of mirror.centos.org
# - EPEL: use dl.fedoraproject.org

# Example fix for CentOS 7 EOL:
sudo sed -i 's/mirrorlist=/mirrorlist=/g' /etc/yum.repos.d/CentOS-Base.repo
sudo sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-Base.repo
```

### 5. Enable/Disable Repositories

```bash
# Enable a repository
sudo yum-config-manager --enable <repo-name>

# Disable a repository
sudo yum-config-manager --disable <repo-name>

# Add a new repository
sudo yum-config-manager --add-repo https://example.com/myrepo.repo
```

### 6. Fix Network and DNS Issues

```bash
# Test repository connectivity
curl -I https://mirror.centos.org

# Check DNS resolution
nslookup mirror.centos.org

# Configure proxy for YUM
sudo nano /etc/yum.conf
# Add: proxy=http://proxy.example.com:8080
```

### 7. Handle Repository Metadata Errors

```bash
# If metadata is corrupted
sudo yum clean all
sudo rm -rf /var/cache/yum/
sudo yum makecache

# If specific repo metadata is bad
sudo yum clean metadata --disablerepo=* --enablerepo=badrepo
sudo yum makecache --disablerepo=* --enablerepo=badrepo
```

## Examples

```bash
$ sudo yum install nginx
Loaded plugins: fastestmirror
Loading mirror speeds from cached hostfile
Could not retrieve mirrorlist http://mirror.centos.org/centos/7/os/x86_64/mirrorlist
Error was: [Errno 14] curl#6 - "Could not resolve host"

# CentOS 7 is EOL — fix repository URLs
$ sudo sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*.repo
$ sudo yum clean all
$ sudo yum install nginx
```

```bash
$ sudo yum update
GPG key retrieval failed: [Errno 14] curl#35 - "SSL connect error"

$ sudo rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7
$ sudo yum update
# Success
```

## Related Errors

- [rpm package not found]({{< relref "/os/linux/linux-rpm-error" >}}) — RPM database issues
- [dnf dependency error]({{< relref "/os/linux/linux-dnf-error" >}}) — DNF dependency failures
- [apt update failed]({{< relref "/os/linux/linux-apt-update-error" >}}) — Debian repository issues
