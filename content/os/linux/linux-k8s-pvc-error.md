---
title: "[Solution] k8s: PVC Pending — PersistentVolumeClaim Stuck"
description: "Fix Kubernetes PersistentVolumeClaim Pending errors. Resolve PVC binding failures, StorageClass issues, and dynamic provisioning problems."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# k8s: PVC Pending — PersistentVolumeClaim Stuck

A PersistentVolumeClaim in Pending status means Kubernetes cannot bind it to a PersistentVolume. The status shows:

> "Pending" in `kubectl get pvc`

Events show:

> "waiting for a volume to be created, either by external provisioner \"ebs.csi.aws.com\" or manually created by system administrator"

## What This Error Means

PVCs request storage from the cluster. In dynamic provisioning, a StorageClass provisions a PersistentVolume automatically. When the provisioner cannot create a volume — due to missing StorageClass, cloud quota exceeded, or misconfiguration — the PVC stays in Pending.

## Common Causes

- StorageClass does not exist or has wrong provisioner
- No available PersistentVolumes matching the PVC's access mode or size
- Cloud provider quota exceeded (e.g., EBS volume limit)
- CSI driver not installed or not running
- PVC requests access mode not supported by the StorageClass
- Dynamic provisioner not configured

## How to Fix

### Check PVC Status

```bash
kubectl get pvc
kubectl describe pvc <pvc-name>
```

### Check StorageClass

```bash
kubectl get storageclass
kubectl describe storageclass <sc-name>
```

### Create a PVC with Correct StorageClass

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: my-pvc
spec:
  accessModes:
    - ReadWriteOnce
  storageClassName: gp3
  resources:
    requests:
      storage: 10Gi
```

### Check Cloud Quota

```bash
# AWS
aws ec2 describe-volumes --filters "Name=status,Values=available"

# Check account limits
aws service-quotas get-service-quota --service-code ec2 --quota-code L-D18FCD1D --region us-east-1
```

### Install CSI Driver

```bash
# AWS EBS CSI Driver
kubectl apply -k "github.com/kubernetes-sigs/aws-ebs-csi-driver/deploy/kubernetes/overlays/stable/?ref=release-1.25"

# Check CSI pods
kubectl get pods -n kube-system -l app=csi-ebs-plugin
```

### Use Manual Binding

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: my-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 10Gi
  volumeName: pv-manually-created
  storageClassName: ""
```

## Related Errors

- [k8s Pod Pending]({{< relref "/os/linux/linux-k8s-pending" >}}) — Pod scheduling failures
- [k8s Node NotReady]({{< relref "/os/linux/linux-k8s-node-not-ready" >}}) — Node readiness issues
- [Disk Full]({{< relref "/os/linux/no-space-left" >}}) — Host disk space issues
