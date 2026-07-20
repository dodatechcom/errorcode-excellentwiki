---
title: "[Solution] Ansible WinRM Connection Timeout"
description: "Fix WinRM timeout issues when managing Windows hosts with Ansible"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

WinRM connection times out when Ansible tries to execute commands on Windows hosts.

```
FAILED! => {"msg": "winrm connection error: timed out"}
```

## Common Causes

- WinRM operation timeout too low
- Large data transfer over WinRM
- Windows host overloaded
- Network latency between controller and Windows host

## How to Fix

```ini
# ansible.cfg
[winrm]
operation_timeout_sec = 60
read_timeout_sec = 60
```

```yaml
# Per-host timeout settings
[win]
winserver ansible_host=10.0.0.50 ansible_winrm_operation_timeout_sec=120
```
