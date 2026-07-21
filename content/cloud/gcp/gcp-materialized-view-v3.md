---
title: "[Solution] GCP Materialized View"
description: "MatViewError for materialized views."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Materialized View` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Base table changed without refresh
- View not fresh
- View query not supported

## How to Fix

### Refresh view

```bash
bq query 'ALTER MATERIALIZED VIEW myDataset.myView SET OPTIONS(enable_refresh=true)'
```

## Examples

- Example scenario: base table changed without refresh
- Example scenario: view not fresh
- Example scenario: view query not supported

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
