---
title: "[Solution] FailedMount"
description: "Fix Kubernetes FailedMount volume error. Resolve pod failures when volumes cannot be mounted to the container."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## FailedMount

This error occurs when the kubelet cannot mount a volume to the container. The pod may stay in ContainerCreating or crash.

### Common Causes

- PVC is not bound to a PV
- StorageClass does not exist or is not configured
- Volume driver (CSI) not installed
- NFS or network storage unreachable
- Volume already attached to another pod with ReadWriteOnce

### How to Fix

Check PVC status:
```bash
kubectl get pvc
kubectl describe pvc <name>
```

Check PV status:
```bash
kubectl get pv
kubectl describe pv <name>
```

Check StorageClass:
```bash
kubectl get storageclass
```

### Examples

```bash
# Check PVC binding
kubectl describe pvc my-claim
# Status:  Pending
# Events:  waiting for a volume to be created

# Check StorageClass provisioner
kubectl get storageclass
# gp2 (default)   kubernetes.io/aws-ebs
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})