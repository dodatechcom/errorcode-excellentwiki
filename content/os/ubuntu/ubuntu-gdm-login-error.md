---
title: "Ubuntu GDM Login Screen Error"
description: "GDM (GNOME Display Manager) login screen fails to load or accepts no input"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Ubuntu GDM Login Screen Error

GDM (GNOME Display Manager) login screen fails to load or accepts no input

## Common Causes

- GDM service not running
- X11 or Wayland session failing
- GPU driver incompatible with display server
- User session configuration corrupted

## How to Fix

1. Check GDM: `systemctl status gdm3`
2. Check logs: `journalctl -u gdm3`
3. Switch to TTY: `Ctrl+Alt+F3` and login
4. Reset GDM: `sudo dpkg-reconfigure gdm3`

## Examples

```bash
# Check GDM status
systemctl status gdm3

# Restart GDM
sudo systemctl restart gdm3

# Reconfigure GDM
sudo dpkg-reconfigure gdm3
```
