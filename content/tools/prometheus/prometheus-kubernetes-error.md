---
title: "[Solution] Prometheus Kubernetes SD Error"
description: "Fix Prometheus kubernetes sd errors. Learn why this happens and how to resolve it quickly."
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Prometheus Kubernetes SD Error

Prometheus Kubernetes service discovery errors occur when pod, service, or node discovery fails.

## Why This Happens

- RBAC permissions insufficient
- Namespace not found
- Pod not ready
- Label selector invalid

## Common Error Messages

- `k8s_sd_error`
- `k8s_sd_rbac_error`
- `k8s_sd_namespace_error`
- `k8s_sd_label_error`

## How to Fix It

### Solution 1: Check RBAC

Ensure Prometheus has proper permissions:

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
rules:
- apiGroups: [""]
  resources: ["pods", "services", "endpoints"]
  verbs: ["get", "list", "watch"]
```

### Solution 2: Verify namespace access

Check if the namespace exists and is accessible.

### Solution 3: Fix label selectors

Ensure label selectors match existing resources.


## Common Scenarios

- **RBAC denied:** Add proper ClusterRole permissions.
- **No targets discovered:** Check namespace and label selectors.

## Prevent It

- Verify RBAC
- Test selectors
- Monitor discovery
