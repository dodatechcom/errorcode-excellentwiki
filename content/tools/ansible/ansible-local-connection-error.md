---
title: "[Solution] Ansible Local Connection Error"
description: "Fix Ansible local connection plugin errors and issues"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible fails to execute tasks using the local connection plugin.

```
ERROR! [Exception]: AnsibleError('Unexpected failure during module execution.')
```

## Common Causes

- Missing local connection plugin
- Incorrect connection type specification
- Python interpreter mismatch
- Module not available on Ansible controller

## How to Fix

```yaml
- hosts: localhost
  connection: local
  gather_facts: false
  tasks:
    - name: Run local command
      ansible.builtin.command: echo \"hello\"
      delegate_to: localhost
```

```ini
# ansible.cfg
[defaults]
connection = local
```
