---
title: "[Solution] Kubernetes PVC Error — PersistentVolumeClaim pending"
description: "Fix Kubernetes PersistentVolumeClaim pending errors. Resolve PVC binding issues."
tools: ["kubernetes"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

A PersistentVolumeClaim (PVC) pending error means the PVC cannot be bound to a PersistentVolume. The pod referencing the PVC cannot start.

## Common Causes

- No PersistentVolume matches the PVC's access mode or storage class
- StorageClass does not exist or is misconfigured
- Storage capacity requested exceeds available PVs
- The cloud provider's storage quota is exceeded
- WaitForFirstConsumer binding mode with no scheduled pod

## How to Fix

### Check PVC Status

```bash
kubectl get pvc
kubectl describe pvc <pvc-name>
```

### Check Available PVs

```bash
kubectl get pv
```

### Verify StorageClass

```bash
kubectl get storageclass
```

### Create a Manual PV

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

### Check Cloud Storage Quota

```bash
# AWS
aws ec2 describe-volumes --filters Name=tag:Name,Values=kubernetes-dynamic-pv-*

# GCP
gcloud compute disks list
```

## Examples

```bash
# Example 1: PVC pending
kubectl get pvc
# NAME        STATUS   VOLUME   CAPACITY   ACCESS MODES
# my-pvc      Pending                             5Gi
# Fix: create a matching PV or StorageClass

# Example 2: StorageClass not found
kubectl describe pvc my-pvc
# Warning: storageclass "fast" not found
# Fix: kubectl get storageclass and use correct name
```

## Related Errors

- [Kubernetes Pending]({{< relref "/tools/kubernetes/k8s-pending" >}}) — pod stuck in Pending
- [Kubernetes Ingress Error]({{< relref "/tools/kubernetes/k8s-ingress-error" >}}) — Ingress controller error
