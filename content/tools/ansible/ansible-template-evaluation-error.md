---
title: "[Solution] Ansible Template Evaluation Error"
description: "Fix Ansible Jinja2 template evaluation errors during variable resolution"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible fails to evaluate a Jinja2 template expression.

```
ERROR! Template syntax error: unexpected '/'
```

## Common Causes

- Invalid Jinja2 syntax
- Division by zero in template
- Undefined variable in template
- Missing closing brackets

## How to Fix

```yaml
- name: Display message
  ansible.builtin.debug:
    msg: "Count is {{ item_count | default(0) }}"

# Escape special characters
- name: Use literal braces
  ansible.builtin.debug:
    msg: "Literal brace: {{ '{{' }} and {{ '}}' }}"
```
