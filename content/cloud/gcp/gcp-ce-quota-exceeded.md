---
title: "[Solution] GCP Compute Engine Quota Exceeded"
description: "QUOTA_EXCEEDED when the project quota limit is reached."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Compute Engine Quota Exceeded` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- vCPU quota for the region exceeded
- Instance group quota reached
- Disk quota exceeded
- GPU quota exhausted

## How to Fix

### Check quotas

```bash
gcloud compute project-info describe --format="table(quotas.metric,quotas.limit,quotas.usage)"
```
### Request quota increase

```bash
gcloud alpha service-quotas update my-project compute.googleapis.com/compute.googleapis.com/X --request-amount=100
```
### Check regional quotas

```bash
gcloud compute regions describe us-central1 --format="table(quotas.metric,quotas.limit,quotas.usage)"
```

## Examples

- Regional vCPU quota of 24 reached
- GPU quota of 8 exhausted by requesting 10

## Related Errors

- [GCP Compute Error]({{< relref "/cloud/gcp/gcp-compute-error" >}}) -- General Compute errors
- [Instance Not Found]({{< relref "/cloud/gcp/gcp-ce-instance-not-found" >}}) -- Instance not found
