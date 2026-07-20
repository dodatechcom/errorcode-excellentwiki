---
title: "[Solution] Ansible Parameter Type Mismatch"
description: "Fix Ansible module errors when parameter types do not match expected values"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible module receives a parameter of the wrong type.

```
ERROR! 'port' must be a string, got '<class int>'
```

## Common Causes

- Integer passed where string expected
- String passed where boolean expected
- List passed where string expected

## How to Fix

```yaml
- name: Configure service
  ansible.builtin.template:
    src: config.j2
    dest: /etc/app/config
    mode: '0644'  # string not integer

- name: Install package
  ansible.builtin.apt:
    name: nginx
    update_cache: true  # boolean not string
```
