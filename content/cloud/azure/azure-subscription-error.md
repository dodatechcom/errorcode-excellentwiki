---
title: "[Solution] Azure Subscription Error — management, registration, and quota failures"
description: "Fix Azure Subscription error. Actionable solutions with Azure CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 164
---

Subscription errors involve registration failures, quota limit issues, or management group access problems that block resource creation and governance.

## Common Causes
- Subscription not registered for required resource providers
- Quota limit exceeded for specific VM sizes or resource types
- Billing issues causing subscription suspension
- Management group hierarchy preventing inherited permissions
- Subscription state changed to Disabled or Expired

## How to Fix
### Check subscription status
```bash
az account show \
  --query "{id:id, name:name, state:state, subscriptionPolicies:subscriptionPolicies}"
```

### Register resource provider
```bash
az provider register --namespace Microsoft.Compute --wait
```

### List resource provider status
```bash
az provider list \
  --query "[].{namespace:namespace,state:state,registrationPolicy:registrationPolicy}"
```

### Check quota usage
```bash
az vm list-usage --location eastus --query "[].{name:name.value,currentValue:currentValue,limit:limit}"
```

### Request quota increase
```bash
az support ticket create \
  --problem-classification-name "Quota Issues" \
  --title "VM quota increase request" \
  --description "Need 100 cores of Standard_DS_v3" \
  --severity Normal
```

## Examples
### List all subscriptions
```bash
az account list --query "[].{id:id,name:name,state:state}"
```

### Set active subscription
```bash
az account set --subscription mySubscriptionId
```

## Related Errors
- {{< relref "/cloud/azure/quota-exceeded" >}}
- {{< relref "/cloud/azure/azure-cost-management-error" >}}
- {{< relref "/cloud/azure/azure-rbac-error" >}}
