---
title: "[Solution] Topology spread constraints not met"
description: "Fix Kubernetes topology spread constraint scheduling errors. Resolve pods that cannot be scheduled due to topology spread rules."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Topology Spread Constraints Not Met

This scheduling error occurs when the pod's topology spread constraints cannot be satisfied. Pods must be distributed across topology domains but no suitable domain is available.

### Common Causes

- Constraints are too strict for the cluster topology
- Not enough nodes to distribute the desired number of pods
- maxSkew is set too low
- Too few topology zones available

### How to Fix

Increase maxSkew to allow more imbalance:
```yaml
topologySpreadConstraints:
  - maxSkew: 5
```

Relax from required to preferred:
```yaml
whenUnsatisfiable: ScheduleAnyway
```

### Examples

```bash
# View node topology zones
kubectl get nodes -o jsonpath='{range .items[*]}{.metadata.name}{"	"}{.metadata.labels.topology\.kubernetes\.io/zone}{"
"}{end}'
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})