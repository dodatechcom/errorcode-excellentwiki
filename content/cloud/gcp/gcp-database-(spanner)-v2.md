---
title: "[Solution] GCP Database (Spanner)"
description: "SpannerDatabaseError for databases."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Database (Spanner)` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Database name taken within instance
- DDL statement invalid
- Database creation quota exceeded

## How to Fix

### Create database

```bash
gcloud spanner databases create myDB --instance=myInstance
```

## Examples

- Example scenario: database name taken within instance
- Example scenario: ddl statement invalid
- Example scenario: database creation quota exceeded

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
