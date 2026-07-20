---
title: "[Solution] Ansible WinRM Basic Auth Disabled"
description: "Enable basic authentication for WinRM in Ansible Windows management"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

WinRM rejects basic authentication.

```
UNREACHABLE! => "Basic auth is not enabled"
```

## Common Causes

- Basic auth disabled on Windows host
- Group policy restrictions
- WinRM misconfiguration

## How to Fix

```powershell
winrm set winrm/config/service/auth '@{Basic="true"}'
winrm set winrm/config/service '@{AllowUnencrypted="true"}'
```

```yaml
[win]
winserver ansible_connection=winrm ansible_winrm_transport=basic
```
