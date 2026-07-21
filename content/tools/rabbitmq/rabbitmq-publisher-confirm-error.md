---
title: "[Solution] RabbitMQ Publisher Confirm Error"
description: "Fix RabbitMQ publisher confirm error. Resolve confirm notification issues."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ Publisher Confirm Error

The publisher confirm indicates a negative acknowledgment. The message was not stored.

## Common Causes

- Broker rejected the message
- Disk alarm is active
- Memory alarm is active

## How to Fix

### Solution 1

```bash
rabbitmqctl status
```

## Related Pages

- [RabbitMQ Connection Error]({{< relref "/tools/rabbitmq/rabbitmq-connection-error" >}})
- [RabbitMQ Queue Error]({{< relref "/tools/rabbitmq/rabbitmq-queue-error" >}})
- [RabbitMQ Exchange Error]({{< relref "/tools/rabbitmq/rabbitmq-exchange-error" >}})
