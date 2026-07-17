---
title: "[Solution] Kubernetes Secret Not Found — secret X not found"
description: "Fix Kubernetes Secret not found error. Create and manage Secrets for sensitive data."
tools: ["kubernetes"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Kubernetes Secret Not Found — secret X not found

This error occurs when a pod references a Secret that doesn't exist. Secrets are used to store sensitive data like passwords, tokens, and certificates.

## Common Causes

- Secret was not created before the pod
- Wrong namespace specified
- Typo in Secret name
- Secret was deleted or never created

## How to Fix

### List Secrets

```bash
kubectl get secrets
```

### Create Secret from Literal

```bash
kubectl create secret generic <name> \
  --from-literal=username=admin \
  --from-literal=password=secret123
```

### Create Secret from File

```bash
kubectl create secret generic <name> \
  --from-file=./username.txt \
  --from-file=./password.txt
```

### Create TLS Secret

```bash
kubectl create secret tls <name> \
  --cert=./tls.crt \
  --key=./tls.key
```

### Create Secret from YAML

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: my-secret
type: Opaque
data:
  username: YWRtaW4=
  password: c2VjcmV0MTIz
```

### Verify Secret Exists

```bash
kubectl get secret <name> -n <namespace>
```

## Examples

```bash
# Example 1: Secret missing
kubectl logs my-pod
# Error: secret "db-credentials" not found
# Fix: kubectl create secret generic db-credentials \
#   --from-literal=password=mydbpass

# Example 2: Wrong namespace
kubectl get secret my-secret -n production
# Error: NotFound
# Fix: kubectl get secret my-secret -n default

# Example 3: Mount secret as volume
kubectl create secret generic tls-cert \
  --from-file=tls.crt=./cert.pem \
  --from-file=tls.key=./key.pem
```

## Related Errors

- [ConfigMap Error]({{< relref "/tools/kubernetes/configmap-error" >}}) — configmap not found
- [RBAC Error]({{< relref "/tools/kubernetes/rbac-error" >}}) — RBAC permission denied
