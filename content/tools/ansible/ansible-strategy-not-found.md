---
title: "[Solution] Ansible Strategy Plugin Not Found"
description: "Fix Ansible strategy plugin configuration errors"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible cannot find the specified strategy plugin.

```
ERROR! the strategy 'free' could not be loaded
```

## Common Causes

- Strategy plugin not installed
- Typo in strategy name
- Strategy plugin incompatible with Ansible version
- Custom plugin not in plugin path

## How to Fix

```yaml
- name: Use linear strategy (default)
  hosts: all
  strategy: linear
  tasks:
    - name: Task 1
      ansible.builtin.debug:
        msg: "Running on {{ inventory_hostname }}"

- name: Use debug strategy
  hosts: all
  strategy: debug
```

```ini
[defaults]
strategy = linear
```
