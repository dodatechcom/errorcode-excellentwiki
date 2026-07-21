---
title: "[Solution] GCP Query Execution Error"
description: "QueryExecutionError for BQ queries."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Query Execution Error` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Query syntax error
- Table not found in query
- JOIN requires equal join keys

## How to Fix

### Dry run query

```bash
bq query --dry_run 'SELECT 1'
```

## Examples

- Example scenario: query syntax error
- Example scenario: table not found in query
- Example scenario: join requires equal join keys

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
