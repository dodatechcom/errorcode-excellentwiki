---
title: "[Solution] Ansible Vault Decrypt Failed"
description: "Fix Ansible vault decryption failures during playbook execution"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible cannot decrypt vault-encrypted content.

```
ERROR! AnsibleVaultEncryptedUnicode has no attribute 'encrypt'
```

## Common Causes

- Wrong vault password
- Vault password changed
- File corrupted
- Multiple vault IDs mismatched

## How to Fix

```bash
ansible-vault decrypt secrets.yml --vault-password-file .vault_pass
ansible-vault encrypt secrets.yml --vault-password-file .new_vault_pass
ansible-vault view secrets.yml --vault-password-file .vault_pass
```

```bash
ansible-playbook site.yml --ask-vault-pass -vvv
```
