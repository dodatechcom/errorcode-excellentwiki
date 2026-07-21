---
title: "[Solution] ClickHouse Regex Error"
description: "How to fix ClickHouse regex matching errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Regex syntax wrong
- Regex too slow
- Regex not matching expected data

## How to Fix

```sql
SELECT match('Hello World', 'Hello.*');
```

## Examples

```sql
SELECT extractAll('abc123def456', '\\d+');
```
