---
title: "[Solution] Ansible Fact Merge Conflict"
description: "Fix Ansible fact merging conflicts when combining facts from multiple sources"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible encounters conflicts when merging facts from different sources.

```
ERROR! Conflicting fact 'ansible_default_ipv4' from multiple sources
```

## Common Causes

- Multiple fact sources overwriting same keys
- Custom facts conflicting with setup module
- set_fact overwriting gathered facts

## How to Fix

```yaml
- name: Deploy
  hosts: all
  gather_facts: true
  gather_subset:
    - "!all"
    - network
  tasks:
    - name: Add custom facts
      ansible.builtin.set_fact:
        custom_fact: "value"

# Merge facts safely
- name: Combine facts
  ansible.builtin.set_fact:
    combined_config: "{{ default_config | combine(custom_config | default({})) }}"
```
