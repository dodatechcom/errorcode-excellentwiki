---
title: "[Solution] Ansible WinRM Basic Auth Disabled"
description: "Enable basic authentication for WinRM in Ansible Windows management"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

WinRM connection fails because basic authentication is not enabled on the Windows host.

```
UNREACHABLE! => "Basic auth is not enabled or supported by the server"
```

## Common Causes

- Basic authentication disabled in WinRM configuration
- Group policy restricting auth methods
- WinRM service configuration does not allow basic auth

## How to Fix

```powershell
# On Windows host (run as Administrator)
winrm set winrm/config/service/auth '@{Basic="true"}'
winrm set winrm/config/service '@{AllowUnencrypted="true"}'
winrm get winrm/config/service/auth
```
