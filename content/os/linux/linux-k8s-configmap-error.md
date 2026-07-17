---
title: "[Solution] k8s: ConfigMap Error — Failed to Mount ConfigMap"
description: "Fix Kubernetes ConfigMap errors. Resolve mount failures, missing keys, and ConfigMap validation issues in pod specifications."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["kubernetes", "k8s", "configmap", "config", "mount", "volume"]
weight: 5
---

# k8s: ConfigMap Error — Failed to Mount ConfigMap

A ConfigMap error occurs when a pod cannot mount or reference a ConfigMap. The pod may fail to start with:

> "Failed to apply default security context" or

> "ConfigMap \"my-config\" not found"

## What This Error Means

ConfigMaps store non-sensitive configuration data that pods can consume as environment variables or mounted files. When a ConfigMap is missing, has wrong keys, or cannot be mounted (e.g., due to namespace mismatch or RBAC), the pod fails to start.

## Common Causes

- ConfigMap does not exist in the pod's namespace
- ConfigMap key does not exist (referenced key missing)
- ConfigMap name is misspelled in the pod spec
- RBAC permissions prevent reading the ConfigMap
- ConfigMap exceeds maximum size (1 MB)
- ConfigMap referenced in volume but pod already exists

## How to Fix

### Check ConfigMap Exists

```bash
kubectl get configmap -n <namespace>
kubectl get configmap <name> -o yaml
```

### Verify ConfigMap Key

```bash
kubectl get configmap <name> -o jsonpath='{.data}'
```

### Create ConfigMap from File

```bash
kubectl create configmap my-config --from-file=config.yaml
kubectl create configmap my-config --from-literal=key1=value1 --from-literal=key2=value2
```

### Fix Volume Mount ConfigMap

```yaml
volumes:
  - name: config-volume
    configMap:
      name: my-config
      items:
        - key: "config.yaml"
          path: "config.yaml"
containers:
  - name: app
    volumeMounts:
      - name: config-volume
        mountPath: /etc/config
```

### Check RBAC Permissions

```bash
kubectl auth can-i get configmap <name> --as=system:serviceaccount:<namespace>:<sa-name>
```

### Update ConfigMap Without Restart

```bash
# Edit ConfigMap
kubectl edit configmap <name>

# Restart pods to pick up changes (if not using subPath)
kubectl rollout restart deployment/<deployment-name>
```

## Related Errors

- [k8s Secret Error]({{< relref "/os/linux/linux-k8s-secret-error" >}}) — Secret mount/reference errors
- [k8s RBAC Forbidden]({{< relref "/os/linux/linux-k8s-rbac-error" >}}) — RBAC permission issues
- [k8s CrashLoopBackOff]({{< relref "/os/linux/linux-k8s-crashloop" >}}) — Pod crash loops from bad config
