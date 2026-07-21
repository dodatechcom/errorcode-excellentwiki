---
title: "[Solution] ScyllaDB Connection Refused Error"
description: "How to fix ScyllaDB connection refused errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- ScyllaDB not running
- Wrong port (default 9042)
- Bind address restricting connections
- Firewall blocking port

## How to Fix

Check status:

```bash
sudo systemctl status scylla-server
nodetool status
```

Check listening ports:

```bash
ss -tlnp | grep 9042
```

## Examples

```bash
cqlsh localhost 9042
nodetool status
ss -tlnp | grep scylla
```
