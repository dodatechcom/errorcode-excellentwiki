---
title: "[Solution] Ansible Group Recursion Detected"
description: "Fix Ansible circular group membership in inventory files"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible detects circular group membership.

```
ERROR! Circular group membership detected
```

## Common Causes

- Group A contains Group B which contains Group A
- Group inherits from itself
- Recursive children definition

## How to Fix

```ini
# WRONG - circular
[group_a:children]
group_b

[group_b:children]
group_a

# CORRECT - flat hierarchy
[production:children]
webservers
dbservers

[webservers]
web1
web2

[dbservers]
db1
db2

# Use :vars for shared variables
[production:vars]
env=production
```
