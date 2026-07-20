---
title: "[Solution] Ansible Diff Mode Not Supported"
description: "Handle Ansible modules that do not support diff mode output"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible module does not support diff mode output.

```
FAILED! => {"msg": "diff mode is not supported for this task"}
```

## Common Causes

- Module does not implement diff support
- Complex operations without diff representation
- Custom module without diff output

## How to Fix

```yaml
- name: Apply configuration
  ansible.builtin.command: /opt/scripts/configure.sh
  diff: false

# Enable diff for templates
- name: Update nginx config
  ansible.builtin.template:
    src: nginx.conf.j2
    dest: /etc/nginx/nginx.conf
  diff: true
```
