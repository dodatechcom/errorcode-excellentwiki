---
title: "[Solution] Ubuntu Server: apt-corrupted-package-cache"
description: "Fix Ubuntu apt-corrupted-package-cache. Local APT package cache contains corrupted files."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Apt Corrupted Package Cache

The local APT package cache contains corrupted or incomplete files.

## Common Causes
- Interrupted apt download or upgrade
- Filesystem error on cache partition
- Incomplete package download due to network issue
- Disk write error during cache update

## How to Fix
1. Clean the corrupted cache
```bash
sudo apt clean
sudo rm -rf /var/cache/apt/archives/*
```
2. Rebuild package lists
```bash
sudo rm -rf /var/lib/apt/lists/*
sudo apt update
```
3. Verify integrity
```bash
sudo apt install --reinstall <package>
```

## Examples
```bash
$ sudo apt install vim
E: Failed to fetch http://archive.ubuntu.com/ubuntu/pool/main/v/vim/vim_8.2.3995-3ubuntu2_amd64.deb
  Hashes of expected file match but file length does not match
```
