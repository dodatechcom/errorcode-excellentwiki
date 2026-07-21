---
title: "[Solution] ScyllaDB Node Bootstrap Error"
description: "How to fix ScyllaDB node bootstrap errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Bootstrap token range overlap
- Existing nodes cannot stream to new node
- Disk space insufficient

## How to Fix

```bash
nodetool status
```

## Examples

```bash
journalctl -u scylla-server | grep -i bootstrap
```
