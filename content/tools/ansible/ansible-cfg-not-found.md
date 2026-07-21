---
title: "[Solution] Ansible Config File Not Found"
description: "Fix Ansible configuration file not found errors when ansible.cfg is missing or not discoverable."
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

# Ansible Config File Not Found

Ansible cannot locate an `ansible.cfg` configuration file and falls back to default settings unexpectedly.

```
[WARNING] No config file found; using defaults.
```

## Common Causes

- ansible.cfg does not exist in the expected search path
- File is in the wrong directory
- Permissions prevent reading the file
- Environment variable ANSIBLE_CONFIG points to wrong path
- Current working directory is incorrect

## How to Fix

### Generate Default Config

```bash
ansible-config init --disabled > ansible.cfg
```

### Specify Config Explicitly

```bash
ansible-playbook -i inventory.ini playbook.yml --config-file /path/to/ansible.cfg
```

### Check Config Search Order

```bash
# Ansible searches in this order:
# 1. ANSIBLE_CONFIG environment variable
# 2. ./ansible.cfg (current directory)
# 3. ~/.ansible.cfg (home directory)
# 4. /etc/ansible/ansible.cfg

# Verify which config is being used
ansible-config dump --config
```

### Set Environment Variable

```bash
export ANSIBLE_CONFIG=/home/admin/projects/ansible/ansible.cfg
```

## Examples

```bash
# Check current config search path
ansible-config view

# Dump all current settings
ansible-config dump

# List all configuration options
ansible-config list
```

```ini
# Minimal ansible.cfg
[defaults]
inventory = ./inventory
remote_user = deploy
host_key_checking = False

[privilege_escalation]
become = True
become_method = sudo
```
