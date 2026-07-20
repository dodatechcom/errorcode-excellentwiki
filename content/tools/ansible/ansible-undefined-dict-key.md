---
title: "[Solution] Ansible Undefined Dictionary Key"
description: "Fix Ansible errors when accessing non-existent dictionary keys"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible tries to access a dictionary key that does not exist.

```
'dict object' has no attribute 'nonexistent'
```

## Common Causes

- Variable not populated
- Key name typo
- Nested key access without null check
- Variable scope issue

## How to Fix

```yaml
- name: Access key safely
  ansible.builtin.debug:
    msg: "Value: {{ my_dict.get('key', 'default_value') }}"

- name: Safe access with default
  ansible.builtin.debug:
    msg: "Value: {{ my_dict.key | default('fallback') }}"

- name: Check key existence
  ansible.builtin.debug:
    msg: "Has key: {{ 'key' in my_dict }}"
```
