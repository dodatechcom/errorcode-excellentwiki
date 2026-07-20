---
title: "[Solution] Ansible WinRM Connection Timeout"
description: "Fix Ansible WinRM timeout issues when connecting to Windows hosts"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

WinRM connection times out when Ansible tries to reach Windows hosts.

```
UNREACHABLE! => "winrm connection error: timed out"
```

## Common Causes

- WinRM service not started
- Firewall blocking ports 5985/5986
- Host overloaded
- Network latency

## How to Fix

```powershell
# On Windows
winrm quickconfig -force
```

```yaml
[win]
winserver ansible_host=10.0.0.50 ansible_winrm_operation_timeout_sec=60

# Or in playbook vars
- hosts: win
  vars:
    ansible_winrm_operation_timeout_sec: 120
    ansible_winrm_read_timeout_sec: 120
```
