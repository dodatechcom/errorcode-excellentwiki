---
title: "[Solution] CockroachDB - range split"
description: "Understand and resolve the CockroachDB 'range split' error with causes, SQL fixes, and examples."
tools: ["cockroachdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

# CockroachDB - range split

The CockroachDB `range split` error can occur during database operations. This page explains what causes it and how to resolve it.

## What This Error Means

Encountering the `range split` error in CockroachDB indicates a problem that prevents normal database operations from completing successfully. Identifying the root cause quickly is key to minimizing downtime.

## Common Causes

- Configuration mismatch or missing setup
- Resource constraints or capacity limits
- Permission or authentication failures
- Query or syntax issues
- Concurrent access or lock contention

## How to Fix

### Check Configuration

Verify that all configuration settings related to this error are correct for your CockroachDB environment. Review server logs for additional details.

### Verify Permissions

Ensure the connecting user or application has the necessary permissions to perform the requested operation in CockroachDB.

### Review Resources

Check that sufficient resources (memory, disk space, connections) are available for the CockroachDB instance.

```sql
-- Check CockroachDB cluster settings
SHOW CLUSTER SETTINGS;
```

## Examples

A typical occurrence of the `range split` error in CockroachDB:

```sql
-- Example diagnostic query
SHOW TABLES;
```

## Related Errors

- Related error in CockroachDB
