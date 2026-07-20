---
title: "[Solution] Service port conflict"
description: "Fix Kubernetes service port conflicts. Resolve issues when multiple services try to use the same NodePort."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Service Port Conflict

`Error: Service "<name>" is invalid: spec.ports[0].nodePort: Invalid value: 30080: provided port is already allocated`

This error occurs when a NodePort or LoadBalancer service requests a port that is already in use by another service.

### Common Causes

- Manually specified NodePort is already allocated
- Multiple services with the same static NodePort
- Pod hostPort conflicts with the service NodePort
- Port range (30000-32767) exhausted

### How to Fix

List services and their NodePorts:
```bash
kubectl get svc --all-namespaces -o wide
```

Use a different NodePort or omit it to let Kubernetes assign one automatically:
```yaml
spec:
  ports:
  - port: 80
    nodePort: 0  # auto-assign
```

### Examples

```bash
# Find conflicting NodePort
kubectl get svc --all-namespaces -o yaml | grep nodePort

# Let Kubernetes assign the port
kubectl patch service my-service -p '{"spec":{"ports":[{"port":80,"nodePort":0}]}}'
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})