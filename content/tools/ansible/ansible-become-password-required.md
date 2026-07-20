---
title: "[Solution] Ansible Become Password Required"
description: "Fix Ansible privilege escalation password prompts during playbook execution"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible prompts for a become (sudo) password during execution, causing the playbook to hang or fail.

```
BECOME-password:\nfatal: [web1]: FAILED! => {"msg": "Incorrect become password"}
```

## Common Causes

- Become password not configured in inventory
- sudo requires TTY but none allocated
- sudo NOPASSWD not configured
- vault password not provided

## How to Fix

```yaml
[all:vars]
ansible_become=true
ansible_become_method=sudo
ansible_become_user=root
ansible_become_password="{{ vault_sudo_password }}"
```

```bash
echo \"ansible ALL=(ALL) NOPASSWD: ALL\" | sudo tee /etc/sudoers.d/ansible
```
