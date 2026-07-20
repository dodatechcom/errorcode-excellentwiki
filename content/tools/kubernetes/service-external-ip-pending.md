---
title: "[Solution] Service ExternalIP pending"
description: "Fix Kubernetes service ExternalIP stuck pending. Resolve external IP assignment delays for services."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Service ExternalIP Pending

`<service>   LoadBalancer   <cluster-ip>   <pending>     80:30080/TCP`

This occurs when a LoadBalancer service's external IP is pending assignment. The cloud load balancer may not have finished provisioning.

### Common Causes

- Cloud load balancer provisioning is slow (can take 1-5 minutes)
- Cloud provider account has resource limits
- Incorrect service annotations for the cloud provider
- Network or subnet configuration issues
- No external load balancer controller (on-premises)

### How to Fix

Wait and retry:
```bash
kubectl get svc --watch
```

Check service events:
```bash
kubectl describe service <name>
```

For AWS, check the ELB/NLB:
```bash
aws elb describe-load-balancers
aws elbv2 describe-load-balancers
```

### Examples

```bash
# Watch service until IP is assigned
kubectl get svc my-service -w

# Check for errors
kubectl describe service my-service | grep -A10 Events
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})