---
title: "[Solution] Node taint: dedicated for specific workloads"
description: "Fix Kubernetes dedicated node taint errors. Resolve pod scheduling failures on nodes tainted for specific workloads."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Dedicated Node Taint

`0/4 nodes are available: 2 node(s) had taint {node-role.kubernetes.io/master: }, 2 node(s) had taint {dedicated: gpu}`

This occurs when nodes have dedicated taints to reserve them for specific workloads and the pod does not have matching tolerations.

### Common Causes

- Nodes are tainted for dedicated workloads (GPU, storage, etc.)
- Master/control-plane nodes have NoSchedule taint
- Infrastructure nodes tainted for system components
- Pods need proper tolerations to use dedicated nodes

### How to Fix

List node taints:
```bash
kubectl get nodes -o jsonpath='{range .items[*]}{.metadata.name}{"	"}{.spec.taints[*].key}{":"}{.spec.taints[*].value}{":"}{.spec.taints[*].effect}{"
"}{end}'
```

Add tolerations to the pod:
```yaml
tolerations:
- key: "dedicated"
  operator: "Equal"
  value: "gpu"
  effect: "NoSchedule"
```

### Examples

```bash
# Add toleration to deployment for GPU nodes
kubectl patch deployment my-app -p '{"spec":{"template":{"spec":{"tolerations":[{"key":"nvidia.com/gpu","operator":"Exists","effect":"NoSchedule"}]}}}}'
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})