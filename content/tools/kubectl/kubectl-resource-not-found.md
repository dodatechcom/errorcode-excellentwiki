---
title: "[Solution] Kubectl Resource Not Found — Fix Resource Lookup"
description: "Fix kubectl resource not found errors. Resolve missing resources, namespace issues, and API group/version mismatches with solutions."
---

## What This Error Means

The `resource not found` error means kubectl cannot locate the specified resource in the cluster. This can be a genuine missing resource or a query to the wrong namespace, API group, or resource type.

A typical error:

```
Error from server (NotFound): deployments.apps "web-app" not found
```

Or:

```
error: the server doesn't have a resource type "ingress"
```

## Why It Happens

Resource not found errors occur when:

- **Resource does not exist**: The resource was never created or was deleted.
- **Wrong namespace**: The resource exists in a different namespace than specified.
- **Wrong API group or version**: Using an incorrect resource type name or API version.
- **RBAC restrictions**: The user lacks permissions to see the resource.
- **Resource not yet created**: The resource creation is still in progress.
- **Typo in resource name**: Incorrect spelling of the resource name.

## How to Fix It

**Step 1: Verify the resource exists in any namespace**

```bash
kubectl get deployments --all-namespaces
kubectl get all --all-namespaces | grep web-app
```

**Step 2: Check the correct resource type**

```bash
kubectl api-resources | grep ingress
```

**Step 3: Use the fully qualified resource name**

```bash
# Instead of:
kubectl get ingress

# Use:
kubectl get ingress.networking.k8s.io
```

**Step 4: Check RBAC permissions**

```bash
kubectl auth can-i get deployments --namespace default
kubectl auth can-i list pods --as=system:serviceaccount:default:mysa
```

**Step 5: Verify resource creation status**

```bash
kubectl get events --sort-by=.metadata.creationTimestamp
kubectl rollout status deployment/web-app
```

## Common Mistakes

- **Assuming default namespace**: Always specify the namespace explicitly with `-n` flag.
- **Using deprecated resource names**: Some resources changed names between Kubernetes versions.
- **Forgetting API version suffixes**: Resource types like `ingress` need `networking.k8s.io` in some clusters.
- **Not checking RBAC**: Service accounts may lack permissions to see certain resources.

## Related Pages

- [Kubectl Context Error](/tools/kubectl/kubectl-context-error/) — Context configuration issues
- [Kubectl Permission Error](/tools/kubectl/kubectl-permission-error/) — RBAC authorization errors
- [Terraform Resource Already Managed](/tools/terraform/terraform-resource-already-managed/) — Resource tracking issues
