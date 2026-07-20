---
title: "[Solution] Pod affinity or anti-affinity conflict"
description: "Fix Kubernetes pod affinity scheduling errors. Resolve pods that cannot be scheduled due to pod affinity or anti-affinity rules."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Pod Affinity / Anti-Affinity Conflict

This scheduling error occurs when the pod's affinity or anti-affinity rules cannot be satisfied by the current state of the cluster.

### Common Causes

- Pod affinity requires pods on the same node but no node has matching pods
- Pod anti-affinity prevents co-location on all available nodes
- RequiredDuringScheduling rules that cannot be met
- TopologyKey mismatch with node labels

### How to Fix

Check pod affinity rules:
```bash
kubectl get pod <pod-name> -o yaml | grep -A20 affinity
```

Relax anti-affinity from required to preferred:
```yaml
affinity:
  podAntiAffinity:
    preferredDuringSchedulingIgnoredDuringExecution: [...]
```

### Examples

```bash
# Check existing pods for anti-affinity conflicts
kubectl get pods -l app=myapp -o wide
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})