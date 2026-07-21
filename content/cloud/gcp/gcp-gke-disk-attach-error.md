---
title: "[Solution] GCP GKE Disk Attach Error"
description: "Fix GKE disk attach errors. Resolve PersistentVolumeClaim, disk attachment, and StorageClass issues in Google Kubernetes Engine."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP GKE Disk Attach Error

The GKE Disk Attach error occurs when PersistentVolumeClaims cannot be attached to nodes due to disk state, zone, or quota issues.

## Common Causes

- Persistent disk is already attached to another instance
- Disk and node are in different availability zones
- Storage quota is exceeded for the project
- StorageClass provisioner is not installed
- Disk type is incompatible with the node machine type

## How to Fix

### 1. Check PVC status
```bash
kubectl get pvc -A
```

### 2. Check disk attachment
```bash
gcloud compute disks describe DISK_NAME --zone=ZONE \
  --format="yaml(status,users)"
```

### 3. Force detach disk
```bash
gcloud compute instances detach-disk VM_NAME \
  --disk=DISK_NAME \
  --zone=ZONE
```

### 4. Verify storage class
```bash
kubectl get storageclass
```

### 5. Create PVC with correct zone
```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: my-pvc
spec:
  accessModes:
  - ReadWriteOnce
  storageClassName: standard
  resources:
    requests:
      storage: 10Gi
```

## Examples

### Check disk quota
```bash
gcloud compute project-info describe --format="yaml(quotas)" \
  | grep -A2 "DISKS"
```

### List all persistent volumes
```bash
kubectl get pv -o custom-columns=\
"NAME:.metadata.name,CAPACITY:.spec.capacity.storage,STATUS:.status.phase,RECLAIM:.spec.persistentVolumeReclaimPolicy"
```

## Related Errors

- [GCP Disk Attach Error]({{< relref "/cloud/gcp/gcp-disk-attach-error" >}})
- [GCP CE Disk Not Found]({{< relref "/cloud/gcp/gcp-ce-disk-not-found" >}})
