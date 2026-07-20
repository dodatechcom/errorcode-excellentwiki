---
title: "[Solution] Ansible Import Role Not Found"
description: "Fix Ansible errors when imported roles are not found in the search path"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible cannot locate the specified role during playbook execution.

```
ERROR! the role 'nginx' was not found in /path/to/roles:/etc/ansible/roles
```

## Common Causes

- Role not installed via ansible-galaxy
- Incorrect role name
- roles_path not configured
- Role directory structure incorrect

## How to Fix

```bash
ansible-galaxy install nginx
ansible-config dump | grep roles_path
```

```ini
[defaults]
roles_path = ./roles:/etc/ansible/roles:/usr/share/ansible/roles
```

```yaml
# requirements.yml
---
roles:
  - name: nginx
    version: "3.1.0"
```
