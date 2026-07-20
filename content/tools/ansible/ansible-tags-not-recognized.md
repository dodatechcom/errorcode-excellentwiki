---
title: "[Solution] Ansible Tags Not Recognized"
description: "Fix Ansible tag configuration errors in playbooks and roles"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible cannot recognize or match the specified tags.

```
ERROR! No matches found for the tag 'deploy' in the playbook
```

## Common Causes

- Tag name typo
- Tag applied to wrong element
- Using tags with import (not supported)
- Tag name with invalid characters

## How to Fix

```yaml
- name: Deploy application
  hosts: all
  tasks:
    - name: Install dependencies
      ansible.builtin.apt:
        name: "{{ item }}"
      tags:
        - install
    - name: Deploy code
      ansible.builtin.git:
        repo: https://github.com/example/app.git
        dest: /opt/app
      tags:
        - deploy

# Run: ansible-playbook site.yml --tags "deploy"
```
