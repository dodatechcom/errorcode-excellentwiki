---
title: "[Solution] Azure Event Grid Error — topic, subscription, and delivery failures"
description: "Fix Azure Event Grid error. Actionable solutions with Azure CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 150
---

Event Grid errors appear as event delivery failures, subscription endpoint returning non-200 status, or topic authorization issues.

## Common Causes
- Event subscription endpoint not responding or unreachable
- Dead letter storage account not configured for failed events
- Input schema mismatch between publisher and subscriber
- Event subscription filter not matching incoming event types
- Managed identity endpoint not receiving delivery tokens

## How to Fix
### Check topic status
```bash
az eventgrid topic show \
  --resource-group myResourceGroup \
  --name myTopic \
  --query "provisioningState"
```

### List event subscriptions
```bash
az eventgrid event-subscription list \
  --source-resource-id /subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.EventGrid/topics/myTopic \
  --query "[].{name:name, endpoint:endpointUrl, deliverySchema:eventDeliverySchema}"
```

### Create event subscription
```bash
az eventgrid event-subscription create \
  --source-resource-id /subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.EventGrid/topics/myTopic \
  --name mySubscription \
  --endpoint "https://myfunction.azurewebsites.net/api/events"
```

### Send test event
```bash
az eventgrid event send \
  --topic-name myTopic \
  --resource-group myResourceGroup \
  --events '[{"eventType":"test.event","subject":"test","data":{"key":"value"},"eventTime":"2023-01-01T00:00:00Z","id":"1"}]'
```

## Examples
### Create custom topic
```bash
az eventgrid topic create \
  --resource-group myResourceGroup \
  --name myTopic \
  --location eastus \
  --kind EventGrid
```

### Check delivery metrics
```bash
az monitor metrics list \
  --resource /subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.EventGrid/topics/myTopic \
  --metric "PublishFailCount,DeliverFailCount"
```

## Related Errors
- {{< relref "/cloud/azure/azure-event-hub-error" >}}
- {{< relref "/cloud/azure/azure-service-bus-error" >}}
- {{< relref "/cloud/azure/azure-functions-error" >}}
