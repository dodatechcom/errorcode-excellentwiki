---
title: "[Solution] Ansible Invalid YAML Syntax"
description: "Fix YAML syntax errors that prevent Ansible playbooks from parsing"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible cannot parse the playbook due to YAML syntax errors.

```
ERROR! We could not match supplied with a key on hosts
```

## Common Causes

- Incorrect indentation
- Missing colons after keys
- Unbalanced quotes
- Mixed tabs and spaces

## How to Fix

```yaml
# CORRECT YAML structure
---
- name: Example playbook
  hosts: all
  become: true
  tasks:
    - name: Install package
      ansible.builtin.apt:
        name: nginx
        state: present
```

```bash
python3 -c \"import yaml; yaml.safe_load(open('playbook.yml'))\"
ansible-lint playbook.yml
```
