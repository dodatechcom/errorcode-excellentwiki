---
title: "[Solution] Ansible Variable Type Conflict"
description: "Fix Ansible errors when variables have unexpected types"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible encounters unexpected variable types during operations.

```
ERROR! Unexpected type for variable: expected string, got list
```

## Common Causes

- Variable defined as list but used as string
- Extra-vars override changing type
- Variable inheritance type mismatch

## How to Fix

```yaml
- name: Safe type usage
  ansible.builtin.debug:
    msg: "Name: {{ app_name | string }}"

- name: Type checking
  ansible.builtin.debug:
    msg: "Type: {{ my_var | type_debug }}"

# Handle mixed types
- name: Process value
  ansible.builtin.debug:
    msg: >
      {% if my_var is iterable and my_var is not string %}
      {{ my_var | join(', ') }}
      {% else %}
      {{ my_var | string }}
      {% endif %}
```
