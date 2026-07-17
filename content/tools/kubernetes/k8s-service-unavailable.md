---
title: "[Solution] Kubernetes Service Unavailable — no endpoints"
description: "Fix Kubernetes Service unavailable errors. Resolve no endpoints issues."
tools: ["kubernetes"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

A Service unavailable error means the Kubernetes Service has no healthy endpoints. Traffic to the Service cannot reach any running pods.

## Common Causes

- No pods match the Service selector
- All matching pods are in a non-running state (CrashLoopBackOff, Pending)
- Pod readiness probes are failing
- Namespace mismatch between Service and Pods
- Service selector label does not match pod labels

## How to Fix

### Check Service Endpoints

```bash
kubectl get endpoints <service-name>
```

### Verify Service Selector

```bash
kubectl get svc <service-name> -o yaml | grep -A 5 selector
```

### Check Pod Labels

```bash
kubectl get pods --show-labels
```

### Verify Pod Readiness

```bash
kubectl get pods -l app=my-app
```

### Check Namespace

```bash
kubectl get svc -n <namespace>
kubectl get pods -n <namespace>
```

## Examples

```bash
# Example 1: No endpoints
kubectl get endpoints my-service
# NAME         ENDPOINTS
# my-service   <none>
# Fix: ensure pods have correct labels

# Example 2: Pods not ready
kubectl get pods -l app=my-app
# NAME     READY   STATUS
# my-pod   0/1     CrashLoopBackOff
# Fix: fix pod crash issue first
```

## Related Errors

- [Kubernetes CrashLoopBackOff]({{< relref "/tools/kubernetes/k8s-crashloop" >}}) — pod keeps crashing
- [Kubernetes NetworkPolicy]({{< relref "/tools/kubernetes/k8s-network-policy" >}}) — connection refused
