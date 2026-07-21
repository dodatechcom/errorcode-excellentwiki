---
title: "[Solution] ScyllaDB Seastar Reactor Stall Error"
description: "How to fix ScyllaDB Seastar reactor stall errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Reactor blocked for too long
- Large allocation causing stall
- External system call blocking reactor

## How to Fix

```yaml
reactor-backend: epoll
```

## Examples

```bash
journalctl -u scylla-server | grep -i stall
```
