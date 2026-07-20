---
title: "[Solution] StorageClass not found"
description: "Fix Kubernetes StorageClass not found error. Resolve PVC creation failures when the referenced StorageClass does not exist."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## StorageClass Not Found

`storageclass.storage.k8s.io "<name>" not found`

This error occurs when a PersistentVolumeClaim references a StorageClass that does not exist in the cluster.

### Common Causes

- StorageClass name is misspelled
- StorageClass has not been created
- StorageClass was deleted
- Cluster does not have a default StorageClass

### How to Fix

List available StorageClasses:
```bash
kubectl get storageclass
```

Check the default StorageClass:
```bash
kubectl get storageclass -o jsonpath='{.items[?(@.metadata.annotations.storageclass\.kubernetes\.io/is-default-class=="true")].metadata.name}'
```

### Examples

```bash
# List StorageClasses
kubectl get storageclass
# gp2 (default)   kubernetes.io/aws-ebs
# standard        kubernetes.io/gce-pd
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})