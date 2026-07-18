---
title: "[Solution] Kubectl PVC Pending - Fix PersistentVolumeClaim Pending"
description: "Fix Kubernetes PersistentVolumeClaim stuck in Pending state. Resolve storage class issues, volume provisioning, and binding failures."
tools: ["kubectl"]
error-types: ["pvc-pending"]
severities: ["warning"]
weight: 5
---

This error means a PersistentVolumeClaim (PVC) is stuck in the `Pending` state because a matching PersistentVolume (PV) cannot be provisioned or found.

## What This Error Means

When a PVC cannot bind to a volume, it remains in Pending:

```
kubectl get pvc
NAME       STATUS    VOLUME   CAPACITY   ACCESS MODES   STORAGECLASS   AGE
my-pvc     Pending                                      standard       5m
```

Pods that depend on this PVC will also remain pending because they cannot mount the volume.

## Why It Happens

- The StorageClass does not exist or is not configured
- The cloud provider's storage API is unreachable
- The requested capacity exceeds the maximum allowed by the storage class
- No available PersistentVolume matches the PVC's access mode or size
- The PVC specifies a StorageClass that no provisioner supports
- Quota limits prevent creating additional storage resources
- The PVC is in a namespace that the provisioner cannot access

## How to Fix It

### Check PVC events

```bash
kubectl describe pvc my-pvc
```

The Events section shows why binding is failing.

### Verify StorageClass exists

```bash
kubectl get storageclass
```

Ensure the StorageClass referenced in the PVC exists and has a valid provisioner.

### Check provisioner logs

```bash
kubectl logs -n kube-system -l app=ebs-csi-controller
```

Cloud storage provisioners may have errors in their logs.

### Ensure the PVC size is valid

```yaml
resources:
  requests:
    storage: 100Gi
```

Some storage classes have minimum or maximum size limits.

### Create a manual PV if needed

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: manual-pv
spec:
  capacity:
    storage: 10Gi
  accessModes:
    - ReadWriteOnce
  hostPath:
    path: /mnt/data
  persistentVolumeReclaimPolicy: Retain
```

### Check resource quotas

```bash
kubectl describe resourcequota -n <namespace>
```

Storage quotas may block PVC creation.

### Delete and recreate the PVC

```bash
kubectl delete pvc my-pvc
kubectl apply -f pvc.yaml
```

A fresh PVC sometimes resolves binding issues.

## Common Mistakes

- Not checking if the StorageClass exists before creating a PVC
- Forgetting that the provisioner must be running and healthy
- Not checking cloud provider quotas for storage
- Assuming PVCs automatically find existing PVs without matching access modes
- Not monitoring storage class provisioner health

## Related Pages

- [Kubectl Pod Pending]({{< relref "/tools/kubectl/kubectl-pod-pending" >}}) -- pod scheduling issues
- [Kubectl Node Not Ready]({{< relref "/tools/kubectl/kubectl-node-not-ready" >}}) -- node health
- [Kubectl RBAC Error]({{< relref "/tools/kubectl/kubectl-rbac-error" >}}) -- access control
