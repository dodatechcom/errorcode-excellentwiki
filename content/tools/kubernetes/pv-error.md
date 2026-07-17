---
title: "[Solution] Kubernetes Persistent Volume Error — PV/PVC error"
description: "Fix Kubernetes persistent volume errors. Resolve PV and PVC binding and access issues."
tools: ["kubernetes"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Kubernetes Persistent Volume Error — persistent volume error

Persistent volume errors occur when PersistentVolumeClaims (PVCs) cannot bind to PersistentVolumes (PVs) or when mounted volumes fail.

## Common Causes

- PVC and PV have mismatched access modes or storage class
- No available PV matches the PVC requirements
- Underlying storage is not provisioned correctly
- Volume is already bound to another claim

## How to Fix

### Check PVC Status

```bash
kubectl get pvc
```

### Check PV Status

```bash
kubectl get pv
```

### Describe PVC for Events

```bash
kubectl describe pvc <pvc-name>
```

### Create a PersistentVolume

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: my-pv
spec:
  capacity:
    storage: 10Gi
  accessModes:
    - ReadWriteOnce
  hostPath:
    path: /mnt/data
```

### Check StorageClass

```bash
kubectl get storageclass
```

### Delete Unbound PVC and Recreate

```bash
kubectl delete pvc <pvc-name>
kubectl apply -f pvc.yaml
```

## Examples

```bash
# Example 1: PVC pending
kubectl get pvc
# NAME        STATUS   VOLUME   CAPACITY   ACCESS MODES
# my-pvc      Pending
# Fix: create a matching PV

# Example 2: Access mode mismatch
kubectl describe pvc my-pvc
# Warning  ProvisioningFailed  access mode mismatch
# Fix: update PV accessModes to match PVC

# Example 3: Storage class not found
kubectl describe pvc my-pvc
# Warning  ProvisioningFailed  storageclass "fast" not found
# Fix: kubectl get storageclass (check available classes)
```

## Related Errors

- [Pending Pod]({{< relref "/tools/kubernetes/pending-pod" >}}) — pod stuck in Pending state
- [Node Not Ready]({{< relref "/tools/kubernetes/node-not-ready" >}}) — node not ready in cluster
