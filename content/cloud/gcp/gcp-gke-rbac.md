---
title: "[Solution] GCP GKE RBAC"
description: "GKERBACError for RBAC."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `GKE RBAC` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- RoleBinding not found
- Subject kind mismatch (User vs ServiceAccount)
- ClusterRole missing

## How to Fix

### Apply RBAC

```bash
kubectl create clusterrolebinding myBinding --clusterrole=cluster-admin --serviceaccount=default:mySA
```

## Examples

- Example scenario: rolebinding not found
- Example scenario: subject kind mismatch (user vs serviceaccount)
- Example scenario: clusterrole missing

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
