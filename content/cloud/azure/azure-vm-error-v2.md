---
title: "[Solution] Azure VM — allocation failed"
description: "Fix Azure VM allocation failed. Resolve VM quota and allocation issues in Azure."
cloud: ["azure"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["azure", "vm", "allocation", "failed", "quota", "capacity", "sku"]
weight: 5
---

An Azure VM allocation failed error means Azure cannot allocate the requested VM SKU in the specified region and availability zone. The deployment fails due to insufficient capacity or quota limits.

## What This Error Means

Azure allocates VM resources from its global infrastructure. When you request a VM with a specific SKU (e.g., Standard_D4s_v5) in a region, Azure checks for available physical capacity and your subscription's quota. If either is exhausted, the allocation fails with `AllocationFailed` or `SkuNotAvailable`. This is distinct from quota limits — it means Azure literally does not have enough physical hardware in that region for the requested VM size.

## Common Causes

- Physical capacity exhaustion in the target region for the VM SKU
- Subscription vCPU quota exceeded for the VM family
- Availability zone has insufficient capacity for the requested SKU
- Too many reserved instances consuming capacity
- Spot VM eviction due to capacity demands
- Regional capacity constraints during high-demand periods

## How to Fix

### Check Subscription Quota

```bash
az vm list-usage --location eastus \
  --query "[?name.value=='cores'].{current:currentValue,limit:limit}"
```

### Try Different Region

```bash
az vm create \
  --resource-group my-rg \
  --name my-vm \
  --image Ubuntu2204 \
  --size Standard_D4s_v5 \
  --location westus2
```

### Try Different VM SKU

```bash
# List available VM SKUs
az vm list-sizes --location eastus \
  --query "[?contains(name,'Standard_D')].{name:name,cpu:numberOfCores}" \
  --output table
```

### Request Quota Increase

```bash
az vm list-usage --location eastus \
  --query "[?name.value=='cores']"

az support ticket create \
  --name "VM quota increase" \
  --description "Need increase in Standard D series vCPU quota" \
  --severity High \
  --service-id "06bfd9a3-ca71-42ac-aa08-6c4869afaa53" \
  --problem-classification-id "06bfd9a3-ca71-42ac-aa08-6c4869afaa53"
```

### Use Spot VMs for Non-Critical Workloads

```bash
az vm create \
  --resource-group my-rg \
  --name my-spot-vm \
  --image Ubuntu2204 \
  --size Standard_D4s_v5 \
  --priority Spot \
  --eviction-policy Deallocate
```

### Check Regional Availability

```bash
az provider show \
  --namespace Microsoft.Compute \
  --query 'resourceTypes[?resourceType=="virtualMachines"].locations'
```

### Deploy with Availability Zones

```bash
az vm create \
  --resource-group my-rg \
  --name my-vm \
  --image Ubuntu2204 \
  --size Standard_D4s_v5 \
  --zone 1
```

## Related Errors

- [Azure App Service Error]({{< relref "/cloud/azure/azure-app-service-error-v2" >}}) — 503 Service Unavailable
- [Azure VM Error]({{< relref "/cloud/azure/azure-vm-error" >}}) — original VM error
- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error-v2" >}}) — instance limit exceeded
