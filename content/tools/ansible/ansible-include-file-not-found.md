---
title: "[Solution] Ansible Include File Not Found"
description: "Fix Ansible errors when included task files do not exist"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible cannot find the file specified in an include_tasks or import_tasks directive.

```
ERROR! could not find file /path/to/tasks/missing_tasks.yml
```

## Common Causes

- File path typo
- Relative path resolution issues
- File not committed to version control
- Role path not configured correctly

## How to Fix

```yaml
- name: Include tasks
  ansible.builtin.include_tasks: "{{ role_path }}/tasks/main.yml"

- name: Conditional include with file check
  ansible.builtin.stat:
    path: "{{ playbook_dir }}/files/optional.conf"
  register: config_check
- name: Include optional configuration
  ansible.builtin.include_tasks: optional_config.yml
  when: config_check.stat.exists
```
