---
title: "[Solution] Ansible Module Not Found"
description: "Fix Ansible module not found errors during playbook execution"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible cannot locate the specified module.

```
ERROR! no action detected in task, Ansible could not identify this 'module'
```

## Common Causes

- Module name typo
- Module requires additional collection
- Module from deprecated namespace
- Ansible version mismatch

## How to Fix

```yaml
# Use FQCN
- name: Install package
  ansible.builtin.apt:
    name: nginx
    state: present
```

```bash
ansible-galaxy collection install community.general
ansible-galaxy collection install community.docker
```
