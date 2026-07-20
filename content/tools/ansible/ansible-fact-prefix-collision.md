---
title: "[Solution] Ansible Fact Prefix Collision"
description: "Fix Ansible fact naming collisions between different modules"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible facts from different modules collide.

```
WARNING: Fact prefix collision: 'ansible_service_mgr' already set
```

## Common Causes

- Multiple modules setting same fact
- Custom module overwriting standard facts
- Fact priority conflicts

## How to Fix

```yaml
# Use unique fact names
- name: Set fact
  ansible.builtin.set_fact:
    myapp_service_manager: "systemd"  # Custom prefix

# Check existing facts before setting
- name: Show service manager
  ansible.builtin.debug:
    msg: "Service manager: {{ ansible_service_mgr }}"
```

# Safe naming convention
- name: Set app facts
  ansible.builtin.set_fact:
    myapp_{{ item.name }}_version: "{{ item.version }}"
  loop:
    - { name: nginx, version: "1.18" }
    - { name: postgresql, version: "13.0" }
```
