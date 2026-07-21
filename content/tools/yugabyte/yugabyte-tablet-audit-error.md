---
title: "[Solution] YugabyteDB Tablet Audit Error"
description: "How to fix YugabyteDB tablet audit logging errors"
tools: ["yugabyte"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Audit logging not enabled
- Audit log file not writable
- Audit log format wrong

## How to Fix

```bash
yb-tserver --enable_ysql_conn_mgr=true
```

## Examples

```bash
curl http://tikv-host:20180/debug/status
```
