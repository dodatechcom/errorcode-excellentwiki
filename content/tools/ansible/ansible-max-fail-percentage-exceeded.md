---
title: "[Solution] Ansible Max Fail Percentage Exceeded"
description: "Fix Ansible max_fail_percentage threshold errors during rolling updates"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible rolling update stops because too many hosts have failed.

```
FAILED - max_fail_percentage reached, aborting playbook
```

## Common Causes

- max_fail_percentage set too low
- Too many hosts failing
- Infrastructure issue affecting multiple hosts

## How to Fix

```yaml
- name: Rolling update with higher threshold
  hosts: webservers
  serial: "25%"
  max_fail_percentage: 30
  tasks:
    - name: Update package
      ansible.builtin.apt:
        name: nginx
        state: latest

# Set to 0 for no tolerance
- name: Strict update
  hosts: webservers
  serial: 1
  max_fail_percentage: 0
  any_errors_fatal: true
```
