---
title: "[Solution] Ansible Fact Not Set Error"
description: "Fix Ansible errors when expected facts are not available on managed hosts"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible playbook fails because expected facts are not set on the target host.

```
ERROR! 'ansible_distribution' is undefined
```

## Common Causes

- gather_facts disabled
- Fact caching issues
- Custom module not returning expected facts
- Connection type does not support fact gathering

## How to Fix

```yaml
- name: Deploy with facts
  hosts: all
  gather_facts: true
  tasks:
    - name: Install package
      ansible.builtin.apt:
        name: nginx
      when: ansible_os_family == "Debian"

# Or set fallback
- name: Use facts with defaults
  ansible.builtin.debug:
    msg: "OS: {{ ansible_distribution | default('unknown') }}"
```
