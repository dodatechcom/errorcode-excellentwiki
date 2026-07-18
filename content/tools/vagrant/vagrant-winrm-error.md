---
title: "[Solution] Vagrant WinRM Error"
description: "Fix Vagrant winrm errors. Learn why this happens and how to resolve it quickly."
tools: ["vagrant"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Vagrant WinRM Error

Vagrant WinRM errors occur when Windows Remote Management connections fail.

## Why This Happens

- Connection refused
- Authentication failed
- WinRM not configured
- Port conflict

## Common Error Messages

- `winrm_connection_error`
- `winrm_auth_error`
- `winrm_config_error`
- `winrm_port_error`

## How to Fix It

### Solution 1: Check WinRM status

Verify WinRM is configured on the VM.

### Solution 2: Fix authentication

Configure WinRM credentials:

```ruby
config.winrm.username = "Administrator"
config.winrm.password = "password"
```

### Solution 3: Check port

Verify WinRM port 5985/5986 is not in use.


## Common Scenarios

- **Connection refused:** Enable WinRM on the VM.
- **Auth failed:** Verify WinRM credentials.

## Prevent It

- Configure WinRM properly
- Test connection
- Monitor WinRM status
