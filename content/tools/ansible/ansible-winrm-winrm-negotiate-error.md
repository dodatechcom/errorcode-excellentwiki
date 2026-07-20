---
title: "[Solution] Ansible WinRM Negotiate Error"
description: "Fix WinRM negotiate authentication errors in Ansible Windows playbooks"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

WinRM negotiate authentication fails.

```
UNREACHABLE! => "winrm connection error: negotiate auth failed"
```

## Common Causes

- Kerberos not configured
- Time sync issues
- NTLM not enabled

## How to Fix

```yaml
[win]
winserver ansible_connection=winrm ansible_winrm_transport=ntlm ansible_user=administrator
```

```bash
sudo apt-get install krb5-user python3-winrm
```
