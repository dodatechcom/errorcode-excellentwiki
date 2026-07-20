---
title: "[Solution] Ansible Inventory Cache Expired"
description: "Fix Ansible inventory caching issues with dynamic inventory"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible dynamic inventory cache has expired or is invalid.

```
WARNING: Inventory cache expired, refreshing...
```

## Common Causes

- Cache timeout set too short
- Cache file corrupted
- Dynamic source changed while cache valid

## How to Fix

```ini
# ansible.cfg - inventory caching
[defaults]
cache = True
cache_connection = /tmp/ansible_inventory_cache
cache_timeout = 300  # 5 minutes

# For specific plugin
[inventory_plugins.aws_ec2]
cache = True
cache_timeout = 600
```

```bash
# Force cache refresh
ansible-inventory --refresh-cache -i aws_ec2.yml

# Clear cache manually
rm -f /tmp/ansible_inventory_cache*
```
