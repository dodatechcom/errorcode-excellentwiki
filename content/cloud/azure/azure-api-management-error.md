---
title: "[Solution] Azure API Management Error — subscription, policy, and product failures"
description: "Fix Azure API Management error. Actionable solutions with Azure CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 147
---

API Management errors appear as subscription key failures, policy conflicts, or product access issues that block API gateway traffic.

## Common Causes
- Subscription key disabled or revoked without developer notification
- Policy XML syntax error causing gateway deployment failure
- Product not published or missing required API associations
- Rate limit policy too restrictive for legitimate traffic patterns
- Backend API unreachable from APIM regional deployment

## How to Fix
### Check APIM service status
```bash
az apim show \
  --resource-group myResourceGroup \
  --name myAPIM \
  --query "provisioningState"
```

### List subscriptions
```bash
az apim subscription list \
  --resource-group myResourceGroup \
  --service-name myAPIM \
  --query "[].{name:name, state:state, primaryKey:primaryKey}"
```

### Create new subscription
```bash
az apim subscription create \
  --resource-group myResourceGroup \
  --service-name myAPIM \
  --name myNewSubscription \
  --scope /products/starter
```

### Update API policy
```bash
az apim api policy create \
  --resource-group myResourceGroup \
  --service-name myAPIM \
  --api-id myApi \
  --xml-file policy.xml
```

## Examples
### List APIs
```bash
az apim api list \
  --resource-group myResourceGroup \
  --service-name myAPIM \
  --query "[].{name:name, path:path}"
```

### Check APIM diagnostics
```bash
az monitor diagnostic-settings list \
  --resource /subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.ApiManagement/service/myAPIM
```

## Related Errors
- {{< relref "/cloud/azure/azure-logic-apps-error" >}}
- {{< relref "/cloud/azure/azure-app-service-error" >}}
- {{< relref "/cloud/azure/auth-failed" >}}
