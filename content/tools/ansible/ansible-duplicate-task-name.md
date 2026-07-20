---
title: "[Solution] Ansible Duplicate Task Name"
description: "Fix Ansible playbooks with duplicate task names that cause ambiguity"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible warns or fails when multiple tasks share the same name within a play.

```
WARNING: A duplicate named task was found. The task "Install package" is defined more than once.
```

## Common Causes

- Copy-paste errors
- Multiple includes defining same task names
- Role tasks conflicting with play tasks

## How to Fix

```yaml
# WRONG - duplicate task names
- name: Install package
  ansible.builtin.apt:
    name: nginx
- name: Install package
  ansible.builtin.apt:
    name: apache2

# CORRECT - unique names
- name: Install nginx
  ansible.builtin.apt:
    name: nginx
- name: Install apache2
  ansible.builtin.apt:
    name: apache2
```
