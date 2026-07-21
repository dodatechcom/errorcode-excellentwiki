---
title: "[Solution] GCP Table Not Found (BQ)"
description: "TableNotFound (BigQuery) for tables."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Table Not Found (BQ)` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Table name incorrect
- Table deleted
- Time-partitioned table mismatch

## How to Fix

### Query table

```bash
bq query 'SELECT * FROM myDataset.myTable LIMIT 10'
```

## Examples

- Example scenario: table name incorrect
- Example scenario: table deleted
- Example scenario: time-partitioned table mismatch

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
