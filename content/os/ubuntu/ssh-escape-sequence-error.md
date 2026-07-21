---
title: "SSH Escape Sequence Character Error"
description: "SSH connection drops when special escape characters sent"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# SSH Escape Sequence Character Error

SSH connection drops when special escape characters sent

## Common Causes

- Tilde escape (~) character sent accidentally
- SSH escape sequence entered in terminal
- Client disconnects on certain character combinations
- Escape character configured incorrectly

## How to Fix

1. Default escape: `~.` (tilde-period) to disconnect
2. Disable escape: `EscapeChar none` in ssh_config
3. Check escape: `~?` shows escape options
4. Use `-e none` to disable escape character

## Examples

```bash
# SSH escape sequences
# ~.  - Disconnect
# ~?  - Show escape sequences
# ~C  - Open command line
# ~R  - Rekey connection

# Disable escape character
ssh -e none user@host
```
