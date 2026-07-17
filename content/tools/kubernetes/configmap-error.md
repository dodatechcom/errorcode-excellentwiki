---
title: "[Solution] Kubernetes ConfigMap Not Found — configmap X not found"
description: "Fix Kubernetes ConfigMap not found error. Create and reference ConfigMaps correctly."
tools: ["kubernetes"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Kubernetes ConfigMap Not Found — configmap X not found

This error occurs when a pod references a ConfigMap that doesn't exist in the namespace. Pods using the ConfigMap will fail to start.

## Common Causes

- ConfigMap was not created before the pod
- Wrong namespace specified
- Typo in ConfigMap name
- ConfigMap was deleted

## How to Fix

### List ConfigMaps

```bash
kubectl get configmaps
```

### Create ConfigMap from File

```bash
kubectl create configmap <name> --from-file=<path>
```

### Create ConfigMap from Literals

```bash
kubectl create configmap <name> --from-literal=key1=value1
```

### Create ConfigMap from YAML

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: my-config
data:
  APP_ENV: "production"
  LOG_LEVEL: "info"
```

### Verify ConfigMap Exists

```bash
kubectl get configmap <name> -n <namespace>
```

### Use envFrom to Reference All Keys

```yaml
spec:
  containers:
    - name: app
      envFrom:
        - configMapRef:
            name: my-config
```

## Examples

```bash
# Example 1: ConfigMap missing
kubectl logs my-pod
# Error: configmap "app-config" not found
# Fix: kubectl create configmap app-config --from-literal=KEY=VALUE

# Example 2: Wrong namespace
kubectl get configmap my-config -n production
# Error: NotFound
# Fix: kubectl get configmap my-config -n default

# Example 3: Mount ConfigMap as volume
kubectl create configmap nginx-conf --from-file=nginx.conf
```

## Related Errors

- [Secret Error]({{< relref "/tools/kubernetes/secret-error" >}}) — secret not found
- [Pod Crash]({{< relref "/tools/kubernetes/pod-crash" >}}) — CrashLoopBackOff error
