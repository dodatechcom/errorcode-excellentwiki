---
title: "[Solution] Ansible WinRM Connection Failed"
description: "Troubleshoot and fix WinRM connection failures for Windows hosts"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible cannot establish a WinRM connection to a Windows managed host.

```
UNREACHABLE! => {"msg": "winrm connection error: An existing connection was forcibly closed"}
```

## Common Causes

- WinRM not enabled on Windows host
- WinRM listener not configured for HTTPS
- Certificate issues
- Firewall blocking WinRM ports (5985/5986)
- Authentication method mismatch

## How to Fix

```powershell
# Run on Windows host as Administrator
Enable-PSRemoting -Force
Set-Item WSMan:\\localhost\\Service\\Auth\\Basic -Value $true
winrm set winrm/config/service '@{MaxConcurrentOperationsPerUser="5000"}'
```

```yaml
# Inventory for Windows
[win]
winserver ansible_host=10.0.0.50 ansible_port=5986 ansible_connection=winrm ansible_winrm_transport=basic
```
