---
title: "[Solution] Ansible Role Name Conflict"
description: "Fix Ansible role name conflicts between local and galaxy roles"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible encounters a role name conflict between local and installed roles.

```
WARNING: role 'common' found at both ./roles/common and /etc/ansible/roles/common
```

## Common Causes

- Same role name in local and global paths
- Role downloaded with conflicting name
- Role renamed locally

## How to Fix

```ini
# ansible.cfg - specify exact role path
[defaults]
roles_path = ./roles
```

# Use unique role names
# ./roles/app-common/
# ./roles/system-common/

# Or use namespace convention
# ./roles/mycompany.common/
# ./roles/mycompany.nginx/
```
