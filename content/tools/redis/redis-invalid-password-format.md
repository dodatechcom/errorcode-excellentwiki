---
title: "[Solution] Redis Invalid Password Format Error"
description: "How to fix Redis error when the password contains invalid characters or is malformed"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- Password contains special characters not properly escaped
- Password has leading or trailing whitespace
- Password was modified in redis.conf with encoding issues

## Fix

Use ACL to set password instead of redis.conf:

```bash
redis-cli ACL SETUSER default on >'p@ssw0rd!'
```

Verify the password in redis.conf:

```bash
grep requirepass /etc/redis/redis.conf
```

Reset password cleanly:

```bash
redis-cli CONFIG SET requirepass ""
redis-cli CONFIG SET requirepass "new_clean_password"
```

## Examples

```bash
# Test with quoted password
redis-cli -a 'my!p@ss#word' --no-auth-warning PING

# Verify current password works
redis-cli -a currentpass PING
```
