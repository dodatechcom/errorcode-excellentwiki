---
title: "[Solution] Ubuntu Server: apt-release-not-found"
description: "Fix Ubuntu apt-release-not-found. APT cannot find the Release file for a repository."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Apt Release Not Found

APT cannot find the Release file for a repository.

## Common Causes
- Incorrect repository URL or distribution name
- Repository does not contain packages for your architecture
- Mirror server is down or out of sync
- Repository has been reorganized or removed

## How to Fix
1. Verify the source entry
```bash
cat /etc/apt/sources.list
ls /etc/apt/sources.list.d/
```
2. Fix incorrect distribution codename
```bash
lsb_release -cs
```
3. Disable broken repository and update
```bash
sudo mv /etc/apt/sources.list.d/broken.list /etc/apt/sources.list.d/broken.list.disabled
sudo apt update
```

## Examples
```bash
$ sudo apt update
E: The repository 'http://ppa.launchpad.net/owner/repo/ubuntu hirsute Release' does not have a Release file.
```
