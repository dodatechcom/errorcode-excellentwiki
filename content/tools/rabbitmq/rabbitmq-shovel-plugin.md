---
title: "[Solution] RabbitMQ Shovel Plugin Error"
description: "Fix RabbitMQ shovel plugin error. Resolve shovel plugin configuration issues."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ Shovel Plugin Error

The shovel plugin encounters errors during configuration or operation.

## Common Causes

- Shovel plugin configuration is invalid
- Shovel source or destination unreachable
- Shovel parameters are wrong

## How to Fix

### Solution 1

```bash
rabbitmqctl Shovel.status
```

## Related Pages

- [RabbitMQ Connection Error]({{< relref "/tools/rabbitmq/rabbitmq-connection-error" >}})
- [RabbitMQ Queue Error]({{< relref "/tools/rabbitmq/rabbitmq-queue-error" >}})
- [RabbitMQ Exchange Error]({{< relref "/tools/rabbitmq/rabbitmq-exchange-error" >}})
