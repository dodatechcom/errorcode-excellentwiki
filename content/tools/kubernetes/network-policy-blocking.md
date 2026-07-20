---
title: "[Solution] Network policy blocking pod communication"
description: "Fix Kubernetes network policy blocking inter-pod communication. Resolve connectivity failures caused by restrictive NetworkPolicies."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Network Policy Blocking Communication

This error occurs when a NetworkPolicy is blocking traffic between pods that need to communicate.

### Common Causes

- Default deny-all network policy is too restrictive
- Missing ingress rules for required traffic
- Missing egress rules for required outbound traffic
- Policy selector does not match source or target pods

### How to Fix

List network policies:
```bash
kubectl get networkpolicy --all-namespaces
```

Check pod labels vs policy selectors:
```bash
kubectl describe networkpolicy <name>
```

Test connectivity:
```bash
kubectl run test-$RANDOM --image=busybox -it --rm -- wget -O- http://<service>:<port>
```

### Examples

```bash
# Test connectivity between pods
kubectl run tester --image=busybox -it --rm -- wget -O- --timeout=3 http://my-service:8080
# wget: download timed out

# List all network policies
kubectl get networkpolicy --all-namespaces
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})