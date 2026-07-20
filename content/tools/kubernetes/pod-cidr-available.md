---
title: "[Solution] Pod CIDR not available"
description: "Fix Kubernetes pod CIDR allocation failures. Resolve pod creation failures when the pod IP range is exhausted."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Pod CIDR Not Available

`Failed to create pod: No IP addresses available in network <name>`

This error occurs when the cluster's pod network CIDR range has been fully allocated and no more IP addresses can be assigned to new pods.

### Common Causes

- Pod CIDR is too small for the number of pods
- Many terminated pods still holding IPs (IPAM cleanup delay)
- CNI plugin IPAM (host-local) IP release delay
- Node has exhausted its local pod IP range
- Cluster was created with a small pod CIDR

### How to Fix

List pods per node:
```bash
kubectl get pods -o wide | awk '{print $8}' | sort | uniq -c
```

Check CNI IPAM configuration:
```bash
kubectl get nodes -o jsonpath='{.items[0].spec.podCIDR}'
```

Delete terminated pods to release IPs:
```bash
kubectl delete pods --field-selector=status.phase=Succeeded
```

### Examples

```bash
# Check pod CIDR
kubectl get nodes -o jsonpath='{range .items[*]}{.metadata.name}{"	"}{.spec.podCIDR}{"
"}{end}'

# Release terminated pod IPs
kubectl delete pods --all-namespaces --field-selector=status.phase=Succeeded
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})