---
title: "[Solution] Ansible Fact Namespace Error"
description: "Fix Ansible fact namespacing and organization errors"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible encounters errors with fact namespacing.

```
ERROR! Fact 'ansible_os' conflicts with namespace 'ansible'
```

## Common Causes

- Custom facts using ansible_ prefix
- Fact naming collision
- Deprecated fact namespacing

## How to Fix

```yaml
# Use custom namespace for custom facts
- name: Set custom fact
  ansible.builtin.set_fact:
    custom_app_version: "1.0.0"  # Don't use ansible_ prefix

# Access with proper namespace
- name: Show facts
  ansible.builtin.debug:
    msg: "App version: {{ custom_app_version }}"
```
