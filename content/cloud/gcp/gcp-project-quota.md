---
title: "[Solution] GCP Project Quota"
description: "ProjectQuotaError for project-level quotas."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Project Quota` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Project creation quota exceeded (max 30)
- Resource manager quota limit hit
- Billing account not associated

## How to Fix

### Check projects

```bash
gcloud projects list
```

## Examples

- Example scenario: project creation quota exceeded (max 30)
- Example scenario: resource manager quota limit hit
- Example scenario: billing account not associated

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
