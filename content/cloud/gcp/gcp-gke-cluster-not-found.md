---
title: "[Solution] GCP GKE Cluster Not Found"
description: "GKEClusterNotFound for clusters."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `GKE Cluster Not Found` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Cluster name incorrect
- Cluster in wrong project
- Zone/region mismatch

## How to Fix

### List clusters

```bash
gcloud container clusters list
```

## Examples

- Example scenario: cluster name incorrect
- Example scenario: cluster in wrong project
- Example scenario: zone/region mismatch

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
