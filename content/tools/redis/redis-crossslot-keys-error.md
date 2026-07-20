---
title: "[Solution] Redis CROSSSLOT Keys Error"
description: "How to fix Redis CROSSSLOT error when multi-key operations span multiple slots"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Common Causes

- Keys in a multi-key operation are on different hash slots
- MGET, SUNION, and similar commands operating on keys in different slots
- No hash tag used to force keys into the same slot

## How to Fix

Use hash tags to ensure keys are in the same slot:

```bash
# Use {} hash tag
SET {user:1}.name "Alice"
SET {user:1}.email "alice@example.com"
MGET {user:1}.name {user:1}.email
```

Check which slots the keys belong to:

```bash
redis-cli CLUSTER KEYSLOT key1
redis-cli CLUSTER KEYSLOT key2
```

Move keys to same slot (requires migration):

```bash
redis-cli CLUSTER SETSLOT 1234 MIGRATING <target-node-id>
```

## Examples

```bash
# Check slots for multiple keys
redis-cli CLUSTER KEYSLOT user:1:name
redis-cli CLUSTER KEYSLOT user:1:email

# Use hash tags in commands
redis-cli MGET {user:1}.name {user:1}.email

# Check cluster topology
redis-cli CLUSTER SLOTS
```
