---
title: "[Solution] RabbitMQ Publish Not Confirmed Error"
description: "Fix RabbitMQ publish not confirmed error. Resolve publisher confirm issues."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ Publish Not Confirmed Error

The publisher confirm is not received. The broker did not confirm the message was received.

## Common Causes

- Publisher confirms not enabled on channel
- Broker crashed before confirming
- Channel closed before confirm

## How to Fix

### Solution 1

```bash
rabbitmqctl list_channels confirm
```

## Related Pages

- [RabbitMQ Connection Error]({{< relref "/tools/rabbitmq/rabbitmq-connection-error" >}})
- [RabbitMQ Queue Error]({{< relref "/tools/rabbitmq/rabbitmq-queue-error" >}})
- [RabbitMQ Exchange Error]({{< relref "/tools/rabbitmq/rabbitmq-exchange-error" >}})
