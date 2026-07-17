---
title: "[Solution] Linux apt update Failed — Repository Sync Fix"
description: "Fix Linux 'apt update failed' errors. Resolve repository issues, GPG key errors, network problems, and corrupted apt caches."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Linux: apt update failed

The `apt update` command refreshes your package repository metadata. When it fails, you cannot install, upgrade, or even search for packages. Failures often produce errors like `Temporary failure resolving`, `The repository is not signed`, or `Failed to fetch`.

## Common Causes

- No internet connectivity or DNS resolution failure
- Repository URL changed or deprecated (e.g., archive.ubuntu.com EOL)
- GPG key missing or expired for a repository
- Corrupted apt cache (`/var/lib/apt/lists/`)
- Third-party repository incompatible with release version
- Proxy or firewall blocking repository access

## How to Fix

### 1. Check Network Connectivity

```bash
# Test internet access
ping -c 4 google.com

# Test DNS resolution
nslookup archive.ubuntu.com

# Check apt's connectivity to repositories
sudo apt update -o Acquire::http::Timeout=10 -o Acquire::ftp::Timeout=10
```

### 2. Fix DNS Issues

```bash
# Check current DNS settings
cat /etc/resolv.conf

# Add Google DNS temporarily
echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf
echo "nameserver 8.8.4.4" | sudo tee -a /etc/resolv.conf
```

### 3. Fix GPG Key Errors

```bash
# If you see "The following signatures couldn't be verified"
# Add the missing key
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys <KEY_ID>

# Or for newer apt versions (deprecated apt-key)
sudo gpg --homedir /etc/apt/trusted.gpg.d --keyserver keyserver.ubuntu.com --recv-keys <KEY_ID>

# Refresh all keys
sudo apt update --allow-insecure-repositories
```

### 4. Clear Corrupted apt Cache

```bash
# Clear the lists directory
sudo rm -rf /var/lib/apt/lists/*
sudo apt update

# Clear partial downloads
sudo rm -rf /var/cache/apt/archives/partial/*
sudo apt update
```

### 5. Fix Repository Configuration

```bash
# Check your sources list
sudo nano /etc/apt/sources.list
ls /etc/apt/sources.list.d/

# For EOL releases, update the repository URL
# Example: Ubuntu 20.04 EOL → old-releases.ubuntu.com
sudo sed -i 's/archive.ubuntu.com/old-releases.ubuntu.com/g' /etc/apt/sources.list
sudo sed -i 's/security.ubuntu.com/old-releases.ubuntu.com/g' /etc/apt/sources.list
```

### 6. Disable Problematic Repositories

```bash
# Comment out the problematic repository
sudo sed -i 's/^deb /#deb /' /etc/apt/sources.list.d/<problem-repo>.list

# Or move the file aside
sudo mv /etc/apt/sources.list.d/<problem-repo>.list /etc/apt/sources.list.d/<problem-repo>.list.bak

# Run apt update to confirm
sudo apt update
```

### 7. Fix Proxy Configuration

```bash
# Configure apt proxy
echo 'Acquire::http::Proxy "http://proxy.example.com:8080";' | sudo tee /etc/apt/apt.conf.d/proxy.conf
echo 'Acquire::https::Proxy "http://proxy.example.com:8080";' | sudo tee -a /etc/apt/apt.conf.d/proxy.conf
```

### 8. Use a Different Mirror

```bash
# For Ubuntu — switch to a different mirror
sudo sed -i 's/archive.ubuntu.com/mirrors.kernel.org/g' /etc/apt/sources.list
```

## Examples

```bash
$ sudo apt update
Err:1 http://archive.ubuntu.com/ubuntu jammy InRelease
  Temporary failure resolving 'archive.ubuntu.com'
Reading package lists... Done

# DNS is failing — fix resolv.conf
$ cat /etc/resolv.conf
# No nameservers configured

$ echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf
$ sudo apt update
Hit:1 http://archive.ubuntu.com/ubuntu jammy InRelease
Reading package lists... Done
```

```bash
$ sudo apt update
W: GPG error: http://repo.mysql.com/apt/ubuntu jammy InRelease: The following signatures couldn't be verified because the public key is not available: NO_PUBKEY 467B942D3A79BD29

$ sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 467B942D3A79BD29
$ sudo apt update
OK
```

## Related Errors

- [apt locked]({{< relref "/os/linux/apt-locked" >}}) — Package manager lock contention
- [dpkg error]({{< relref "/os/linux/linux-dpkg-error" >}}) — Package configuration failures
- [DNS errors]({{< relref "/os/linux/linux-resolv-conf-error" >}}) — DNS resolution issues
