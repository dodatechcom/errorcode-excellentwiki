---
title: "[Solution] GCP Dataset Not Found"
description: "DatasetNotFound for BigQuery."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Dataset Not Found` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Dataset name incorrect
- Project mismatch
- Dataset deleted (2-day recovery)

## How to Fix

### List datasets

```bash
bq ls
```

## Examples

- Example scenario: dataset name incorrect
- Example scenario: project mismatch
- Example scenario: dataset deleted (2-day recovery)

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
