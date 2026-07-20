---
title: "[Solution] Ansible SSH Authentication Failed"
description: "Fix Ansible SSH authentication failures when connecting to managed nodes"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible cannot authenticate to the remote host using the provided credentials or SSH key.

```
UNREACHABLE! => {"msg": "Permission denied (publickey,password)"}
```

## Common Causes

- Incorrect SSH username
- Password mismatch or not provided
- SSH key not added to remote host
- Key file permissions too open
- Remote host password authentication disabled

## How to Fix

```yaml
# Inventory with explicit credentials
[webservers]
web1 ansible_host=192.168.1.100 ansible_user=admin ansible_ssh_private_key_file=~/.ssh/id_rsa

- hosts: webservers
  gather_facts: false
  tasks:
    - name: Test connection
      ansible.builtin.ping:
      vars:
        ansible_user: admin
        ansible_password: "{{ vault_ssh_password }}"
```
