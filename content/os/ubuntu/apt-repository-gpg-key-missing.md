---
title: "[Solution] Ubuntu Server: apt-repository-gpg-key-missing"
description: "Fix Ubuntu apt-repository-gpg-key-missing. APT repository GPG key is missing or expired."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Apt Repository GPG Key Missing

APT cannot verify repository signatures because the GPG key is missing or expired.

## Common Causes
- New repository added without importing its signing key
- GPG key expired or revoked
- Keyring file damaged or missing
- Repository changed its signing key

## How to Fix
1. Import the missing GPG key
```bash
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys <KEY_ID>
```
2. Use the newer signed-by method
```bash
curl -fsSL https://example.com/gpg-key | sudo gpg --dearmor -o /usr/share/keyrings/example.gpg
echo "deb [signed-by=/usr/share/keyrings/example.gpg] https://example.com/repo stable main" | sudo tee /etc/apt/sources.list.d/example.list
```
3. Update package lists
```bash
sudo apt update
```

## Examples
```bash
$ sudo apt update
Err:1 https://dl.google.com/linux/chrome/deb stable InRelease
  The following signatures could not be verified: NO_PUBKEY 1397BC53640DB551
```
