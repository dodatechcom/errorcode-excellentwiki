---
title: "[Solution] Ansible Handler Error"
description: "Fix Ansible handler notification and execution errors"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible handler fails to execute or is notified incorrectly.

```
ERROR! Handler "restart nginx" not found
```

## Common Causes

- Handler name typo
- Handler not defined in handlers section
- Handler in wrong file
- Notification name mismatch

## How to Fix

```yaml
# Define handler in handlers/main.yml
---
- name: restart nginx
  ansible.builtin.service:
    name: nginx
    state: restarted

# Notify with correct name
- name: Update config
  ansible.builtin.template:
    src: nginx.conf.j2
    dest: /etc/nginx/nginx.conf
  notify: restart nginx
```
