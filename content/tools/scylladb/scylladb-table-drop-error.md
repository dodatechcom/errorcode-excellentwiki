---
title: "[Solution] ScyllaDB Table Drop Error"
description: "How to fix ScyllaDB DROP TABLE errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Table referenced by materialized view
- Table in use by transaction
- Schema agreement not reached

## How to Fix

```cql
DROP TABLE IF EXISTS mytable;
```

## Examples

```cql
DESCRIBE TABLE mytable;
```
