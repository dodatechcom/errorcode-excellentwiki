---
title: "[Solution] RabbitMQ Overflow Behaviour Error"
description: "Fix RabbitMQ overflow behaviour error. Resolve queue overflow handling issues."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ Overflow Behaviour Error

The queue overflow behaviour is not configured as expected. Messages are dropped instead of rejected.

## Common Causes

- Overflow not set (default: drop-head)
- reject-publish needed but not configured
- Dead-lettering not configured

## How to Fix

### Solution 1

```bash
rabbitmqadmin declare queue name=myqueue arguments='{"x-max-length":1000,"x-overflow":"reject-publish"}'
```

## Related Pages

- [RabbitMQ Connection Error]({{< relref "/tools/rabbitmq/rabbitmq-connection-error" >}})
- [RabbitMQ Queue Error]({{< relref "/tools/rabbitmq/rabbitmq-queue-error" >}})
- [RabbitMQ Exchange Error]({{< relref "/tools/rabbitmq/rabbitmq-exchange-error" >}})
