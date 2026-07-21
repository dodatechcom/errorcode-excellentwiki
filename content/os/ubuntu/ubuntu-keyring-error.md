---
title: "Ubuntu Keyring Access Error"
description: "GNOME Keyring or system keyring service fails to unlock"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Ubuntu Keyring Access Error

GNOME Keyring or system keyring service fails to unlock

## Common Causes

- Keyring daemon not running
- PAM configuration not prompting for keyring password
- Keyring file corrupted
- Autologin configured without keyring password

## How to Fix

1. Check daemon: `systemctl --user status gnome-keyring-daemon`
2. Start daemon: `eval $(gnome-keyring-daemon --components=secrets,ssh) && export SSH_AUTH_SOCK`
3. Check PAM: `grep keyring /etc/pam.d/*`
4. Reset keyring: delete ~/.local/share/keyrings/ files

## Examples

```bash
# Check keyring daemon status
systemctl --user status gnome-keyring-daemon

# Start keyring manually
eval $(gnome-keyring-daemon --components=secrets,ssh)
export SSH_AUTH_SOCK=$XDG_RUNTIME_DIR/keyring/ssh
```
