---
title: "[Solution] Ubuntu Server: apt-authentication-error"
description: "Fix Ubuntu apt-authentication-error. APT cannot authenticate the repository or package."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Apt Authentication Error

APT fails to authenticate the repository because credentials or signatures are invalid.

## Common Causes
- Expired or missing GPG key for the repository
- Repository requires login credentials
- Clock out of sync causing signature verification failure
- Repository URL changed

## How to Fix
1. Check system time
```bash
sudo timedatectl set-ntp true
date
```
2. Re-import the repository key
```bash
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys <KEY_ID>
```
3. Update source with credentials if needed
```bash
echo "deb https://user:pass@repo.example.com/apt stable main" | sudo tee /etc/apt/sources.list.d/secure.list
sudo apt update
```

## Examples
```bash
$ sudo apt update
Err:1 https://repo.example.com/apt stable InRelease
  401  Unauthorized [IP: 192.168.1.100 443]
```
