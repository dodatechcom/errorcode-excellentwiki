---
title: "[Solution] GCP Instance Quota"
description: "InstanceQuotaError for CPU/instance limits."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Instance Quota` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- CPU quota exceeded in region
- Instance count quota hit
- Preemptible quota separate

## How to Fix

### Check quota

```bash
gcloud compute regions describe us-central1
```

## Examples

- Example scenario: cpu quota exceeded in region
- Example scenario: instance count quota hit
- Example scenario: preemptible quota separate

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
