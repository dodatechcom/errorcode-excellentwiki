---
title: "[Solution] ClickHouse Connection Refused Error"
description: "How to fix ClickHouse connection refused errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- ClickHouse server not running
- Wrong port (default 8123 HTTP, 9000 native)
- Bind address not allowing connections
- Firewall blocking port

## How to Fix

Check server status:

```bash
systemctl status clickhouse-server
curl http://localhost:8123/ping
```

Check listening ports:

```bash
ss -tlnp | grep clickhouse
```

## Examples

```bash
curl http://localhost:8123/ping
ss -tlnp | grep -E '(8123|9000)'
systemctl status clickhouse-server
```
