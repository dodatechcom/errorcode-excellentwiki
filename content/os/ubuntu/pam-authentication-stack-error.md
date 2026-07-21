---
title: "PAM Authentication Stack Error"
description: "PAM authentication stack misconfiguration prevents login"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# PAM Authentication Stack Error

PAM authentication stack misconfiguration prevents login

## Common Causes

- PAM configuration syntax error
- Required module returns failure
- Stack entry missing 'required' or 'sufficient' control
- Include directive points to non-existent file

## How to Fix

1. Check PAM config: `cat /etc/pam.d/<service>`
2. Verify syntax: `pam-auth-update --test`
3. Check included files exist
4. Restore default: `sudo pam-auth-update`

## Examples

```bash
# Test PAM configuration
sudo pam-auth-update --test

# Check available PAM modules
ls /etc/pam.d/

# Restore PAM defaults
sudo pam-auth-update
```
