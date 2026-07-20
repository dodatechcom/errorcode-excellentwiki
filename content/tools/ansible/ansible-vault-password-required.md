---
title: "[Solution] Ansible Vault Password Required"
description: "Fix Ansible vault password prompt issues during playbook execution"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible prompts for vault password during execution.

```
Vault password:
```

## Common Causes

- Vault-encrypted variables in playbook
- No vault password file configured
- Password not provided via CLI

## How to Fix

```bash
ansible-playbook site.yml --ask-vault-pass
ansible-playbook site.yml --vault-password-file ~/.vault_pass
```

```ini
# ansible.cfg
[defaults]
vault_password_file = ~/.vault_pass
```

```bash
echo "MyStr0ngP@ssw0rd" > ~/.vault_pass
chmod 600 ~/.vault_pass
```
