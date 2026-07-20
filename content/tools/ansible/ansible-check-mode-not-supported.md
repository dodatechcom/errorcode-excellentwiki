---
title: "[Solution] Ansible Check Mode Not Supported"
description: "Handle Ansible modules that do not support check mode (dry run)"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible module does not support check mode (dry run).

```
FAILED! => {"msg": "check mode is not supported for this task"}
```

## Common Causes

- Module implemented without check_mode support
- Custom module lacking check mode logic
- Certain operations cannot be previewed

## How to Fix

```yaml
- name: Run destructive task
  ansible.builtin.command: /opt/scripts/migrate_db.sh
  check_mode: false

# Or use when condition
- name: Apply changes
  ansible.builtin.command: /opt/scripts/migrate_db.sh
  when: not ansible_check_mode
```
