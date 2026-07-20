---
title: "[Solution] Pod anti-affinity rules preventing scheduling"
description: "Fix Kubernetes pod anti-affinity rules that prevent all pods from being scheduled. Resolve when anti-affinity is too strict."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Pod Anti-Affinity Preventing Scheduling

This error occurs when pod anti-affinity rules are too strict and prevent any new pods from being scheduled.

### Common Causes

- requiredDuringScheduling anti-affinity with no overlap allowed
- Too many pods already running that match the anti-affinity
- Insufficient nodes to spread pods according to anti-affinity
- Same topology key on too few nodes
- Rolling update creates new pods before old ones are removed

### How to Fix

Change required to preferred:
```yaml
affinity:
  podAntiAffinity:
    preferredDuringSchedulingIgnoredDuringExecution:
    ...
```

Increase the topology key scope:
```yaml
topologyKey: "topology.kubernetes.io/zone"  # instead of kubernetes.io/hostname
```

### Examples

```bash
# Change anti-affinity from required to preferred
kubectl patch deployment my-app --type=json -p='[{"op": "replace", "path": "/spec/template/spec/affinity/podAntiAffinity/requiredDuringSchedulingIgnoredDuringExecution", "value": null}]'
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})