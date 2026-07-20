---
title: "[Solution] Ansible Any Errors Fatal Triggered"
description: "Fix Ansible any_errors_fatal configuration that stops playbook on first error"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible playbook stops immediately when any host encounters an error.

```
FATAL: any_errors_fatal triggered, aborting remaining hosts
```

## Common Causes

- any_errors_fatal: true set on play or task
- Critical task failure
- Infrastructure issue

## How to Fix

```yaml
- name: Deploy application
  hosts: webservers
  any_errors_fatal: false
  tasks:
    - name: Deploy with rescue
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
        - name: Rollback on failure
          ansible.builtin.git:
            repo: https://github.com/example/app.git
            dest: /opt/app
            version: HEAD~1
```
