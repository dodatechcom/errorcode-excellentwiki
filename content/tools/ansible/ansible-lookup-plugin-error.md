---
title: "[Solution] Ansible Lookup Plugin Error"
description: "Fix Ansible lookup plugin errors when fetching external data"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible lookup plugin fails to retrieve data.

```
LookupError: [Errno 2] No such file or directory: '/path/to/file'
```

## Common Causes

- File path incorrect
- Network resource unavailable
- Authentication required for lookup
- Lookup plugin not installed

## How to Fix

```yaml
- name: Read file content
  ansible.builtin.debug:
    msg: "{{ lookup('ansible.builtin.file', '/path/to/file', errors='ignore') }}"

- name: Password lookup
  ansible.builtin.debug:
    msg: "{{ lookup('ansible.builtin.password', '/tmp/password.txt', length=20) }}"
```

```yaml
# Safe lookup with fallback
- name: Read optional config
  ansible.builtin.set_fact:
    config: "{{ lookup('ansible.builtin.file', '/etc/app/config', errors='ignore') | default('{}') }}"
```
