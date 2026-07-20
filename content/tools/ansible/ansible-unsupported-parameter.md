---
title: "[Solution] Ansible Unsupported Parameter"
description: "Fix Ansible errors when using parameters not supported by a module"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible module receives an unrecognized parameter.

```
ERROR! unsupported parameter for module: 'enable_ssl'
```

## Common Causes

- Parameter name typo
- Parameter from wrong module version
- Module version mismatch with documentation

## How to Fix

```yaml
# Check docs first: ansible-doc ansible.builtin.apt

# WRONG
- name: Install package
  ansible.builtin.apt:
    name: nginx
    enable_ssl: true  # Not valid

# CORRECT
- name: Install package
  ansible.builtin.apt:
    name: nginx
    state: present
```
