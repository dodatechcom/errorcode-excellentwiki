---
title: "[Solution] Ansible Recursive Loop Detected"
description: "Fix Ansible recursive variable references and loops"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible detects an infinite loop or recursive reference during playbook execution.

```
ERROR! A recursive loop was detected: var_a -> var_b -> var_a
```

## Common Causes

- Variable A references Variable B which references Variable A
- include loop (playbook A includes B which includes A)
- When/loop creating infinite recursion

## How to Fix

```yaml
# WRONG - circular reference
vars:
  var_a: "{{ var_b }}"
  var_b: "{{ var_a }}"

# CORRECT - break the cycle
vars:
  var_a: "fixed_value"
  var_b: "{{ var_a }}"
```
