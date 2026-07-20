---
title: "[Solution] Gateway API error"
description: "Fix Kubernetes Gateway API errors. Resolve issues with Gateway, GatewayClass, and HTTPRoute resources."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Gateway API Error

`The Gateway "<name>" is not ready`

This error occurs when a Gateway API resource is not in a ready state, preventing HTTPRoute traffic routing.

### Common Causes

- GatewayClass does not exist or is not supported
- Gateway controller is not installed
- Gateway configuration is invalid
- Listener hostname conflict

### How to Fix

Check GatewayClass:
```bash
kubectl get gatewayclass
kubectl describe gatewayclass <name>
```

Check Gateway:
```bash
kubectl describe gateway <name>
```

### Examples

```bash
# Check Gateway API resources
kubectl get gatewayclass,gw,httproute

# Describe Gateway
kubectl describe gateway my-gateway
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})