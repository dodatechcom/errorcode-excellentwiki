---
title: "[Solution] ContainerCreating (Stuck)"
description: "Fix Kubernetes pods stuck in ContainerCreating state. Resolve issues when pods remain in ContainerCreating status during startup."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## ContainerCreating (Stuck)

This state means the pod has been scheduled to a node but the kubelet is still creating the container. While this is normal during startup, being stuck in this state for minutes indicates an underlying issue.

### Common Causes

- Image pull is slow (large image, slow registry, rate limited)
- Volume mount is pending (PVC not bound, NFS unreachable)
- Node resource pressure (CPU, memory, disk)
- Storage provisioning is slow (CSI driver, cloud volume attach)
- Network plugin (CNI) setup delays

### How to Fix

Check pod events:
```bash
kubectl describe pod <pod-name>
```

Check PVC binding:
```bash
kubectl get pvc
kubectl get pv
```

Check node conditions:
```bash
kubectl describe node <node-name>
```

### Examples

```bash
# Wait for pod with timeout
kubectl wait --for=condition=Ready pod/<pod-name> --timeout=300s

# Check pending PVC
kubectl get pvc
# my-claim    Pending
# Fix: ensure StorageClass exists and can provision volumes
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})