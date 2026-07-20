---
title: "[Solution] kubectl drain failed"
description: "Fix 'kubectl drain' errors. Resolve node drain failures when evicting pods for maintenance."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Drain Failed

`error: unable to drain node "<node>" due to <reason>`

This error occurs when `kubectl drain` cannot evict pods from a node. Draining is required before node maintenance or removal.

### Common Causes

- PodDisruptionBudget (PDB) prevents eviction
- DaemonSet pods cannot be evicted (need --ignore-daemonsets)
- Pods with emptyDir volumes (need --delete-emptydir-data)
- Unmanaged pods not part of a controller

### How to Fix

Use drain with appropriate flags:
```bash
kubectl drain <node> --ignore-daemonsets --delete-emptydir-data --force
```

Check PDBs:
```bash
kubectl get pdb --all-namespaces
```

### Examples

```bash
# Drain node with all options
kubectl drain node-3 --ignore-daemonsets --delete-emptydir-data --grace-period=120

# Check PDB blocking drain
kubectl get pdb --all-namespaces | grep -v "Allowed disruption.*>="
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})