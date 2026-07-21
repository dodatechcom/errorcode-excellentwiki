---
title: "[Solution] Azure Event Hub Throttling Error"
description: "Fix Azure Event Hub throttling and quota exceeded errors that block message ingestion."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Event Hub throttling occurs when message ingestion exceeds the throughput unit limits. This causes message drops and client disconnections.

## Common Causes

- Throughput units are too low for the message volume
- Multiple producers are sending to the same partition simultaneously
- Consumer group is lagging behind and causing backpressure
- Event Hub namespace has hit the maximum partition count

## How to Fix

### Check Event Hub throughput usage

```bash
az monitor metrics list \
  --resource /subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.EventHub/namespaces/myNamespace \
  --metric "IncomingMessages" "ThrottledRequests"
```

### Scale throughput units

```bash
az eventhubs namespace update \
  --name myNamespace \
  --resource-group myRG \
  --capacity 4
```

### Check consumer group lag

```bash
az eventhubs eventhub consumer-group list \
  --namespace-name myNamespace \
  --eventhub-name myEventHub \
  --resource-group myRG
```

### Monitor throttled requests

```bash
az monitor metrics list \
  --resource /subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.EventHub/namespaces/myNamespace \
  --metric "ThrottledRequests" \
  --interval PT1M
```

## Examples

- Producer receives `QuotaExceeded` when sending 1000 messages per second with 1 TU
- Consumer group falls behind by 1 million messages and cannot catch up
- Event Hub throttles all connections because the namespace reached its connection limit

## Related Errors

- [Azure Event Hub Error]({{< relref "/cloud/azure/azure-event-hub-error" >}}) -- General Event Hub errors.
- [Azure Service Bus Error]({{< relref "/cloud/azure/azure-service-bus-error" >}}) -- Service Bus issues.
