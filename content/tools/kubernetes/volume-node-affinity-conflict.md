---
title: "[Solution] VolumeNodeAffinityConflict"
description: "Fix Kubernetes VolumeNodeAffinityConflict error. Resolve pod scheduling failures when volumes have node affinity constraints."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## VolumeNodeAffinityConflict

This error occurs when a pod requests a volume that has node affinity constraints and no available node matches both the pod's scheduling constraints and the volume's node affinity.

### Common Causes

- PV has node affinity for a specific zone or node
- The node with the PV data is unavailable or cordoned
- Volume is in a different availability zone

### How to Fix

Check PV node affinity:
```bash
kubectl get pv <name> -o yaml | grep -A10 nodeAffinity
```

List nodes in the required topology zone:
```bash
kubectl get nodes -l topology.kubernetes.io/zone=<zone>
```

### Examples

```bash
# View PV topology constraints
kubectl get pv pvc-xxxx -o yaml | grep -A5 "nodeAffinity"

# Schedule pod to correct zone
kubectl run my-app --image=nginx --overrides='{"spec":{"nodeSelector":{"topology.kubernetes.io/zone":"us-east-1a"}}}'
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})