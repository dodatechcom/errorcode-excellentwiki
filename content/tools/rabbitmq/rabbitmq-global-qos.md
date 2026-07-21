---
title: "[Solution] RabbitMQ Global QoS Error"
description: "Fix RabbitMQ global QoS error. Resolve global prefetch limit issues."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ Global QoS Error

The global QoS setting affects all consumers on the connection. Some consumers are starved.

## Common Causes

- Global QoS is too restrictive
- Multiple consumers share global prefetch
- QoS scope is connection instead of channel

## How to Fix

### Solution 1

```bash
rabbitmqctl list_consumers
```

## Related Pages

- [RabbitMQ Connection Error]({{< relref "/tools/rabbitmq/rabbitmq-connection-error" >}})
- [RabbitMQ Queue Error]({{< relref "/tools/rabbitmq/rabbitmq-queue-error" >}})
- [RabbitMQ Exchange Error]({{< relref "/tools/rabbitmq/rabbitmq-exchange-error" >}})
