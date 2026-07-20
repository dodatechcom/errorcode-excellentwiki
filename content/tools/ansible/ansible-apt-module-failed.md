---
title: "[Solution] Ansible apt Module Failed"
description: "Fix Ansible apt module errors on Debian/Ubuntu systems"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible apt module fails to manage packages on Debian/Ubuntu.

```
FAILED! => "Failed to update apt cache: E: Could not get lock"
```

## Common Causes

- Another process holding apt lock
- Package repository issues
- GPG key problems
- Disk space full

## How to Fix

```yaml
- name: Wait for apt lock
  ansible.builtin.wait_for:
    path: /var/lib/dpkg/lock-frontend
    timeout: 300

- name: Install package
  ansible.builtin.apt:
    name: nginx
    state: present
    update_cache: true
    cache_valid_time: 3600
```
