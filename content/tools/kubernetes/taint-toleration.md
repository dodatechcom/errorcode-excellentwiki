---
title: "[Solution] Node had taints that the pod did not tolerate"
description: "Fix Kubernetes taint and toleration scheduling errors. Resolve pods that cannot be scheduled due to node taints without matching tolerations."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Node Taints Not Tolerated

`0/4 nodes are available: 4 node(s) had untolerated taint`

This scheduling error occurs when all nodes have taints that the pod does not tolerate. Kubernetes uses taints and tolerations to control which pods can run on which nodes.

### Common Causes

- Node has a taint preventing general workload scheduling
- Pod is missing required tolerations
- Node was cordoned (tainted unschedulable)
- Workload intended for a different node pool
- Taint added for node maintenance

### How to Fix

List node taints:
```bash
kubectl describe nodes | grep -i taint
```

Add tolerations to the pod spec:
```yaml
tolerations:
- key: "dedicated"
  operator: "Equal"
  value: "gpu"
  effect: "NoSchedule"
```

Remove a taint:
```bash
kubectl taint nodes <node-name> key:NoSchedule-
```

### Examples

```bash
# Add toleration to deployment
kubectl patch deployment my-app -p '{"spec":{"template":{"spec":{"tolerations":[{"key":"dedicated","operator":"Equal","value":"gpu","effect":"NoSchedule"}]}}}}'
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})