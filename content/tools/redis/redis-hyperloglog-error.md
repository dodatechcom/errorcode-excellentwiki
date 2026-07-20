---
title: "[Solution] Redis HyperLogLog Error"
description: "How to fix Redis HyperLogLog merge and configuration errors"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- PFMERGE with wrong number of arguments
- Source keys do not exist
- Key exists but is not a HyperLogLog

## Fix

Verify key type:

```bash
redis-cli TYPE pfkey
redis-cli OBJECT ENCODING pfkey
```

Add elements before merging:

```bash
redis-cli PFADD pf1 "elem1" "elem2"
redis-cli PFADD pf2 "elem3" "elem4"
redis-cli PFMERGE pfmerged pf1 pf2
```

Check count:

```bash
redis-cli PFCOUNT pfmerged
```

## Examples

```bash
# Add elements
redis-cli PFADD unique_visitors "user1" "user2" "user3"

# Get count
redis-cli PFCOUNT unique_visitors

# Merge two HyperLogLogs
redis-cli PFMERGE merged pf1 pf2
```
