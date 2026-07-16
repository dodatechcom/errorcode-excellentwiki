---
title: "Azure ResourceNotFound: Virtual Machine Not Found"
description: "ResourceNotFound: The Virtual Machine was not found — Fix Azure VM resource lookup errors."
cloud: ["azure"]
error-types: ["api-error"]
severities: ["error"]
tags: ["azure", "vm", "virtual-machine", "resource-not-found", "arm", "management"]
weight: 5
---

The `ResourceNotFound` error occurs when an Azure API call references a Virtual Machine that does not exist in the specified resource group or subscription. The VM may have been deleted, the resource group name is wrong, or the subscription ID is incorrect.

## Common Causes

- The VM was deleted and references in scripts or templates are stale
- Wrong resource group name in the command or template
- The VM is in a different subscription than the one currently logged in
- Typo in the VM name (Azure is case-sensitive for some operations)

## How to Fix

Check the current subscription:

```bash
az account show --query '{Name:name, Id:id}'
```

List VMs in a resource group:

```bash
az vm list --resource-group my-rg --query '[].{Name:name, Status:provisioningState}' --output table
```

Search across all subscriptions:

```bash
az account list --query '[].{Name:name, Id:id}' --output table

az vm list --query '[].{Name:name, ResourceGroup:resourceGroup, Subscription:subscriptionId}' --output table
```

Recreate the VM if it was deleted:

```bash
az vm create \
  --name my-vm \
  --resource-group my-rg \
  --image Ubuntu2204 \
  --size Standard_D2s_v3 \
  --admin-username azureuser \
  --ssh-key-value ~/.ssh/id_rsa.pub
```

## Examples

- Terraform destroy removed the VM and a CI/CD pipeline still tries to SSH into it
- Deployment script uses `--name my-VM` but the actual VM is named `my-vm`
- Developer runs commands against a staging subscription instead of production

## Related Errors

- [Azure Disk Error]({{< relref "/cloud/azure/disk-error" >}}) — disk I/O failure.
- [Azure NSG Error]({{< relref "/cloud/azure/nsg-error" >}}) — network security group issues.
- [AWS Instance Not Found]({{< relref "/cloud/aws/instance-not-found" >}}) — AWS EC2 equivalent.
