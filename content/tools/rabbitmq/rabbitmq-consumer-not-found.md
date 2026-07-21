---
title: "[Solution] RabbitMQ Consumer Not Found Error"
description: "Fix RabbitMQ consumer not found error. Resolve consumer reference issues."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ Consumer Not Found Error

The specified consumer does not exist. It may have been cancelled or the consumer tag is wrong.

## Common Causes

- Consumer was cancelled
- Consumer tag is incorrect
- Connection dropped and consumer removed

## How to Fix

### Solution 1

```bash
rabbitmqctl list_consumers
```

## Related Pages

- [RabbitMQ Connection Error]({{< relref "/tools/rabbitmq/rabbitmq-connection-error" >}})
- [RabbitMQ Queue Error]({{< relref "/tools/rabbitmq/rabbitmq-queue-error" >}})
- [RabbitMQ Exchange Error]({{< relref "/tools/rabbitmq/rabbitmq-exchange-error" >}})
