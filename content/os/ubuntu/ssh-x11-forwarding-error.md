---
title: "SSH X11 Forwarding Error"
description: "X11 forwarding over SSH not working, cannot display GUI applications"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# SSH X11 Forwarding Error

X11 forwarding over SSH not working, cannot display GUI applications

## Common Causes

- X11Forwarding not enabled in sshd_config
- xauth not installed on server
- DISPLAY not set in remote shell
- X11UseLocalhost misconfigured

## How to Fix

1. Enable: `X11Forwarding yes` in /etc/ssh/sshd_config
2. Install xauth: `sudo apt-get install xauth`
3. Test: `ssh -X user@host xclock`
4. Check DISPLAY: `echo $DISPLAY` on remote

## Examples

```bash
# Enable X11 forwarding
sudo sed -i 's/#X11Forwarding no/X11Forwarding yes/' /etc/ssh/sshd_config
sudo systemctl restart sshd

# Test X11 forwarding
ssh -X user@host xclock
# On remote, verify DISPLAY
echo $DISPLAY
```
