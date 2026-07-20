---
title: "[Solution] Ansible Fact Caching Disabled"
description: "Enable and configure Ansible fact caching for better performance"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible fact caching is not enabled, causing repeated fact gathering.

```
WARNING: Fact caching is disabled
```

## Common Causes

- fact_caching not set in ansible.cfg
- Cache plugin not configured
- Cache timeout set to 0

## How to Fix

```ini
# ansible.cfg - JSON file caching
[defaults]
fact_caching = jsonfile
fact_caching_connection = /tmp/ansible_facts_cache
fact_caching_timeout = 3600

# Redis-backed caching
[defaults]
fact_caching = redis
fact_caching_connection = localhost:6379:0
fact_caching_prefix = ansible_facts
```

```ini
# Memcached-backed caching
[defaults]
fact_caching = memcached
fact_caching_connection = localhost:11211
fact_caching_timeout = 7200
```
