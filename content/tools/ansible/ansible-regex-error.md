---
title: "[Solution] Ansible Regex Template Error"
description: "Fix Ansible Jinja2 regex filter errors in templates and tasks"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible regex filter encounters an error during template evaluation.

```
ERROR! Jinja2 Template Error: bad escape in end of string
```

## Common Causes

- Invalid regex syntax
- Unescaped special characters
- Missing regex module

## How to Fix

```yaml
- name: Match pattern
  ansible.builtin.debug:
    msg: "{{ 'server1.example.com' is match('server.*\\.example\\.com') }}"

- name: Extract IP
  ansible.builtin.debug:
    msg: "{{ 'IP: 192.168.1.100' | regex_search('(\\d+\\.\\d+\\.\\d+\\.\\d+)') }}"

- name: Replace pattern
  ansible.builtin.debug:
    msg: "{{ 'Hello World' | regex_replace('World', 'Ansible') }}"
```
