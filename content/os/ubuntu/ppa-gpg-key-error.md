---
title: "PPA GPG Key Error"
description: "PPA repository GPG key missing or invalid"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# PPA GPG Key Error

PPA repository GPG key missing or invalid

## Common Causes

- GPG key not imported to system keyring
- Key server unreachable
- Key expired or revoked
- Key imported to wrong location

## How to Fix

1. Add PPA key: `sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys <KEY_ID>`
2. Check keyring: `apt-key list | grep -A5 -B5 <KEY_ID>`
3. Import directly: `curl -fsSL <url> | sudo apt-key add -`
4. Check keyserver: `gpg --keyserver keyserver.ubuntu.com --recv-keys <KEY_ID>`

## Examples

```bash
# Add PPA and its GPG key
sudo add-apt-repository ppa:user/ppa-name

# Or manually add key
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys ABCD1234

# Update package list
sudo apt-get update
```
