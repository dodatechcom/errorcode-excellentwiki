---
title: "[Solution] Ubuntu Server: apt-no-public-key-error"
description: "Fix Ubuntu apt-no-public-key-error. APT cannot verify signatures because public key is missing."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Apt No Public Key Error

APT cannot verify package signatures because the public key is not available.

## Common Causes
- Key not added to the system keyring
- Repository key ID changed
- Keyring file corrupted
- Package signed with different key

## How to Fix
1. Fetch the missing key
```bash
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys <KEY_ID>
```
2. Alternative using gpg directly
```bash
gpg --keyserver keyserver.ubuntu.com --recv-keys <KEY_ID>
gpg --export <KEY_ID> | sudo tee /usr/share/keyrings/<name>.gpg
```
3. Update after adding key
```bash
sudo apt update
```

## Examples
```bash
$ sudo apt update
The following signatures could not be verified:
  NO_PUBKEY 0E984BC2D39AEC42

$ sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 0E984BC2D39AEC42
gpg: key 0E984BC2D39AEC42: public key "Ubuntu Archive Automatic Signing Key" imported
```
