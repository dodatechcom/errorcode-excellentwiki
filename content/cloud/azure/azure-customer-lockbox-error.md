---
title: "[Solution] Azure Customer Lockbox Error"
description: "Fix Azure Customer Lockbox approval failures that block Microsoft support access to data."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Customer Lockbox errors prevent Microsoft support engineers from accessing customer data during support incidents. This can delay issue resolution when data access is required.

## Common Causes

- Customer Lockbox is not enabled for the subscription
- Lockbox request has expired before being approved
- Designated approver is not available or has insufficient permissions
- Lockbox request is for a resource in a subscription without Lockbox enabled

## How to Fix

### Enable Customer Lockbox

```bash
az security sub-assessment show \
  --assessed-resource-id "/subscriptions/xxx" \
  --assessment-name "c4e2980f-39e0-4bd8-ba5a-7a5a8a8a8a8a"
```

### Check pending lockbox requests

```bash
az lockbox request list \
  --resource-group myRG \
  --query "[].{Id:id,Status:status,Expiration:expirationDateTime}"
```

### Approve a lockbox request

```bash
az lockbox request approve \
  --resource-group myRG \
  --request-id requestId \
  --approval "Approved for troubleshooting database corruption"
```

### Deny a lockbox request

```bash
az lockbox request deny \
  --resource-group myRG \
  --request-id requestId \
  --reason "Data access not required for this issue"
```

## Examples

- Support engineer cannot access the SQL database logs because the Lockbox request was denied
- Lockbox request expires after 48 hours because no designated approver is assigned
- Customer Lockbox is enabled but the approver role is assigned to a service account with no notifications

## Related Errors

- [Azure Security Center Error]({{< relref "/cloud/azure/azure-security-center-error" >}}) -- Security Center errors.
- [Azure Policy Error]({{< relref "/cloud/azure/azure-policy-error" >}}) -- Policy issues.
