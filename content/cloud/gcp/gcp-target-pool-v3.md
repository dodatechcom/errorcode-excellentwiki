---
title: "[Solution] GCP Target Pool"
description: "TargetPoolError for target pools."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Target Pool` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Pool name taken
- Instances not healthy
- Session affinity config invalid

## How to Fix

### Create pool

```bash
gcloud compute target-pools create myPool --region=us-central1
```

## Examples

- Example scenario: pool name taken
- Example scenario: instances not healthy
- Example scenario: session affinity config invalid

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
