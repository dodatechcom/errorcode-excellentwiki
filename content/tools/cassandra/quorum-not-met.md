---
title: "[Solution] Cassandra - quorum not met"
description: "Understand and resolve the Cassandra 'quorum not met' error with causes, CQL fixes, and examples."
tools: ["cassandra"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

# Cassandra - quorum not met

The Cassandra `quorum not met` error can occur during database operations. This page explains what causes it and how to resolve it.

## What This Error Means

Encountering the `quorum not met` error in Cassandra indicates a problem that prevents normal database operations from completing successfully. Identifying the root cause quickly is key to minimizing downtime.

## Common Causes

- Configuration mismatch or missing setup
- Resource constraints or capacity limits
- Permission or authentication failures
- Query or syntax issues
- Concurrent access or lock contention

## How to Fix

### Check Configuration

Verify that all configuration settings related to this error are correct for your Cassandra environment. Review server logs for additional details.

### Verify Permissions

Ensure the connecting user or application has the necessary permissions to perform the requested operation in Cassandra.

### Review Resources

Check that sufficient resources (memory, disk space, connections) are available for the Cassandra instance.

```cql
-- Check system.log for error details
-- tail -f /var/log/cassandra/system.log
```

## Examples

A typical occurrence of the `quorum not met` error in Cassandra:

```cql
-- Example diagnostic query
SELECT * FROM system_schema.tables;
```

## Related Errors

- Related error in Cassandra
