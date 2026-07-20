---
title: "[Solution] Istio sidecar injection failed"
description: "Fix Istio sidecar injection failures in Kubernetes. Resolve issues when the Istio sidecar proxy is not injected into pods."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Istio Sidecar Injection Failed

`istio-sidecar-injector: Sidecar injection failed: failed to inject sidecar`

This error occurs when Istio cannot inject the Envoy sidecar proxy into a pod.

### Common Causes

- Namespace does not have the `istio-injection: enabled` label
- Istio sidecar injector is not installed or not running
- Pod annotations disable injection (`sidecar.istio.io/inject: "false"`)
- Resource limits too low for sidecar
- Istio version incompatibility
- Webhook timeout during injection

### How to Fix

Check namespace label:
```bash
kubectl get ns <namespace> --show-labels | grep istio
```

Enable injection on the namespace:
```bash
kubectl label ns <namespace> istio-injection=enabled --overwrite
```

Check the sidecar injector status:
```bash
kubectl get pods -n istio-system | grep sidecar-injector
```

Restart the pod after enabling injection:
```bash
kubectl rollout restart deployment/<name>
```

### Examples

```bash
# Enable Istio injection
kubectl label ns default istio-injection=enabled

# Verify injection
kubectl describe pod <name> | grep -i istio
# Should show istio-proxy container
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})