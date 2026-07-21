---
title: "[Solution] ClickHouse String Function Error"
description: "How to fix ClickHouse string function errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- String function argument wrong
- UTF-8 encoding issue
- String concatenation error

## How to Fix

```sql
SELECT concat('Hello', ' ', 'World');
```

## Examples

```sql
SELECT length('Hello'), upper('hello'), lower('HELLO'), trim('  hello  ');
```
