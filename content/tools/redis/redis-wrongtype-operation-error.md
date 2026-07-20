---
title: "[Solution] Redis WRONGTYPE Operation Error"
description: "How to fix Redis WRONGTYPE error when operating on a key with wrong data type"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Common Causes

- Trying to use String commands on a Hash key
- Trying to use List commands on a Set key
- Key was overwritten with a different type
- Application logic error causing type mismatch

## How to Fix

Check the key type:

```bash
redis-cli TYPE mykey
```

Use type-appropriate commands:

```bash
# For Hash
redis-cli HGET mykey field

# For List
redis-cli LINDEX mykey 0

# For Set
redis-cli SMEMBERS mykey
```

Delete and recreate with correct type:

```bash
redis-cli DEL mykey
redis-cli HSET mykey field1 value1
```

Use OBJECT ENCODING to check internal type:

```bash
redis-cli OBJECT ENCODING mykey
```

## Examples

```bash
# Wrong - String command on Hash
redis-cli SET myhash key
redis-cli HGET myhash field
# WRONGTYPE Operation against a key holding the wrong kind of value

# Correct
redis-cli HSET myhash field value
redis-cli HGET myhash field
```
