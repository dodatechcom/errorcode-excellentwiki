---
title: "[Solution] Ansible Linear Strategy Failure"
description: "Fix Ansible linear strategy execution failures in playbooks"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible linear strategy fails to execute tasks in order.

```
ERROR! Linear strategy failed: task execution order disrupted
```

## Common Causes

- Task ordering conflicts
- Role dependencies affecting order
- include_tasks changing execution order

## How to Fix

```yaml
- name: Ordered deployment
  hosts: all
  strategy: linear
  tasks:
    - name: Step 1 - Stop service
      ansible.builtin.service:
        name: nginx
        state: stopped

    - name: Step 2 - Update code
      ansible.builtin.git:
        repo: https://github.com/example/app.git
        dest: /opt/app

    - name: Step 3 - Start service
      ansible.builtin.service:
        name: nginx
        state: started
```
