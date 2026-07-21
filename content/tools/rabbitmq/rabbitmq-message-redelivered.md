---
title: "[Solution] RabbitMQ Message Redelivered Error"
description: "Fix RabbitMQ message redelivered error. Resolve message redelivery issues."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ Message Redelivered Error

Messages are being redelivered to consumers. The consumer is not acknowledging messages properly.

## Common Causes

- Consumer does not send basic.ack
- Consumer crashes before acknowledging
- Requeue is set to true on reject

## How to Fix

### Solution 1

```bash
rabbitmqctl list_queues name messages consumers
```

## Related Pages

- [RabbitMQ Connection Error]({{< relref "/tools/rabbitmq/rabbitmq-connection-error" >}})
- [RabbitMQ Queue Error]({{< relref "/tools/rabbitmq/rabbitmq-queue-error" >}})
- [RabbitMQ Exchange Error]({{< relref "/tools/rabbitmq/rabbitmq-exchange-error" >}})
