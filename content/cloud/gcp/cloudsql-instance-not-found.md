---
title: "[Solution] GCP Cloud SQL Instance Not Found"
description: "NOT_FOUND when the specified Cloud SQL instance does not exist."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Cloud SQL Instance Not Found` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Instance name is incorrect
- Instance was deleted
- Instance in different project
- Instance in different region

## How to Fix

### List instances

```bash
gcloud sql instances list
```
### Check instance

```bash
gcloud sql instances describe my-instance
```
### Create instance

```bash
gcloud sql instances create my-instance --database-version=MYSQL_8_0 --tier=db-f1-micro
```

## Examples

- Instance my-instance not found
- Instance deleted but connection string still references it

## Related Errors

- [Cloud SQL Error]({{< relref "/cloud/gcp/gcp-cloud-sql-error" >}}) -- General Cloud SQL errors
- [Backup Failed]({{< relref "/cloud/gcp/cloudsql-backup-failed" >}}) -- Backup failures
