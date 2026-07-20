---
title: "[Solution] Ansible Cache Timeout Error"
description: "Fix Ansible fact cache timeout configuration issues"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible cache timeout is set incorrectly or expired.

```
WARNING: Fact cache timeout expired
```

## Common Causes

- Cache timeout too short
- Cache timeout set to 0 (disabled)
- Clock sync issues

## How to Fix

```ini
[defaults]
fact_caching = jsonfile
fact_caching_connection = /tmp/ansible_cache
fact_caching_timeout = 3600  # 1 hour

# Disable timeout (cache forever)
# fact_caching_timeout = 0

# 24 hour cache
# fact_caching_timeout = 86400
```
