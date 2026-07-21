---
title: "[Solution] ScyllaDB Uptime Check Error"
description: "How to fix ScyllaDB uptime monitoring errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Scylla server restarting frequently
- OOM killer terminating process
- Configuration error causing crash loop

## How to Fix

```bash
nodetool info | grep -i uptime
```

## Examples

```bash
journalctl -u scylla-server --since "1 hour ago" | grep -i restart
```
