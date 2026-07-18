---
title: "[Solution] Helm Namespace Error — Fix Namespace Not Found or Already Exists"
description: "Fix Helm namespace errors when the target namespace does not exist or already exists. Create or delete namespaces and configure Helm namespace flags correctly."
---

## What This Error Means

Helm namespace errors occur when the specified Kubernetes namespace is missing or conflicts with an existing one. Helm cannot install or manage releases without a valid namespace.

A typical error:

```
Error: create: failed to create: namespaces "my-app" not found
```

Or:

```
Error: INSTALLATION FAILED: namespaces "my-app" already exists
```

## Why It Happens

Namespace errors happen when:

- **Namespace does not exist**: The target namespace has not been created in the cluster.
- **Namespace already exists**: Using `--create-namespace` with an existing namespace causes conflicts.
- **No namespace specified**: Helm defaults to the `default` namespace, which may not be appropriate.
- **Permission denied**: The user lacks RBAC permissions to create or access the namespace.
- **Namespace is terminating**: The namespace is stuck in a Terminating state and cannot be used.

## How to Fix It

**Step 1: Check existing namespaces**

```bash
kubectl get namespaces
```

**Step 2: Create the namespace**

```bash
kubectl create namespace my-app
helm install my-app ./chart --namespace my-app
```

**Step 3: Use --create-namespace flag**

```bash
helm install my-app ./chart --namespace my-app --create-namespace
```

**Step 4: Handle namespace already exists**

This error is informational. Just remove `--create-namespace`:

```bash
helm install my-app ./chart --namespace my-app
```

**Step 5: Fix a terminating namespace**

```bash
kubectl get namespace my-app -o json > namespace.json
# Remove the finalizers block from namespace.json
kubectl replace --raw "/api/v1/namespaces/my-app/finalize" -f namespace.json
```

**Step 6: Check RBAC permissions**

```bash
kubectl auth can-i create namespaces
kubectl auth can-i get namespaces
```

## Common Mistakes

- **Not creating the namespace before helm install**: Always create namespaces first or use `--create-namespace`.
- **Using --create-namespace on subsequent installs**: This flag is only needed for the first install.
- **Running helm in the default namespace by accident**: Always specify `--namespace` explicitly.
- **Not checking if a namespace is in Terminating state**: Terminating namespaces block all operations.

## Related Pages

- [Helm Release Failed](/tools/helm/helm-release-failed/) -- Release installation failures
- [Helm Upgrade Failed](/tools/helm/helm-upgrade-failed/) -- Upgrade and rollback issues
- [Kubectl Namespace Error](/tools/kubectl/kubectl-namespace-error/) -- Kubernetes namespace issues
