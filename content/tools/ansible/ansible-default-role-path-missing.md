---
title: "[Solution] Ansible Default Role Path Missing"
description: "Fix Ansible errors when default role directories do not exist"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible cannot find the default role path.

```
ERROR! the role 'common' was not found in any of the known roles paths
```

## Common Causes

- Default roles_path does not exist
- Custom roles_path not configured
- Role directory permissions wrong

## How to Fix

```bash
mkdir -p ~/.ansible/roles
mkdir -p /etc/ansible/roles

# Or configure custom path
```

```ini
[defaults]
roles_path = ./roles:~/.ansible/roles:/usr/share/ansible/roles
```

```bash
ansible-config dump | grep roles_path
```
