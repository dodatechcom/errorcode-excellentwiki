---
title: "[Solution] GCP BigQuery Table Not Found"
description: "NOT_FOUND when the specified table does not exist."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `BigQuery Table Not Found` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Table name is incorrect
- Table was deleted
- Table in different dataset
- Table not accessible to caller

## How to Fix

### List tables

```bash
bq ls my-project:my-dataset
```
### Check table

```bash
bq show my-project:my-dataset.my-table
```
### Create table

```bash
bq mk --table my-project:my-dataset.my-table schema.json
```

## Examples

- Table my-table not found in dataset my-dataset
- Table was deleted during dataset cleanup

## Related Errors

- [BigQuery Error]({{< relref "/cloud/gcp/gcp-bigquery-error" >}}) -- General BigQuery errors
- [Dataset Not Found]({{< relref "/cloud/gcp/bigquery-dataset-not-found" >}}) -- Dataset not found
