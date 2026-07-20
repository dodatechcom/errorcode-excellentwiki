---
title: "[Solution] Ansible Recursive Import Error"
description: "Fix Ansible recursive import and include errors in playbooks"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible detects a recursive import or include pattern.

```
ERROR! Recursive include detected: playbook.yml -> tasks/main.yml -> playbook.yml
```

## Common Causes

- Playbook A imports Playbook B which imports Playbook A
- Role A depends on Role B which depends on Role A
- include_tasks creating circular reference

## How to Fix

```yaml
# Safe import structure
- import_playbook: site-common.yml
- import_playbook: site-web.yml
- import_playbook: site-db.yml

# site-web.yml
- hosts: webservers
  tasks:
    - import_tasks: tasks/install.yml
    - import_tasks: tasks/configure.yml
```
