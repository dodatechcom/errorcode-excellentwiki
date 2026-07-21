---
title: "[Solution] Ubuntu Server: kernel-livepatch-error"
description: "Fix Ubuntu kernel-livepatch-error. Canonical Livepatch service fails to apply kernel patches."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Kernel Livepatch Error

Canonical Livepatch fails to apply kernel patches.

## Common Causes
- Livepatch token expired or invalid
- Kernel version not supported
- snapd not running properly
- Livepatch service not enabled

## How to Fix
1. Check Livepatch status
```bash
sudo canonical-livepatch status
```
2. Enable Livepatch
```bash
sudo canonical-livepatch enable <your-token>
```
3. Restart snapd
```bash
sudo systemctl restart snapd
```
4. Check logs
```bash
journalctl -u snap.canonical-livepatch.canonical-livepatchd
```

## Examples
```bash
$ sudo canonical-livepatch status
error: not enabled

$ sudo canonical-livepatch enable abc123token
Successfully enabled device
```
