---
title: "[Solution] Ansible Vault Secret Not Found"
description: "Fix Ansible vault errors when secrets cannot be located"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible vault cannot find the encrypted secret.

```
ERROR! The vault secret 'prod' was not found in the vault password files
```

## Common Causes

- Vault password file missing
- Vault secret not configured
- Wrong vault password file path

## How to Fix

```bash
echo "prod_password" > ~/.vault_prod
echo "dev_password" > ~/.vault_dev
chmod 600 ~/.vault_prod ~/.vault_dev
```

```ini
[defaults]
vault_identity_list = prod@~/.vault_prod,dev@~/.vault_dev
```

```bash
export ANSIBLE_VAULT_PASSWORD_FILE=~/.vault_${ENV}
ansible-playbook site.yml
```
