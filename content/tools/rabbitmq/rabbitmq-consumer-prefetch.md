---
title: "[Solution] RabbitMQ Consumer Prefetch Error"
description: "Fix RabbitMQ consumer prefetch error. Resolve QoS prefetch configuration issues."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ Consumer Prefetch Error

The consumer prefetch (QoS) setting is causing issues. Too many or too few messages are delivered.

## Common Causes

- Prefetch count is too high causing memory issues
- Prefetch set to 0 (unlimited)
- Prefetch set on non-channel scope

## How to Fix

### Solution 1

```bash
rabbitmqctl list_consumers
```

## Related Pages

- [RabbitMQ Connection Error]({{< relref "/tools/rabbitmq/rabbitmq-connection-error" >}})
- [RabbitMQ Queue Error]({{< relref "/tools/rabbitmq/rabbitmq-queue-error" >}})
- [RabbitMQ Exchange Error]({{< relref "/tools/rabbitmq/rabbitmq-exchange-error" >}})
