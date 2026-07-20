---
title: "[Solution] Ansible Role Dependency Cycle"
description: "Fix circular role dependencies in Ansible playbooks and roles"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible detects a circular dependency between roles.

```
ERROR! Recursive include detected: role 'web' depends on 'common' which depends on 'web'
```

## Common Causes

- Role A depends on Role B which depends on Role A
- Meta dependencies creating infinite loops

## How to Fix

```yaml
# Break the dependency cycle
# roles/web/meta/main.yml
---
dependencies:
  - role: common

# roles/common/meta/main.yml
---
dependencies: []
```

# Flat dependency structure
- name: Full stack deployment
  hosts: all
  roles:
    - role: base
    - role: common
    - role: nginx
    - role: app
```
