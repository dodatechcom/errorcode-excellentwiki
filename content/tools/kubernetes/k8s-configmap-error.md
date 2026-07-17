---
title: "[Solution] Kubernetes ConfigMap Error — ConfigMap not found or invalid"
description: "Fix Kubernetes ConfigMap errors. Resolve ConfigMap not found or invalid data issues."
tools: ["kubernetes"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

A ConfigMap error occurs when a pod references a ConfigMap that does not exist or contains invalid data. This can prevent pods from starting.

## Common Causes

- ConfigMap name or namespace is misspelled in the pod spec
- ConfigMap was deleted or not yet created
- ConfigMap key referenced in volume mount does not exist
- ConfigMap exceeds the 1MB size limit
- Invalid YAML or data format in ConfigMap

## How to Fix

### Check ConfigMap Exists

```bash
kubectl get configmap <name> -n <namespace>
```

### View ConfigMap Contents

```bash
kubectl get configmap <name> -o yaml
```

### Create ConfigMap

```bash
kubectl create configmap my-config --from-file=config.yaml
kubectl create configmap my-config --from-literal=key1=value1
```

### Verify Pod References

```bash
kubectl get pod <pod-name> -o yaml | grep -A 10 configMapRef
```

### Check Events for Errors

```bash
kubectl describe pod <pod-name>
```

## Examples

```bash
# Example 1: ConfigMap not found
kubectl describe pod my-pod
# Warning: ConfigMap "my-config" not found
# Fix: kubectl create configmap my-config --from-literal=key=value

# Example 2: ConfigMap key missing
kubectl describe pod my-pod
# Warning: key "config.json" not found in ConfigMap "my-config"
# Fix: add the missing key to the ConfigMap
```

## Related Errors

- [Kubernetes Secret Error]({{< relref "/tools/kubernetes/k8s-secret-error" >}}) — Secret not found or invalid
- [Kubernetes RBAC Error]({{< relref "/tools/kubernetes/k8s-rbac-error" >}}) — RBAC forbidden
