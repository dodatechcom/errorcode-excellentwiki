---
title: "[Solution] PVC WaitForFirstConsumer"
description: "Fix Kubernetes PVC WaitForFirstConsumer mode. Resolve volume provisioning delays when using delayed volume binding."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## PVC WaitForFirstConsumer

`Status: Pending (WaitForFirstConsumer)`

This is not an error but a volume binding mode where the PVC stays Pending until a pod using it is created. The volume is provisioned in the same zone as the pod.

### Common Causes

- StorageClass uses volumeBindingMode: WaitForFirstConsumer
- No pod has been created to consume the PVC yet
- Normal behavior for topology-aware provisioning
- Pod scheduling constraints may cause provisioning delays

### How to Fix

This is expected behavior. Create a pod that uses the PVC:
```bash
kubectl create -f pod-with-pvc.yaml
```

If the PVC stays pending, check pod scheduling events:
```bash
kubectl describe pod <pod-name>
```

### Examples

```bash
# Check StorageClass binding mode
kubectl get sc <name> -o yaml | grep volumeBindingMode
# volumeBindingMode: WaitForFirstConsumer

# Create a pod to trigger volume provisioning
kubectl run test-pod --image=nginx --overrides='{"spec":{"volumes":[{"name":"data","persistentVolumeClaim":{"claimName":"my-pvc"}}],"containers":[{"name":"nginx","image":"nginx","volumeMounts":[{"name":"data","mountPath":"/data"}]}]}}'
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})