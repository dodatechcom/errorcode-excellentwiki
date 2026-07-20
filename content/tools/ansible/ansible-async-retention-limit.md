---
title: "[Solution] Ansible Async Retention Limit"
description: "Fix Ansible async job retention and cleanup issues"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible async job files exceed retention limits or are cleaned up prematurely.

```
WARNING: Async job files older than retention period have been cleaned up
```

## Common Causes

- Too many async jobs running simultaneously
- Default retention period too short
- Disk space issues

## How to Fix

```ini
[defaults]
async_dir = /tmp/.ansible_async
```

```yaml
# Clean up old async files
- name: Clean async files
  ansible.builtin.find:
    paths: /tmp/.ansible_async
    age: "7d"
  register: old_files

- name: Remove old files
  ansible.builtin.file:
    path: "{{ item.path }}"
    state: absent
  loop: "{{ old_files.files | default([]) }}"
```
