---
title: "[Solution] Kubernetes PVC — no PersistentVolume available"
description: "Fix Kubernetes PVC no PersistentVolume available. Resolve persistent volume claim binding failures."
tools: ["kubernetes"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["kubernetes", "pvc", "persistentvolume", "storage", "binding", "claim"]
weight: 5
---

A PVC error means the PersistentVolumeClaim cannot find a matching PersistentVolume to bind to. The pod remains in Pending state until a suitable volume becomes available.

## What This Error Means

When a PersistentVolumeClaim is created, Kubernetes attempts to bind it to an available PersistentVolume that matches the requested storage class, access mode, and capacity. If no suitable PersistentVolume exists or the StorageClass cannot dynamically provision one, the PVC stays in a `Pending` state. Any pod using this PVC will also be stuck in Pending.

## Common Causes

- No PersistentVolume exists with matching storage class
- StorageClass does not have a provisioner configured
- Storage capacity requested exceeds available storage
- Access mode mismatch (ReadWriteOnce vs ReadWriteMany)
- Dynamic provisioner for the storage class is not installed
- Cloud provider storage quota exceeded

## How to Fix

### Check PVC Status

```bash
kubectl get pvc <pvc-name>
kubectl describe pvc <pvc-name>
```

### Check Available PersistentVolumes

```bash
kubectl get pv
kubectl get storageclass
```

### Create a Matching PersistentVolume

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
  persistentVolumeReclaimPolicy: Retain
  hostPath:
    path: /mnt/data
```

### Fix StorageClass Provisioner

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: standard
provisioner: kubernetes.io/aws-ebs
parameters:
  type: gp2
reclaimPolicy: Retain
volumeBindingMode: Immediate
```

### Check Dynamic Provisioning

```bash
kubectl get events --field-selector reason=ProvisioningFailed
```

### Set Correct Access Mode

```yaml
spec:
  accessModes:
    - ReadWriteOnce  # Use RWO for single-node storage
  resources:
    requests:
      storage: 5Gi
```

## Related Errors

- [Kubernetes Pod Pending]({{< relref "/tools/kubernetes/k8s-pending-v2" >}}) — pod stuck in Pending
- [Kubernetes Node NotReady]({{< relref "/tools/kubernetes/k8s-node-not-ready-v2" >}}) — node unhealthy
- [AWS RDS Error]({{< relref "/cloud/aws/aws-rds-error-v2" >}}) — database connection failed
