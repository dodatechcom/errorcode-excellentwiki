---
title: "[Solution] Ansible Block Rescue Error"
description: "Fix Ansible block/rescue/always error handling patterns"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible block/rescue/always pattern has errors.

```
ERROR! Invalid block structure
```

## Common Causes

- Missing rescue or always block
- Tasks not inside block
- Nested block errors
- Variable scope in rescue

## How to Fix

```yaml
- name: Deploy with error handling
  hosts: webservers
  tasks:
    - name: Deploy application
      block:
        - name: Deploy code
          ansible.builtin.git:
            repo: https://github.com/example/app.git
            dest: /opt/app

        - name: Restart service
          ansible.builtin.service:
            name: nginx
            state: restarted
      rescue:
        - name: Rollback
          ansible.builtin.git:
            repo: https://github.com/example/app.git
            dest: /opt/app
            version: HEAD~1
      always:
        - name: Check status
          ansible.builtin.service:
            name: nginx
            state: started
```
