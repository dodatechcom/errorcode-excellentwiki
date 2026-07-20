---
title: "[Solution] Ansible Jinja2 Unexpected Closing Parenthesis"
description: "Fix Jinja2 syntax errors with unmatched parentheses in Ansible templates"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Jinja2 template has an unexpected closing parenthesis.

```
ERROR! Jinja2 Template Error: unexpected ')'
```

## Common Causes

- Extra closing parenthesis
- Missing opening parenthesis
- Parentheses in wrong position

## How to Fix

```yaml
# WRONG
- name: Bad template
  ansible.builtin.debug:
    msg: "{{ variable }})"

# CORRECT
- name: Good template
  ansible.builtin.debug:
    msg: "{{ variable }}"

# Complex expressions need matching parens
- name: Nested parens
  ansible.builtin.debug:
    msg: "{{ (var1 | int) + (var2 | int) }}"
```
