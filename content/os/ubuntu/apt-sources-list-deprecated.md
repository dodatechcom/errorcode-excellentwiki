---
title: "[Solution] Ubuntu Server: apt-sources-list-deprecated"
description: "Fix Ubuntu apt-sources-list-deprecated. APT sources.list uses deprecated format for repositories."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Apt Sources List Deprecated

APT warns that the sources.list format is deprecated.

## Common Causes
- Using deb without signed-by in third-party repos
- Distribution codename is EOL
- Repository using unsigned format
- Legacy apt-key style keys

## How to Fix
1. Check current sources
```bash
cat /etc/apt/sources.list
```
2. Convert to signed-by format
```bash
curl -fsSL https://example.com/key.gpg | sudo gpg --dearmor -o /usr/share/keyrings/example.gpg
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/example.gpg] https://example.com/repo stable main" | sudo tee /etc/apt/sources.list.d/example.list
```
3. Remove deprecated apt-key entries
```bash
sudo apt-key list
sudo apt-key del <KEY_ID>
```

## Examples
```bash
$ cat /etc/apt/sources.list.d/old-repo.list
deb https://old.example.com/repo stable main

# Should be:
deb [arch=amd64 signed-by=/usr/share/keyrings/old.gpg] https://old.example.com/repo stable main
```
