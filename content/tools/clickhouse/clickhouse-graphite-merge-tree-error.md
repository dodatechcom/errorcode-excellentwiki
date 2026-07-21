---
title: "[Solution] ClickHouse GraphiteMergeTree Error"
description: "How to fix ClickHouse GraphiteMergeTree errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Graphite rollup config missing
- Time column not specified
- Rollup function not defined

## How to Fix

```xml
<graphite_rollup>
  <path_column>metric_name</path_column>
  <time_column>timestamp</time_column>
  <value_column>value</value_column>
  <version_column>version</version_column>
</graphite_rollup>
```

## Examples

```sql
SHOW CREATE TABLE mytable;
```
