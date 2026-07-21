---
title: "[Solution] Azure AKS Pod Identity Error"
description: "Fix Azure AKS pod managed identity failures preventing pods from accessing Azure resources."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Pod identity errors prevent AKS pods from using managed identity to authenticate to Azure services like Key Vault, Storage, and SQL. This breaks workload identity federation.

## Common Causes

- Pod identity CRDs are not installed or are outdated
- Managed identity is not assigned to the node pool or has no role assignments
- Azure AD pod identity webhook is not running in the cluster
- Namespace mismatch between the pod identity and the running pod

## How to Fix

### Install pod identity CRDs

```bash
kubectl apply -f https://raw.githubusercontent.com/Azure/azure-workload-identity/main/deploy/manifests/crds.yaml
```

### Deploy workload identity webhook

```bash
helm install workload-identity-webhook azure/workload-identity \
  --namespace kube-system --create-namespace
```

### Assign managed identity to the node pool

```bash
az aks update \
  --name myAKSCluster \
  --resource-group myRG \
  --enable-managed-identity \
  --assign-identity /subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.ManagedIdentity/userAssignedIdentities/myIdentity
```

### Create identity binding

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: my-pod-sa
  annotations:
    azure.workload.identity/client-id: "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
```

## Examples

- Pod fails with `aadpodidentity` not found error when trying to access Key Vault
- Managed identity exists but no role assignment allows it to read secrets
- Workload identity webhook injection is disabled in the target namespace

## Related Errors

- [Azure Managed Identity Error]({{< relref "/cloud/azure/azure-managed-identity-error" >}}) -- Managed identity issues.
- [Azure Key Vault Error]({{< relref "/cloud/azure/azure-key-vault-error" >}}) -- Key Vault access.
