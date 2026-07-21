---
title: "[Solution] ScyllaDB Remove Node Error"
description: "How to fix ScyllaDB node removal errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Node not fully dead
- Too many nodes already removed
- Token ownership mismatch

## How to Fix

```bash
nodetool removenode UUID_OF_DEAD_NODE
```

## Examples

```bash
nodetool status | grep DN
```
