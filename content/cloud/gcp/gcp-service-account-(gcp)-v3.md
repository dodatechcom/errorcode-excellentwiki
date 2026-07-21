---
title: "[Solution] GCP Service Account (GCP)"
description: "ServiceAccountError for SA."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Service Account (GCP)` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- SA email already exists
- SA key quota (10) exceeded
- SA disabled or deleted

## How to Fix

### Create SA

```bash
gcloud iam service-accounts create mySA
```

## Examples

- Example scenario: sa email already exists
- Example scenario: sa key quota (10) exceeded
- Example scenario: sa disabled or deleted

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
