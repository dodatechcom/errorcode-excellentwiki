---
title: "[Solution] Linux: sudo-env-error -- sudo environment error"
description: "Fix Linux sudo environment errors. Sudo environment variable preservation failure."
os: ["linux"]
error-types: ["sudo-error"]
severities: ["warning"]
---

# Linux: Sudo Environment Error

Sudo environment errors occur when variables are incorrectly stripped or preserved.

## Common Causes

- env_reset stripping required variables
- secure_path overriding user PATH
- env_keep configuration missing for needed vars
- HOME=reset changing script behavior
- sudo -E failing due to env_keep not configured

## How to Fix

### 1. Check Sudo Config

```bash
sudo grep -E "env_reset|secure_path|env_keep" /etc/sudoers
sudo -V | head -10
```

### 2. Preserve Environment

```bash
sudo -E env
# Add to /etc/sudoers.d/env
Defaults    env_keep += "PATH"
Defaults    env_keep += "LANG"
Defaults    env_keep += "HOME"
```

### 3. Pass Specific Variables

```bash
sudo MY_VAR=value /path/to/script
sudo env MY_VAR=value command
```

## Examples

```bash
$ sudo -E echo $MY_VAR
# Empty - not preserved
$ sudo grep env_keep /etc/sudoers
Defaults    env_keep += "PATH"
$ sudo -E env | grep PATH
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
```
