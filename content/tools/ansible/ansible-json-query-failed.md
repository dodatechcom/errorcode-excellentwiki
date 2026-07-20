---
title: "[Solution] Ansible json_query Filter Failed"
description: "Fix Ansible json_query filter errors when querying JSON data"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible json_query filter fails to parse or execute the query.

```
ERROR! Failed to evaluate json_query: jmespath.exceptions.ParseError
```

## Common Causes

- Invalid JMESPath syntax
- Missing community.general collection
- Query references non-existent path

## How to Fix

```bash
ansible-galaxy collection install community.general
```

```yaml
- name: Query JSON data
  ansible.builtin.debug:
    msg: "{{ data | community.general.json_query('servers[*].name') }}"

- name: Find active servers
  ansible.builtin.debug:
    msg: "{{ servers | community.general.json_query('[?status==`active`].name') }}"
```
