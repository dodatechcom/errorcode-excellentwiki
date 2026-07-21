---
title: "[Solution] GCP Workload Identity"
description: "WorkloadIdentityError for GKE WI."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Workload Identity` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- GSA not found
- KSA annotation missing
- IAM binding not set on GSA

## How to Fix

### Enable WI

```bash
gcloud container clusters update myCluster --workload-pool=myProject.svc.id.goog
```

## Examples

- Example scenario: gsa not found
- Example scenario: ksa annotation missing
- Example scenario: iam binding not set on gsa

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
