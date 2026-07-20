---
title: "[Solution] Ansible Throttle Limit Reached"
description: "Fix Ansible throttle limit configuration errors in task definitions"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible throttle limit has been exceeded or is invalid.

```
ERROR! the throttle value must be a positive integer, got 'abc'
```

## Common Causes

- Non-integer throttle value
- Throttle set to zero or negative
- Throttle exceeding available forks

## How to Fix

```yaml
- name: API calls with rate limiting
  hosts: all
  tasks:
    - name: Call external API
      ansible.builtin.uri:
        url: "https://api.example.com/data"
      throttle: 5
```
