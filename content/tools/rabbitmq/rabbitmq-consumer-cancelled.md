---
title: "[Solution] RabbitMQ Consumer Cancelled Error"
description: "Fix RabbitMQ consumer cancelled error. Resolve unexpected consumer cancellation issues."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ Consumer Cancelled Error

The broker cancels the consumer. This can happen due to queue deletion, TTL expiry, or policy changes.

## Common Causes

- Queue was deleted or expired
- Consumer cancelled via management UI
- Queue was moved or redeclared

## How to Fix

### Solution 1

```bash
rabbitmqctl list_queues name
```

## Related Pages

- [RabbitMQ Connection Error]({{< relref "/tools/rabbitmq/rabbitmq-connection-error" >}})
- [RabbitMQ Queue Error]({{< relref "/tools/rabbitmq/rabbitmq-queue-error" >}})
- [RabbitMQ Exchange Error]({{< relref "/tools/rabbitmq/rabbitmq-exchange-error" >}})
