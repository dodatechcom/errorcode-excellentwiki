---
title: "[Solution] ClickHouse Connection Refused Error"
description: "Fix ClickHouse connection refused errors when client cannot connect to server"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse Connection Refused Error

Connection refused errors occur when ClickHouse client cannot establish a connection to the server.

## Common Causes

- ClickHouse server not running
- Wrong port configured (default 9000 for TCP, 8123 for HTTP)
- Firewall blocking ClickHouse ports
- Bind address restricted to localhost only

## How to Fix

Check ClickHouse status:

```bash
systemctl status clickhouse-server
```

Check listening ports:

```bash
ss -tlnp | grep -E '8123|9000|9100'
```

Check bind address config:

```xml
<listen_host>0.0.0.0</listen_host>
```

Test connection:

```bash
clickhouse-client --query "SELECT 1"
```

## Examples

```bash
curl http://localhost:8123/?query=SELECT+1
```
