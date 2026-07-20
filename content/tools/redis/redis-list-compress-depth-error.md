---
title: "[Solution] Redis List Compress Depth Configuration Error"
description: "How to fix Redis list-compress-depth configuration errors"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- Compress depth set too high causing memory overhead
- Compression failing for certain data types
- Invalid compress depth value

## Fix

Check compress depth:

```bash
redis-cli CONFIG GET list-compress-depth
```

Set appropriate value:

```bash
# 0: disable compression (default)
redis-cli CONFIG SET list-compress-depth 0

# 1: compress all nodes except head and tail
redis-cli CONFIG SET list-compress-depth 1
```

Check encoding:

```bash
redis-cli OBJECT ENCODING mylist
```

## Examples

```bash
# Check compress depth
redis-cli CONFIG GET list-compress-depth

# Set compress depth
redis-cli CONFIG SET list-compress-depth 2

# Check encoding
redis-cli OBJECT ENCODING mylist
```
