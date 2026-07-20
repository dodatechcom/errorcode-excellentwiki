---
title: "[Solution] Ansible Serial Batch Too Small"
description: "Fix Ansible serial batch size configuration errors"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible serial batch is too small for effective deployment.

```
ERROR! Serial batch too small: 0 hosts selected
```

## Common Causes

- Serial value set to 0
- Serial value larger than available hosts
- Percentage calculation results in 0 hosts

## How to Fix

```yaml
- name: Rolling update
  hosts: webservers
  serial: 1
  tasks:
    - name: Update
      ansible.builtin.apt:
        upgrade: dist

# Multi-stage serial
- name: Progressive rollout
  hosts: webservers
  serial:
    - 1
    - "25%"
    - "50%"
    - "100%"
```
