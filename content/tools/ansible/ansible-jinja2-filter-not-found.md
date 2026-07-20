---
title: "[Solution] Ansible Jinja2 Filter Not Found"
description: "Fix Ansible errors when using unavailable Jinja2 filters"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible encounters an unknown Jinja2 filter.

```
ERROR! 'json_query' is not a filter
```

## Common Causes

- Filter from uninstalled collection
- Filter name typo
- Filter requires additional Python library

## How to Fix

```bash
ansible-galaxy collection install community.general
ansible-doc -t filter -l
```

```yaml
- name: Query JSON
  ansible.builtin.debug:
    msg: "{{ data | community.general.json_query('servers[*].name') }}"
```

# Alternative: use built-in filters
- name: Filter list
  ansible.builtin.debug:
    msg: "{{ my_list | select('match', '^web') | list }}"
```
