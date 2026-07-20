---
title: "[Solution] Ansible Module Non-Empty Warning"
description: "Address Ansible module warnings that may indicate configuration issues"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible module returns a non-empty warning message.

```
WARNING: Module returned non-empty warning
```

## Common Causes

- Module completed but with caveats
- Service installed but not started
- Configuration partially applied
- Deprecated feature usage

## How to Fix

```yaml
- name: Install and start nginx
  ansible.builtin.apt:
    name: nginx
    state: present
  register: nginx_install

- name: Display warnings
  ansible.builtin.debug:
    var: nginx_install.warnings
  when: nginx_install.warnings is defined

- name: Start nginx service
  ansible.builtin.service:
    name: nginx
    state: started
```
