---
title: "[Solution] Azure Event Grid Dead Letter Error"
description: "Fix Azure Event Grid dead letter queue failures preventing undelivered event handling."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Dead letter errors occur when Event Grid cannot deliver events to the dead letter storage. This causes lost events that cannot be replayed or debugged.

## Common Causes

- Dead letter storage account does not exist or has been deleted
- Event subscription dead letter endpoint URL is invalid
- Storage container for dead letters does not exist
- Access policy on the dead letter storage does not allow Event Grid to write

## How to Fix

### Check dead letter configuration

```bash
az eventgrid event-subscription show \
  --name mySubscription \
  --source-resource-id /subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.EventGrid/topics/myTopic \
  --query "deadLetterDestination"
```

### Create a dead letter container

```bash
az storage container create \
  --account-name mystorageaccount \
  --name deadletter \
  --auth-mode login
```

### Update event subscription with dead letter

```bash
az eventgrid event-subscription update \
  --name mySubscription \
  --source-resource-id /subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.EventGrid/topics/myTopic \
  --dead-letter-endpoint "https://mystorageaccount.blob.core.windows.net/deadletter"
```

### List dead letter events

```bash
az storage blob list \
  --account-name mystorageaccount \
  --container-name deadletter \
  --query "[].{Name:name,Created:properties.creationTime}"
```

## Examples

- Event subscription fails to create because the dead letter container does not exist
- Dead letter storage account is in a different region and Event Grid cannot write
- Events are dropped silently because the dead letter endpoint points to a non-existent container

## Related Errors

- [Azure Event Grid Error]({{< relref "/cloud/azure/azure-event-grid-error" >}}) -- General Event Grid errors.
- [Azure Storage Error]({{< relref "/cloud/azure/azure-storage-error" >}}) -- Storage issues.
