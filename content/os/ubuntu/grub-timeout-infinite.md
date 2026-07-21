---
title: "[Solution] Ubuntu Server: grub-timeout-infinite"
description: "Fix Ubuntu grub-timeout-infinite. GRUB menu timeout is set to infinite preventing auto-boot."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# GRUB Timeout Infinite

GRUB menu stays indefinitely waiting for user input.

## Common Causes
- GRUB_TIMEOUT set to -1
- GRUB_TIMEOUT_STYLE set to menu
- Corrupted grub.cfg with bad timeout
- Custom GRUB script overriding timeout

## How to Fix
1. Check current GRUB timeout
```bash
grep GRUB_TIMEOUT /etc/default/grub
```
2. Set proper timeout
```bash
sudo sed -i s/GRUB_TIMEOUT=-1/GRUB_TIMEOUT=3/ /etc/default/grub
sudo update-grub
```

## Examples
```bash
$ grep GRUB_TIMEOUT /etc/default/grub
GRUB_TIMEOUT=-1
GRUB_TIMEOUT_STYLE=menu
```
