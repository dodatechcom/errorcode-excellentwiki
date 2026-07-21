---
title: "[Solution] Vitess Tablet Connection Pool Error"
description: "Fix Vitess tablet connection pool exhaustion when backend MySQL connections are depleted"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vitess Tablet Connection Pool Error

Connection pool errors happen when vtgate exhausts available connections to a tablet, causing new queries to fail.

## Common Causes

- Connection pool size too small for workload
- Slow queries holding connections too long
- Backend MySQL max_connections reached
- Connection leak in application code

## How to Fix

Increase pool size in vtgate config:

```bash
vtgate -tablet_grpc_concurrency=20 -mysql_server_socket_path /tmp/mysql.sock
```

Check connection usage:

```sql
SHOW PROCESSLIST;
```

Kill stale connections:

```sql
SELECT CONCAT('KILL ', id, ';') FROM information_schema.processlist WHERE time > 300;
```

## Examples

```bash
vtctlclient GetTablet cell1-tablet-100
```
