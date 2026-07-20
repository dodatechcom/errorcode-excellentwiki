---
title: "[Solution] Ansible WinRM Negotiate Auth Error"
description: "Fix WinRM negotiate authentication errors in Ansible Windows playbooks"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible WinRM connection fails with negotiate authentication errors.

```
UNREACHABLE! => "winrm connection error: negotiate auth failed"
```

## Common Causes

- Kerberos not configured on Ansible controller
- SPN (Service Principal Name) not set
- Time synchronization issues
- NTLM authentication not enabled

## How to Fix

```yaml
# Use NTLM instead of Kerberos
[win]
winserver ansible_connection=winrm ansible_winrm_transport=ntlm ansible_user=administrator
```

```bash
# Or install Kerberos
sudo apt-get install python3-winrm python3-requests-kerberos krb5-user
```
