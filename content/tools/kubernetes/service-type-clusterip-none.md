---
title: "[Solution] Service ClusterIP is None (headless)"
description: "Fix Kubernetes headless service issues. Resolve connectivity problems when using headless services with ClusterIP: None."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Headless Service (ClusterIP: None)

This is not an error but a configuration. Headless services (ClusterIP: None) do not load-balance traffic. DNS queries return all pod IPs instead of a single virtual IP.

### Common Causes

- StatefulSets use headless services by design
- Application not handling multiple DNS A/AAAA records
- Client expects a single IP but gets multiple
- DNS caching issues with multiple endpoints
- Pod readiness affecting DNS records

### How to Fix

Ensure your application can handle multiple IP addresses from DNS.

For StatefulSets, use the specific pod DNS name:
```
<pod-name>.<service-name>.<namespace>.svc.cluster.local
```

If you need load balancing, use a regular service instead:
```yaml
spec:
  type: ClusterIP
  clusterIP: ""  # let Kubernetes assign
```

### Examples

```bash
# Check if service is headless
kubectl get svc <name> -o jsonpath='{.spec.clusterIP}'
# None

# DNS lookup returns all pod IPs
kubectl run test --image=busybox -it --rm -- nslookup my-headless-service
# Name:   my-headless-service
# Address: 10.1.0.1
# Address: 10.1.0.2
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})