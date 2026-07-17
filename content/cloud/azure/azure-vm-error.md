---
title: "[Solution] Azure VM Deployment Error"
description: "Fix Azure VM deployment errors. Resolve virtual machine provisioning issues."
error-types: ["api-error"]
severities: ["error"]
weight: 5
---

An Azure VM deployment error occurs when Azure cannot create or start a virtual machine. This can be caused by quota limits, configuration issues, or resource conflicts.

## Common Causes

- Subscription quota exceeded for the VM series
- Insufficient permissions to create resources
- Invalid VM configuration (OS disk, network)
- Storage account not available
- VNet/Subnet misconfiguration

## How to Fix

### Check Quota

```bash
az vm list-usage --location eastus --query "[?name.value=='cores']"
```

### List Available VM Sizes

```bash
az vm list-sizes --location eastus --query "[?name.contains(name, 'Standard')]"
```

### Check Deployment Errors

```bash
az deployment group show --resource-group myRG --name myDeployment --query 'properties.error'
```

### Verify Permissions

```bash
az role assignment list --assignee user@domain.com
```

### Check Resource Group

```bash
az group show --name myRG
```

## Examples

```bash
# Example 1: Quota exceeded
# Operation could not be completed as it results in exceeding quota limit
# Fix: request quota increase or use different VM series

# Example 2: Invalid configuration
# The requested VM size is not available in the location
# Fix: use available VM size in the region
```

## Related Errors

- [Azure App Service Error]({{< relref "/cloud/azure/azure-app-service-error" >}}) — App Service error
- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) — EC2 launch failed
