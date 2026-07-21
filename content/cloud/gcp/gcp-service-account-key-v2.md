---
title: "[Solution] GCP Service Account Key"
description: "SAKeyError for SA keys."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Service Account Key` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Key already exists with same name
- Key type (JSON/P12) invalid
- Key corrupted or expired

## How to Fix

### Create key

```bash
gcloud iam service-accounts keys create key.json --iam-account=mySA@project.iam.gserviceaccount.com
```

## Examples

- Example scenario: key already exists with same name
- Example scenario: key type (json/p12) invalid
- Example scenario: key corrupted or expired

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
