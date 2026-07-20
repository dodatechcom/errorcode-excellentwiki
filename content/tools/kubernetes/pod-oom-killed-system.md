---
title: "[Solution] System OOM killed (node-level)"
description: "Fix Kubernetes node-level OOM kills. Resolve issues where the Linux OOM killer terminates processes when the node runs out of memory."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## System OOM Killed (Node-Level)

`oom_kill_process: Kill process <pid> (<name>) score <n> or a child of cgroup`

This is a node-level event where the Linux OOM killer terminates processes because the entire node is out of memory.

### Common Causes

- Node memory is overcommitted by pods
- No resource limits set on memory-hungry pods
- BestEffort pods consuming all available memory

### How to Fix

Check node memory:
```bash
kubectl top node <node-name>
```

Check pod memory usage:
```bash
kubectl top pods --all-namespaces --sort-by=memory | head -10
```

### Examples

```bash
# Find top memory consumers
kubectl top pods --all-namespaces --sort-by=memory | head -10

# Check for OOM kills in kernel logs
ssh <node> sudo dmesg | grep -i "oom_kill"
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})