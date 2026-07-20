---
title: "[Solution] Ansible set_fact Cacheable Error"
description: "Fix Ansible set_fact cacheable parameter configuration issues"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible set_fact with cacheable parameter not working as expected.

```
ERROR! set_fact: cacheable must be a boolean value
```

## Common Causes

- cacheable value not boolean
- Fact caching not enabled
- Cache plugin not configured

## How to Fix

```yaml
- name: Set persistent fact
  ansible.builtin.set_fact:
    app_version: "1.2.3"
    cacheable: true
```

```ini
[defaults]
fact_caching = jsonfile
fact_caching_connection = /tmp/ansible_facts
fact_caching_timeout = 3600
```
