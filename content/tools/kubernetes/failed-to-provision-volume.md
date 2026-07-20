---
title: "[Solution] Failed to provision volume"
description: "Fix Kubernetes volume provisioning failures. Resolve PVC pending when the StorageClass provisioner cannot create the volume."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Failed to Provision Volume

`Failed to provision volume with StorageClass "<name>"`

This error occurs when the storage provisioner (EBS, GCE PD, Azure Disk) cannot create a persistent volume for a PVC.

### Common Causes

- Cloud provider API rate limiting
- Insufficient permissions to create volumes
- Volume type is not available in the region
- StorageClass parameters are invalid
- Cloud provider quota exceeded

### How to Fix

Check PVC events:
```bash
kubectl describe pvc <name>
```

Check StorageClass configuration:
```bash
kubectl describe storageclass <name>
```

Check cloud provider limits:
```bash
# AWS
aws ec2 describe-account-attributes
# GCP
gcloud compute regions describe <region>
# Azure
az vm list-usage --location <region>
```

### Examples

```bash
# Check PVC events for provisioning error
kubectl describe pvc my-claim | grep -A5 Events
#  Failed to provision volume: AccessDenied
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})