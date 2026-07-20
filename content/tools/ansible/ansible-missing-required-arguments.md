---
title: "[Solution] Ansible Missing Required Arguments"
description: "Fix Ansible module errors due to missing required parameters"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible module fails because required arguments are not provided.

```
ERROR! this task 'ansible.builtin.apt' requires one of 'name', 'deb'
```

## Common Causes

- Required parameter not specified
- Variable used but undefined
- Incorrect parameter name

## How to Fix

```yaml
# WRONG
- name: Install package
  ansible.builtin.apt:
    state: present

# CORRECT
- name: Install package
  ansible.builtin.apt:
    name: nginx
    state: present
```
