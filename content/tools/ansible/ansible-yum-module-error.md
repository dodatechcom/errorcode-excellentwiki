---
title: "[Solution] Ansible yum Module Error"
description: "Fix Ansible yum module errors on RHEL/CentOS systems"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible yum module fails to manage packages on RHEL/CentOS systems.

```
FAILED! => "Error: Unable to find a match: nginx"
```

## Common Causes

- Package not in enabled repositories
- EPEL not installed
- Repository metadata stale
- DNF/yum version mismatch

## How to Fix

```yaml
- name: Install EPEL
  ansible.builtin.yum:
    name: epel-release
    state: present

- name: Install nginx
  ansible.builtin.yum:
    name: nginx
    state: present

# Or use dnf on newer systems
- name: Install package
  ansible.builtin.dnf:
    name: nginx
    state: present
```
