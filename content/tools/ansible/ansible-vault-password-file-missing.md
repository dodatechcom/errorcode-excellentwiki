---
title: "[Solution] Ansible Vault Password File Missing"
description: "Fix Ansible errors when vault password file is not found"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible cannot find the vault password file.

```
ERROR! The vault password file /path/to/.vault_pass was not found
```

## Common Causes

- File path incorrect
- File not created yet
- Permission denied
- Wrong working directory

## How to Fix

```bash
echo "MyStr0ngP@ssw0rd" > ~/.vault_pass
chmod 600 ~/.vault_pass
ls -la ~/.vault_pass
```

```ini
[defaults]
vault_password_file = ~/.vault_pass
```
