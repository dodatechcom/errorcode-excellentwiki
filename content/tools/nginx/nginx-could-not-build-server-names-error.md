---
title: "[Solution] Nginx Could Not Build Server Names Error"
description: "Nginx failed to build the server names hash table, typically due to too many unique server names."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

Nginx failed to build the server names hash table, typically due to too many unique server names.

## Common Causes

- **Too many unique server names**
- **Server name hash bucket too small**
- **Wildcard conflicts**

## How to Fix

1. Increase hash: `server_names_hash_bucket_size 128;`
2. Or disable: `server_names_hash_max_size 4096; server_names_hash_bucket_size 128;`
3. Remove unused server names

## Examples

**Config:**
```nginx
http {
    server_names_hash_bucket_size 128;
    server_names_hash_max_size 4096;
    # ...
}
```