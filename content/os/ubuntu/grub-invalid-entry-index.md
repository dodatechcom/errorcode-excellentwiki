---
title: "GRUB Invalid Entry Index"
description: "GRUB menu entry index references non-existent menu entry"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# GRUB Invalid Entry Index

GRUB menu entry index references non-existent menu entry

## Common Causes

- GRUB_DEFAULT set to index beyond available entries
- Menu entries changed after kernel update
- GRUB configuration regenerated with fewer entries
- Custom menu entries not properly defined

## How to Fix

1. Set GRUB_DEFAULT to 'saved' instead of numeric index
2. Check available entries: `grep menuentry /boot/grub/grub.cfg`
3. Update GRUB: `sudo update-grub`
4. Edit /etc/default/grub and set correct GRUB_DEFAULT

## Examples

```bash
# List available GRUB menu entries
grep menuentry /boot/grub/grub.cfg

# Set GRUB to remember last selection
sudo sed -i 's/GRUB_DEFAULT=.*/GRUB_DEFAULT=saved/' /etc/default/grub
sudo update-grub
```
