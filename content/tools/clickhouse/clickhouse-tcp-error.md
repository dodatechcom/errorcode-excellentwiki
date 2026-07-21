---
title: "[Solution] ClickHouse TCP Interface Error"
description: "Fix ClickHouse TCP native protocol errors when client connections fail"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse TCP Interface Error

TCP interface errors occur when ClickHouse native TCP connections cannot be established.

## Common Causes

- TCP port blocked by firewall
- ClickHouse server not listening on expected port
- Client using wrong protocol version
- Max concurrent TCP connections exceeded

## How to Fix

Check TCP port:

```bash
ss -tlnp | grep 9000
```

Check max connections:

```sql
SELECT value FROM system.settings WHERE name = 'max_concurrent_queries';
```

Increase connection limit:

```xml
<max_concurrent_queries>200</max_concurrent_queries>
```

Test TCP connection:

```bash
clickhouse-client --query "SELECT 1"
```

## Examples

```bash
clickhouse-client -h localhost -p 9000 -u user --password pass
```
