---
title: "[Solution] PersistentVolumeClaim not found"
description: "Fix Kubernetes PVC not found error. Resolve pod failures when a referenced PersistentVolumeClaim does not exist."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## PersistentVolumeClaim Not Found

`persistentvolumeclaim "<name>" not found`

This error occurs when a pod references a PersistentVolumeClaim that does not exist in the same namespace.

### Common Causes

- PVC name is misspelled in the pod spec
- PVC was deleted but pod still references it
- PVC is in a different namespace
- PVC hasn't been created yet

### How to Fix

List PVCs in the namespace:
```bash
kubectl get pvc
```

Create the PVC:
```bash
kubectl create -f pvc.yaml
```

### Examples

```bash
# List PVCs
kubectl get pvc --all-namespaces

# Create PVC from inline YAML
kubectl apply -f - <<EOF
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: my-claim
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 10Gi
EOF
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})