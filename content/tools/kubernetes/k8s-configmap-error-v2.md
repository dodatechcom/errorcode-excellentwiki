---
title: "[Solution] Kubernetes ConfigMap — key not found"
description: "Fix Kubernetes ConfigMap key not found. Resolve missing ConfigMap keys and volume mount errors."
tools: ["kubernetes"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

A ConfigMap key not found error means the pod references a key that does not exist in the ConfigMap, causing the pod to fail to start or a volume mount to be incomplete.

## What This Error Means

When a pod references a ConfigMap key via environment variable substitution (`configMapKeyRef`) or as a volume mount item, Kubernetes expects the key to exist in the specified ConfigMap. If the key is missing, the pod remains in `CreateContainerConfigError` state and never starts. This is a validation error that prevents container creation entirely.

## Common Causes

- Typo in the key name referenced by the pod
- ConfigMap was updated and the key was renamed or removed
- ConfigMap belongs to a different namespace than the pod
- Key exists but the ConfigMap name is misspelled
- ConfigMap has not been created yet

## How to Fix

### Check Pod Events

```bash
kubectl describe pod <pod-name> | grep -A 5 Events
# Look for: Warning  Failed  configmap "xxx" not found
```

### List ConfigMap Keys

```bash
kubectl get configmap <configmap-name> -o yaml
kubectl get configmap <configmap-name> -o jsonpath='{.data}' | jq 'keys'
```

### Verify Environment Variable Source

```yaml
envFrom:
  - configMapRef:
      name: my-config
```

### Verify Individual Key Reference

```yaml
env:
  - name: APP_CONFIG
    valueFrom:
      configMapKeyRef:
        name: my-config
        key: app-config
```

### Create Missing ConfigMap

```bash
kubectl create configmap my-config --from-literal=app-config="value"
```

## Related Errors

- [Kubernetes Secret Error]({{< relref "/tools/kubernetes/k8s-secret-error-v2" >}}) — secret decode error
- [Kubernetes CrashLoopBackOff]({{< relref "/tools/kubernetes/k8s-crashloop-v2" >}}) — pod crash loop
- [Kubernetes ConfigMap Error]({{< relref "/tools/kubernetes/k8s-configmap-error" >}}) — original ConfigMap error
