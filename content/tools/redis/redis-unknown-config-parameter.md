---
title: "[Solution] Redis Unknown Config Parameter Error"
description: "How to fix Redis unknown configuration parameter errors"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Common Causes

- Typo in redis.conf parameter name
- Using config parameter from wrong Redis version
- Deprecated configuration option

## How to Fix

Check valid parameters:

```bash
redis-cli CONFIG GET *
```

Search documentation for correct parameter:

```bash
redis-cli CONFIG SET maxmemory 4gb  # valid
redis-cli CONFIG SET max_mem 4gb    # invalid: unknown config parameter
```

View current config file:

```bash
grep -v "^#" /etc/redis/redis.conf | grep -v "^$"
```

## Examples

```bash
# List all config parameters
redis-cli CONFIG GET * | head -20

# Test parameter
redis-cli CONFIG SET maxmemory-policy allkeys-lru

# Check parameter exists
redis-cli CONFIG GET maxmemory-policy
```
