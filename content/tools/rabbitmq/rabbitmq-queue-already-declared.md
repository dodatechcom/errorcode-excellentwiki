---
title: "[Solution] RabbitMQ Queue Already Declared Error"
description: "Fix RabbitMQ queue already declared error. Resolve duplicate queue declaration issues."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ Queue Already Declared Error

The queue is already declared with incompatible properties by another connection.

## Common Causes

- Another connection declared with different properties
- Auto-delete or exclusive settings conflict
- Arguments do not match

## How to Fix

### Solution 1

```bash
rabbitmqctl list_queues name arguments
```

## Related Pages

- [RabbitMQ Connection Error]({{< relref "/tools/rabbitmq/rabbitmq-connection-error" >}})
- [RabbitMQ Queue Error]({{< relref "/tools/rabbitmq/rabbitmq-queue-error" >}})
- [RabbitMQ Exchange Error]({{< relref "/tools/rabbitmq/rabbitmq-exchange-error" >}})
