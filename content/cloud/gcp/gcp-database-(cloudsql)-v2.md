---
title: "[Solution] GCP Database (CloudSQL)"
description: "CloudSQLDatabaseError for databases."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Database (CloudSQL)` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Database name taken within instance
- Charset/collation not supported
- Database already deleted

## How to Fix

### Create database

```bash
gcloud sql databases create myDB --instance=myInstance
```

## Examples

- Example scenario: database name taken within instance
- Example scenario: charset/collation not supported
- Example scenario: database already deleted

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
