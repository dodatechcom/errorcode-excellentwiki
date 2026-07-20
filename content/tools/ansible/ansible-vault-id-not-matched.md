---
title: "[Solution] Ansible Vault ID Not Matched"
description: "Fix Ansible vault identity mismatch errors"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible vault ID does not match any configured vault identity.

```
ERROR! Vault password id 'prod' not found in vault identity list
```

## Common Causes

- Vault encrypted with different ID
- Vault identity not in ansible.cfg
- ID name typo

## How to Fix

```ini
# ansible.cfg
[defaults]
vault_identity_list = prod@~/.vault_prod,dev@~/.vault_dev
```

```bash
ansible-playbook site.yml --vault-id prod@prompt --vault-id dev@prompt
```

```yaml
- name: Deploy
  hosts: all
  vars_files:
    - name: vars/common.yml
    - name: vars/prod_secrets.yml
      vault_id: prod
```
