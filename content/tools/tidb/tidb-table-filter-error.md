---
title: "[Solution] TiDB Lightning Table Filter Error"
description: "How to fix TiDB Lightning table filter errors"
tools: ["tidb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Filter syntax wrong
- Table not matching filter
- Exclude filter too broad

## How to Fix

```toml
[mydumper]
datasource-type = "file"
filter = ["mydb.mytable"]
```

## Examples

```bash
tiup tidb-lightning --filter='mydb.mytable'
```
