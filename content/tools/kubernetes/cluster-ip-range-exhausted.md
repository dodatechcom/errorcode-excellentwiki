---
title: "[Solution] Cluster IP range exhausted"
description: "Fix Kubernetes cluster IP range exhausted errors. Resolve service creation failures when the ClusterIP range is full."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Cluster IP Range Exhausted

`Failed to assign IP address to service: IP range exhausted`

This error occurs when the cluster's Service IP range is fully allocated and no more ClusterIPs can be assigned.

### Common Causes

- Too many services created in the cluster
- Cluster CIDR is too small for the number of services
- Services are not cleaned up after use
- Non-RFC1918 address range used
- Default /24 CIDR space exhausted (256 IPs)

### How to Fix

List services:
```bash
kubectl get svc --all-namespaces | wc -l
```

Delete unused services:
```bash
kubectl delete svc <unused-service>
```

Check Service CIDR:
```bash
kubectl cluster-info dump | grep -i "service-cluster-ip-range"
```

### Examples

```bash
# Count services
kubectl get svc -A | wc -l

# List services sorted by creation timestamp
kubectl get svc --all-namespaces --sort-by=.metadata.creationTimestamp
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})