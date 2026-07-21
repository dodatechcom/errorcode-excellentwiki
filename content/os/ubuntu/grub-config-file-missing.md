---
title: "GRUB Configuration File Missing"
description: "GRUB cannot find grub.cfg or its source configuration files"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# GRUB Configuration File Missing

GRUB cannot find grub.cfg or its source configuration files

## Common Causes

- /boot/grub/grub.cfg deleted or corrupted
- /etc/default/grub missing after disk failure
- /etc/grub.d/ scripts not executable
- Boot partition reformatted without GRUB reinstallation

## How to Fix

1. Boot from live USB and reinstall GRUB
2. Regenerate grub.cfg: `sudo grub-mkconfig -o /boot/grub/grub.cfg`
3. Ensure /etc/default/grub exists with correct settings
4. Check permissions: `ls -la /etc/grub.d/`

## Examples

```bash
# Regenerate GRUB config
sudo grub-mkconfig -o /boot/grub/grub.cfg

# Check GRUB config file exists
ls -la /etc/default/grub
```
