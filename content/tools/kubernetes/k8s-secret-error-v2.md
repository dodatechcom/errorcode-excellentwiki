---
title: "[Solution] Kubernetes Secret — decode error"
description: "Fix Kubernetes Secret decode errors. Resolve base64 encoding and secret mounting issues."
tools: ["kubernetes"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["kubernetes", "secret", "decode", "base64", "encoding", "mount"]
weight: 5
---

A Secret decode error means the Kubernetes secret contains data that cannot be decoded from base64, or the secret is missing keys referenced by the pod spec.

## What This Error Means

Kubernetes secrets store data as base64-encoded strings. If the data was not properly encoded when created, the decoded content will be corrupted. Additionally, if a pod references a secret key that does not exist, the container will fail with `CreateContainerConfigError`. Secrets can also fail if they exceed the 1MB size limit or have invalid YAML/JSON in annotations.

## Common Causes

- Secret data was not base64-encoded before creation
- Pod references a secret key that does not exist
- Secret exceeds the 1MB size limit
- Secret is in a different namespace than the pod
- Secret type does not match usage (e.g., `kubernetes.io/tls` for SSH keys)
- Corrupted secret data after manual editing

## How to Fix

### Decode Secret Data

```bash
kubectl get secret <secret-name> -o jsonpath='{.data.<key>}' | base64 --decode
```

### List Secret Keys

```bash
kubectl get secret <secret-name> -o jsonpath='{.data}' | jq 'keys'
```

### Create Secret Properly

```bash
kubectl create secret generic my-secret \
  --from-literal=db-password='my-secret-password'
```

### Fix Base64 Encoding

```bash
echo -n 'my-plain-text' | base64
# Output: bXktcGxhaW4tdGV4dA==
```

### Verify Secret Key Reference in Pod

```yaml
env:
  - name: DB_PASSWORD
    valueFrom:
      secretKeyRef:
        name: my-secret
        key: db-password  # Must exist in the secret
```

### Check Secret Type

```bash
kubectl get secret <secret-name> -o jsonpath='{.type}'
```

## Related Errors

- [Kubernetes ConfigMap Error]({{< relref "/tools/kubernetes/k8s-configmap-error-v2" >}}) — ConfigMap key not found
- [Kubernetes RBAC Error]({{< relref "/tools/kubernetes/k8s-rbac-error-v2" >}}) — RBAC forbidden
- [Kubernetes ImagePullBackOff]({{< relref "/tools/kubernetes/k8s-image-pull-v2" >}}) — image pull failed
