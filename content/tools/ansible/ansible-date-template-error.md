---
title: "[Solution] Ansible Date Template Error"
description: "Fix Ansible Jinja2 date formatting template errors"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible date formatting filter produces errors.

```
ERROR! Jinja2 Template Error: unsupported format character
```

## Common Causes

- Wrong date format syntax
- Missing date filter
- Non-date value passed to date filter

## How to Fix

```yaml
- name: Format current date
  ansible.builtin.debug:
    msg: "{{ ansible_date_time.iso8601 }}"

# Custom date format
- name: Custom format
  ansible.builtin.debug:
    msg: "{{ ansible_date_time.date }}"

# Use to_datetime filter
- name: Parse date
  ansible.builtin.debug:
    msg: "{{ '2024-01-15' | to_datetime('%Y-%m-%d') }}"
```
