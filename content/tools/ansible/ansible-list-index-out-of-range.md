---
title: "[Solution] Ansible List Index Out of Range"
description: "Fix Ansible errors when accessing list elements beyond bounds"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible tries to access a list index that does not exist.

```
ERROR! list index out of range
```

## Common Causes

- List shorter than expected
- Index calculated incorrectly
- Loop variable exceeds bounds
- Variable not populated

## How to Fix

```yaml
- name: Get first element
  ansible.builtin.debug:
    msg: "{{ myList[0] | default('empty list') }}"

- name: Safe access
  ansible.builtin.debug:
    msg: "{{ myList[0] if myList | length > 0 else 'empty' }}"
```

```yaml
- name: Iterate safely
  ansible.builtin.debug:
    msg: "Item {{ idx }}: {{ item }}"
  loop: "{{ myList | default([]) }}"
```
