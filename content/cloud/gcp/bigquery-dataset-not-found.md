---
title: "[Solution] GCP BigQuery Dataset Not Found"
description: "NOT_FOUND when the specified dataset does not exist."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `BigQuery Dataset Not Found` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Dataset name is incorrect
- Dataset was deleted
- Dataset in different project
- Dataset not accessible to caller

## How to Fix

### List datasets

```bash
bq ls --project_id my-project
```
### Check dataset

```bash
bq show my-project:my-dataset
```
### Create dataset

```bash
bq mk --dataset my-project:my-dataset
```

## Examples

- Dataset my-dataset not found in project my-project
- Dataset deleted but query still references it

## Related Errors

- [BigQuery Error]({{< relref "/cloud/gcp/gcp-bigquery-error" >}}) -- General BigQuery errors
- [Table Not Found]({{< relref "/cloud/gcp/bigquery-table-not-found" >}}) -- Table not found
