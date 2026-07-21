---
title: "[Solution] AZURE Managed Identity Error"
description: "ManagedIdentityNotFound when managed identity operations fail."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Managed Identity Error` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Identity name is incorrect
- Identity was deleted
- Identity in different resource group
- Identity not assigned to resource

## How to Fix

### Check identity

```bash
az identity show --name myIdentity --resource-group myRG
```
### List identities

```bash
az identity list --resource-group myRG --query "[].{Name:name,PrincipalId:principalId}" --output table
```
### Create identity

```bash
az identity create --name myIdentity --resource-group myRG
```

## Examples

- Identity myIdentity not found in resource group
- Identity deleted but still referenced in VM config

## Related Errors

- [Azure IAM Error]({{< relref "/cloud/azure/azure-rbac-error" >}}) -- General RBAC errors
- [System Assigned]({{< relref "/cloud/azure/azure-managed-identity-system" >}}) -- System assigned
