---
title: "[Solution] Ansible String to Integer Conversion Error"
description: "Fix Ansible type conversion errors between strings and integers"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible fails to convert between string and integer types.

```
'string' object cannot be interpreted as an integer
```

## Common Causes

- Numeric value stored as string
- Jinja2 filter applied to wrong type
- Arithmetic on string values

## How to Fix

```yaml
- name: Convert string to int
  ansible.builtin.debug:
    msg: "{{ '42' | int }}"

- name: Add numbers
  ansible.builtin.debug:
    msg: "{{ (count_a | int) + (count_b | int) }}"

- name: Float conversion
  ansible.builtin.debug:
    msg: "{{ '3.14' | float }}"
```
