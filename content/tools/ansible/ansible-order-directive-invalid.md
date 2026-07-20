---
title: "[Solution] Ansible Order Directive Invalid"
description: "Fix Ansible role include order configuration errors"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible encounters an invalid order directive in role includes.

```
ERROR! Invalid order value for role include: 'xyz'
```

## Common Causes

- Non-numeric order value
- Duplicate order values
- order used with the wrong include type

## How to Fix

```yaml
- name: Setup servers
  hosts: all
  roles:
    - role: base
      order: 1
    - role: common
      order: 2
    - role: nginx
      order: 3
```
