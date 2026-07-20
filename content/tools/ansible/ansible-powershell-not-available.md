---
title: "[Solution] Ansible PowerShell Not Available"
description: "Fix Ansible errors when PowerShell is not found on Windows hosts"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible cannot find PowerShell on the Windows host.

```
FAILED! => "PowerShell not found on remote host"
```

## Common Causes

- PowerShell not installed
- PowerShell not in PATH
- PowerShell execution policy restricted

## How to Fix

```powershell
Install-WindowsFeature -Name PowerShell -IncludeAllSubFeature
```

```yaml
- hosts: win
  vars:
    ansible_powershell_executable: "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"
  tasks:
    - name: Run PowerShell command
      ansible.windows.win_shell: Write-Output "Hello"
```
