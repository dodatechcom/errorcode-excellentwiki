---
title: "[Solution] Azure API Management Rate Limit Error"
description: "Fix Azure API Management rate limiting errors that block legitimate API requests."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Rate limiting errors in API Management return HTTP 429 responses when clients exceed their request quotas. This is by design but can be misconfigured.

## Common Causes

- Rate limit policy is too restrictive for the client's normal usage pattern
- Rate limit counter resets at midnight UTC but usage is not evenly distributed
- Multiple policies apply conflicting rate limits to the same operation
- Developer portal does not display the correct quota information to consumers

## How to Fix

### Check rate limit policy

```bash
az apim api show \
  --resource-group myRG \
  --service-name myAPIM \
  --api-id myAPI \
  --query "apiVersionSetId"
```

### Update rate limit policy

```xml
<policies>
    <inbound>
        <rate-limit-by-key calls="100" renewal-period="60" 
            counter-key="@(context.Subscription.Id)" />
    </inbound>
</policies>
```

### Monitor rate limit metrics

```bash
az monitor metrics list \
  --resource /subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.ApiManagement/service/myAPIM \
  --metric "TotalRequests" "FailedRequests"
```

### List APIM products and rate limits

```bash
az apim product list \
  --resource-group myRG \
  --service-name myAPIM \
  --query "[].{Name:name,State:state,SubscriptionRequired:subscriptionRequired}"
```

## Examples

- Client receives 429 Too Many Requests after sending 50 requests per minute when the limit is 100
- Rate limit applies per subscription but the client shares a subscription across multiple services
- Rate limit counter is not reset and blocks the client for the rest of the hour

## Related Errors

- [Azure API Management Error]({{< relref "/cloud/azure/azure-api-management-error" >}}) -- General APIM errors.
- [Azure App Service Error]({{< relref "/cloud/azure/azure-app-service-error" >}}) -- Backend errors.
