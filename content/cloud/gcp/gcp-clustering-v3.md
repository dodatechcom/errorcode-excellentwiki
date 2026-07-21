---
title: "[Solution] GCP Clustering"
description: "ClusteringError for clustered tables."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Clustering` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Clustering columns don't match schema
- Clustered column order mismatch
- Re-clustering already running

## How to Fix

### Check clustering

```bash
bq show myDataset.myTable
```

## Examples

- Example scenario: clustering columns don't match schema
- Example scenario: clustered column order mismatch
- Example scenario: re-clustering already running

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
