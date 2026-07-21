---
title: "[Solution] GCP Database (Firestore)"
description: "FirestoreDatabaseError for databases."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Database (Firestore)` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Database name already exists
- Location type (regional vs multi-region) mismatch
- App Engine app not in same region

## How to Fix

### Create database

```bash
gcloud firestore databases create --location=us-central1
```

## Examples

- Example scenario: database name already exists
- Example scenario: location type (regional vs multi-region) mismatch
- Example scenario: app engine app not in same region

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
