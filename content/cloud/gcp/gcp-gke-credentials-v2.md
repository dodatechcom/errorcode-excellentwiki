---
title: "[Solution] GCP GKE Credentials"
description: "GKECredentialError for kubeconfig."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `GKE Credentials` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Cluster not running
- Permission denied (roles/container.clusterAdmin)
- Legacy auth disabled

## How to Fix

### Get credentials

```bash
gcloud container clusters get-credentials myCluster
```

## Examples

- Example scenario: cluster not running
- Example scenario: permission denied (roles/container.clusteradmin)
- Example scenario: legacy auth disabled

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
