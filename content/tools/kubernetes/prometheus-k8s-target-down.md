---
title: "[Solution] Prometheus target down in Kubernetes"
description: "Fix Kubernetes Prometheus target down errors. Resolve Prometheus monitoring failures in the cluster."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Prometheus Target Down

`Get "<url>": dial tcp <ip>:<port>: connect: connection refused`

This error occurs when Prometheus cannot scrape metrics from a target that has been discovered via service or pod annotations.

### Common Causes

- Target pod or service is not running
- Network policy blocking Prometheus traffic
- Target is listening on localhost instead of 0.0.0.0
- ServiceMonitor / PodMonitor misconfiguration

### How to Fix

Check the target endpoint:
```bash
kubectl get pod -l <selector> -o wide
```

Test connectivity from Prometheus pod:
```bash
kubectl exec -n monitoring prometheus-0 -- wget -O- http://<target-ip>:<port>/metrics
```

### Examples

```bash
# Test metric endpoint manually
kubectl port-forward service/my-app 8080:8080
curl http://localhost:8080/metrics

# Check Prometheus target status
kubectl port-forward service/prometheus 9090:9090
# Open http://localhost:9090/targets
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})