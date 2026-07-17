---
title: "Azure QuotaExceeded: Request Quota Exceeded"
description: "QuotaExceeded: The request quota has been exceeded — Fix Azure subscription quota limits."
error-types: ["quota-error"]
severities: ["error"]
weight: 5
---

The `QuotaExceeded` error occurs when an Azure subscription exceeds its allocated quota for a specific resource type (e.g., vCPUs, storage accounts, or VM instances). This prevents new resource creation until the quota is increased or resources are deallocated.

## Common Causes

- Too many VMs running in a region, exhausting the vCPU quota
- Subscription has a low default quota (new subscriptions start with conservative limits)
- Resource group contains resources that are not immediately visible
- Shared subscription across multiple teams with no centralized quota management

## How to Fix

Check current quota usage:

```bash
az vm list-usage --location eastus --query '[].{Name:name,Current:currentValue,Max:limit}'
```

View all quota limits:

```bash
az provider show --namespace Microsoft.Compute --query 'resourceTypes[].quotaUsages'
```

Request a quota increase:

```bash
az support ticket create \
  --display-name "Increase vCPU quota" \
  --support-plan "Azure_CUv2" \
  --severity "moderate" \
  --service-id "06bfd9a3-3930-cf49-c314-348537258f45" \
  --problem-description "Need to increase standard Dv4 vCPU limit from 20 to 100 in East US"
```

Deallocate unused VMs to free quota:

```bash
az vm deallocate --name my-vm --resource-group my-rg
az vm delete --name my-vm --resource-group my-rg
```

## Examples

- Deployment fails with `Operation could not be completed as it results in exceeding quota limit of 20` for standard DSv3 vCPUs
- Cannot create more storage accounts because the subscription limit of 200 is reached
- AKS cluster creation fails because the subscription does not have enough GPU quota

## Related Errors

- [Azure VM Not Found]({{< relref "/cloud/azure/vm-not-found" >}}) — VM resource not found.
- [AWS Quota Exceeded]({{< relref "/cloud/aws/ec2-quota" >}}) — AWS EC2 limits.
- [GCP Quota Exceeded]({{< relref "/cloud/gcp/quota-exceeded2" >}}) — GCP equivalent.
