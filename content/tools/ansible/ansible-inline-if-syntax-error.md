---
title: "[Solution] Ansible Inline If Syntax Error"
description: "Fix Jinja2 inline if (ternary) expression syntax errors in Ansible"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible Jinja2 inline if expression has incorrect syntax.

```
ERROR! Jinja2 Template Error: unexpected 'else'
```

## Common Causes

- Missing if keyword
- Missing else clause
- Wrong order of condition/value/else

## How to Fix

```yaml
# Jinja2 inline if syntax:
# {{ value_if_true if condition else value_if_false }}

# WRONG
- name: Bad ternary
  ansible.builtin.debug:
    msg: "{{ 'active' else 'inactive' if enabled }}"

# CORRECT
- name: Good ternary
  ansible.builtin.debug:
    msg: "{{ 'active' if enabled else 'inactive' }}"
```

```yaml
# Chained ternary
- name: Complex condition
  ansible.builtin.debug:
    msg: "{{ 'prod' if env == 'production' else ('staging' if env == 'staging' else 'dev') }}"
```
