---
title: "[Solution] Ansible Free Strategy Not Compatible"
description: "Fix Ansible free strategy compatibility issues in playbooks"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible free strategy is not compatible with certain playbook features.

```
ERROR! 'free' strategy is not compatible with 'serial'
```

## Common Causes

- Using free strategy with serial
- Using free strategy with rescue/always blocks
- Incompatible role features

## How to Fix

```yaml
# Free strategy without serial
- name: Independent execution
  hosts: all
  strategy: free
  tasks:
    - name: Run independently
      ansible.builtin.command: /opt/scripts/setup.sh

# Use linear with serial
- name: Rolling update
  hosts: webservers
  strategy: linear
  serial: 2
```
