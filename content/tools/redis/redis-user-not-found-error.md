---
title: "[Solution] Redis ACL User Not Found Error"
description: "How to fix Redis ACL user not found errors"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- User does not exist in ACL
- Wrong username in AUTH command
- ACL file not loaded

## Fix

List all users:

```bash
redis-cli ACL LIST
```

Create user:

```bash
redis-cli ACL SETUSER newuser on >password ~* +@all
```

Check user permissions:

```bash
redis-cli ACL GETUSER newuser
```

Load ACL file:

```bash
redis-cli ACL LOAD
```

## Examples

```bash
# Check users
redis-cli ACL LIST

# Create user
redis-cli ACL SETUSER appuser on >apppass ~app:* +get +set +hset +hget

# Get user details
redis-cli ACL GETUSER appuser
```
