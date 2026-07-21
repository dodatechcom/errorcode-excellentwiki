---
title: "[Solution] ClickHouse Remote Table Function Error"
description: "How to fix ClickHouse remote() table function errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Remote server unreachable
- Wrong port in remote connection
- Authentication failed on remote

## How to Fix

```sql
SELECT * FROM remote('remote-host:9000', 'mydb.mytable', 'myuser', 'password');
```

## Examples

```sql
SELECT count() FROM remote('host1,host2,host3', 'mydb.mytable');
```
