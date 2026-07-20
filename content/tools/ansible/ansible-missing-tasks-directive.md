---
title: "[Solution] Ansible Missing Tasks Directive"
description: "Fix Ansible plays that are missing the tasks directive"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible playbook fails because no tasks are defined in a play.

```
ERROR! 'tasks' is not a valid attribute for a Play
```

## Common Causes

- Tasks keyword misspelled
- Roles-only play without tasks key
- Empty play definition

## How to Fix

```yaml
# CORRECT: Include tasks
- name: Setup web server
  hosts: webservers
  tasks:
    - name: Ensure nginx is installed
      ansible.builtin.apt:
        name: nginx
        state: present

# Roles-only play (valid without tasks)
- name: Setup web server
  hosts: webservers
  roles:
    - nginx
```
