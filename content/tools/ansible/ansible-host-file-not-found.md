---
title: "[Solution] Ansible Host File Not Found"
description: "Fix Ansible errors when the inventory host file is missing"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible cannot find the specified inventory or host file.

```
ERROR! Could not find inventory file /path/to/hosts
```

## Common Causes

- File path incorrect
- File not created
- File permissions wrong
- Working directory different

## How to Fix

```ini
# ansible.cfg
[defaults]
inventory = ./inventory/hosts
```

```bash
# Create inventory directory and file
mkdir -p inventory
cat > inventory/hosts << 'EOF'
[webservers]
web1 ansible_host=192.168.1.100

[dbservers]
db1 ansible_host=192.168.1.200
EOF

# Verify inventory
ansible-inventory --list
ansible-inventory --graph
```
