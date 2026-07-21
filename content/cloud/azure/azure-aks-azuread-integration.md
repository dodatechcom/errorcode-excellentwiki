---
title: "[Solution] Azure AKS Azure AD Integration Error"
description: "Fix Azure Kubernetes Service Azure AD integration failures for cluster authentication and RBAC."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Azure AD integration errors prevent users from authenticating to AKS clusters using Azure AD credentials. This blocks kubectl access and RBAC enforcement.

## Common Causes

- Azure AD application registration is missing or misconfigured
- Cluster RBAC binding references a group that no longer exists
- kubectl cannot obtain a token due to expired refresh token
- AKS cluster was created without Azure AD integration and cannot be added later

## How to Fix

### Check Azure AD integration status

```bash
az aks show \
  --name myAKSCluster \
  --resource-group myRG \
  --query "azureAdProfile"
```

### Get cluster admin credentials

```bash
az aks get-credentials \
  --name myAKSCluster \
  --resource-group myRG \
  --admin
```

### Create Kubernetes RBAC binding

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: aks-admin-binding
subjects:
  - kind: Group
    name: "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: cluster-admin
  apiGroup: rbac.authorization.k8s.io
```

### Verify kubectl can authenticate

```bash
kubectl auth can-i --list
```

## Examples

- `az aks get-credentials` fails with `AADTokenExpired` after 1 hour without refresh
- kubectl returns `error: You must be logged in to the server` despite valid Azure CLI session
- RBAC ClusterRoleBinding references a deleted Azure AD group causing 403 Forbidden

## Related Errors

- [Azure AKS Error]({{< relref "/cloud/azure/azure-aks-error" >}}) -- General AKS errors.
- [Azure AD Error]({{< relref "/cloud/azure/azure-ad-error" >}}) -- Azure AD authentication issues.
