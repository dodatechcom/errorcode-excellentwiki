---
title: "[Solution] Ubuntu Server: ubuntu-ubuntu-pro-repo-error"
description: "Fix Ubuntu ubuntu-ubuntu-pro-repo-error. Ubuntu Pro repository access fails."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Ubuntu Ubuntu Pro Repository Error

Ubuntu Pro (ESM) repository access fails.

## Common Causes
- Token expired or invalid
- System not attached to Pro
- Repository not enabled after attach

## How to Fix
1. Check Pro status
```bash
sudo pro status
```
2. Attach with valid token
```bash
sudo pro attach <token>
```
3. Enable specific service
```bash
sudo pro enable esm-infra
sudo apt update
```

## Examples
```bash
$ sudo pro status
SERVICE       ENTITLED  STATUS
ESM Infra     yes       disabled
```