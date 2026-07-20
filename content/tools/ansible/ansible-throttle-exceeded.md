---
title: "[Solution] Ansible Throttle Exceeded"
description: "Fix Ansible throttle limit exceeded errors in task execution"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible throttle limit is exceeded during task execution.

```
ERROR! Throttle limit exceeded for task
```

## Common Causes

- Throttle value exceeds available forks
- Too many concurrent tasks
- Resource exhaustion

## How to Fix

```yaml
- name: API calls with reduced concurrency
  hosts: all
  tasks:
    - name: Call API
      ansible.builtin.uri:
        url: "https://api.example.com/endpoint"
      throttle: 5

# Or increase forks in ansible.cfg
# [defaults]
# forks = 50
```
