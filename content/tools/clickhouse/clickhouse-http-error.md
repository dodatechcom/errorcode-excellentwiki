---
title: "[Solution] ClickHouse HTTP Interface Error"
description: "Fix ClickHouse HTTP interface errors when API requests fail"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse HTTP Interface Error

HTTP interface errors occur when ClickHouse HTTP API requests fail due to configuration or protocol issues.

## Common Causes

- ClickHouse HTTP port not configured or blocked
- Request body too large for HTTP buffer
- Authentication credentials missing or invalid
- CORS headers blocking browser requests

## How to Fix

Check HTTP interface:

```bash
curl http://localhost:8123/?query=SELECT+1
```

Check ClickHouse HTTP config:

```xml
<http_port>8123</http_port>
```

Test with authentication:

```bash
curl -u user:password 'http://localhost:8123/?query=SHOW+DATABASES'
```

## Examples

```bash
curl -X POST 'http://localhost:8123/' -d 'SELECT count() FROM system.tables'
```
