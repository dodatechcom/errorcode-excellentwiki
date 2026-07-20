---
title: "[Solution] Ansible Recursive Variable Reference"
description: "Fix Ansible circular variable references that cause infinite recursion"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible detects a recursive variable reference during template evaluation.

```
ERROR! A recursive loop was detected: var_a -> var_b -> var_a
```

## Common Causes

- Variable A references Variable B which references Variable A
- set_fact creating circular references
- Variable inheritance chain broken

## How to Fix

```yaml
# WRONG - circular reference
vars:
  app_name: "{{ project_name }}"
  project_name: "{{ app_name }}"

# CORRECT - break the cycle
vars:
  app_name: "my-application"
  project_name: "{{ app_name }}"
```
