---
title: "[Solution] Kubernetes No Endpoints Available — service has no endpoints"
description: "Fix Kubernetes no endpoints available error. Resolve service endpoint and selector issues."
tools: ["kubernetes"]
error-types: ["tool-error"]
severities: ["error"]
tags: ["service-error", "no-endpoints", "service", "selector", "kubernetes"]
weight: 5
---

# Kubernetes No Endpoints Available — service has no endpoints

A service shows no endpoints when its selector doesn't match any running pods. Traffic to the service will fail.

## Common Causes

- Service selector doesn't match pod labels
- No pods are running for the service
- Pods are in a non-Running state
- Selector label is misspelled

## How to Fix

### Check Service Selector

```bash
kubectl get svc <service-name> -o yaml
```

### Check Matching Pods

```bash
kubectl get pods -l <selector-key>=<selector-value>
```

### Verify Endpoints

```bash
kubectl get endpoints <service-name>
```

### Fix Pod Labels

```yaml
metadata:
  labels:
    app: my-service  # Must match service selector
```

### Describe Service for Events

```bash
kubectl describe svc <service-name>
```

### Check Pod Status

```bash
kubectl get pods --show-labels
```

## Examples

```bash
# Example 1: Label mismatch
kubectl get endpoints my-svc
# NAME       ENDPOINTS   AGE
# my-svc     <none>      5m
# Fix: ensure pods have label matching service selector

# Example 2: Pods not running
kubectl get pods -l app=my-service
# NAME                     READY   STATUS
# my-service-pod           0/1     CrashLoopBackOff
# Fix: resolve pod crash issue

# Example 3: Check all labels
kubectl get pods --show-labels
# Fix: update deployment labels to match service selector
```

## Related Errors

- [Service Error]({{< relref "/tools/kubernetes/service-error2" >}}) — service endpoint issues
- [Pod Crash]({{< relref "/tools/kubernetes/pod-crash" >}}) — pod keeps crashing
