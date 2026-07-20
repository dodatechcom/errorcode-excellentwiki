---
title: "[Solution] Redis MOVED Redirection Error"
description: "How to fix Redis MOVED redirection error when keys are on a different slot"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Common Causes

- Client does not support cluster protocol
- Hash slot calculation mismatch
- Keys migrated to different node during resharding
- Client cache of slot mappings is stale

## How to Fix

Use a Redis cluster-aware client:

```bash
# Python with redis-py cluster
from redis.cluster import RedisCluster
rc = RedisCluster(host='localhost', port=7001)
```

Check which node owns the slot:

```bash
redis-cli CLUSTER KEYSLOT mykey
redis-cli CLUSTER SLOTS
```

Use hash tags to keep keys in the same slot:

```bash
# Both keys will be in slot 2775
SET {user:1000}.name "John"
SET {user:1000}.email "john@example.com"
```

Update client cluster topology:

```bash
redis-cli CLUSTER SLOTS
```

## Examples

```bash
# Check slot for a key
redis-cli CLUSTER KEYSLOT mykey

# View slot to node mapping
redis-cli CLUSTER SLOTS

# Use hash tags
redis-cli SET {tag}.key1 value1
redis-cli SET {tag}.key2 value2
```
