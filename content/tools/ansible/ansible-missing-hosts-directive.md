---
title: "[Solution] Ansible Missing Hosts Directive"
description: "Fix Ansible playbooks that are missing the required hosts directive"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible playbook fails because the hosts directive is missing from a play.

```
ERROR! playbooks must include a list of hosts
```

## Common Causes

- Typo in play structure
- hosts key omitted entirely
- Empty hosts value

## How to Fix

```yaml
# CORRECT
- name: Install web server
  hosts: webservers
  become: true
  tasks:
    - name: Install nginx
      ansible.builtin.apt:
        name: nginx
        state: present
```
