---
title: "Landscape Package Management Error"
description: "Landscape fails to manage packages on managed systems"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Landscape Package Management Error

Landscape fails to manage packages on managed systems

## Common Causes

- Landscape client cannot reach package repository
- Package profile not matching system
- APT sources not configured for Landscape
- Package operation timeout

## How to Fix

1. Check client: `landscape-client --check`
2. View package status: check in Landscape web UI
3. Verify APT sources: `cat /etc/apt/sources.list.d/landscape*.list`
4. Restart client: `sudo systemctl restart landscape-client`

## Examples

```bash
# Check Landscape client status
sudo landscape-client --check

# View landscape APT sources
cat /etc/apt/sources.list.d/landscape-*.list

# Restart landscape client
sudo systemctl restart landscape-client
```
