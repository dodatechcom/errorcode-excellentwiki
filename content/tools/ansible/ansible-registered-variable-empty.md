---
title: "[Solution] Ansible Registered Variable Empty"
description: "Fix Ansible issues when registered variables contain unexpected empty values"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible registered variable is empty or missing expected content.

```
ERROR! 'stdout_lines' is undefined
```

## Common Causes

- Task output captured incorrectly
- Command produces no stdout
- Variable registered before task ran
- Conditional prevented task execution

## How to Fix

```yaml
- name: Run command
  ansible.builtin.command: echo "hello"
  register: result
  changed_when: false

- name: Check output
  ansible.builtin.debug:
    var: result.stdout_lines
  when: result.stdout_lines is defined

# Use default values
- name: Safe access
  ansible.builtin.debug:
    msg: "{{ result.stdout_lines | default(['no output']) }}"
```
