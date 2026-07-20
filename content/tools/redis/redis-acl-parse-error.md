---
title: "[Solution] Redis ACL Parse Error"
description: "How to fix Redis ACL configuration parsing errors"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- Invalid ACL syntax in redis.conf
- Wrong permission format
- Invalid channel pattern

## Fix

Check ACL file:

```bash
cat /etc/redis/users.acl
```

Test ACL command:

```bash
redis-cli ACL SETUSER testuser on >password ~* +@all
```

View current ACL:

```bash
redis-cli ACL LIST
```

Validate ACL syntax:

```bash
redis-cli ACL WHOAMI
redis-cli ACL LOG
```

## Examples

```bash
# Create user with correct ACL syntax
redis-cli ACL SETUSER myuser on >password123 ~data:* +get +set

# Check ACL errors
redis-cli ACL LOG

# List all users
redis-cli ACL LIST
```
