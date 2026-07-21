---
title: "[Solution] RabbitMQ Immediate Flag Error"
description: "Fix RabbitMQ immediate flag error. Resolve immediate delivery issues."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ Immediate Flag Error

Messages published with immediate flag are returned because no consumer is ready to receive them.

## Common Causes

- No consumer available on target queue
- All consumers are busy
- Queue is empty and no consumer waiting

## How to Fix

### Solution 1

```bash
rabbitmqctl list_consumers
```

## Related Pages

- [RabbitMQ Connection Error]({{< relref "/tools/rabbitmq/rabbitmq-connection-error" >}})
- [RabbitMQ Queue Error]({{< relref "/tools/rabbitmq/rabbitmq-queue-error" >}})
- [RabbitMQ Exchange Error]({{< relref "/tools/rabbitmq/rabbitmq-exchange-error" >}})
