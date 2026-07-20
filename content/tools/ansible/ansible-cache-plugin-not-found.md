---
title: "[Solution] Ansible Cache Plugin Not Found"
description: "Fix Ansible cache plugin configuration and availability errors"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible cannot find the specified cache plugin.

```
ERROR! Cache plugin 'redis' not found
```

## Common Causes

- Cache plugin not installed
- Plugin name incorrect
- Required Python libraries missing

## How to Fix

```bash
pip install redis
pip install python-memcached
```

```ini
[defaults]
fact_caching = jsonfile
fact_caching_connection = /tmp/ansible_cache
fact_caching_timeout = 3600
```

```bash
ansible-doc -t cache -l
ansible localhost -m setup --cache
```
