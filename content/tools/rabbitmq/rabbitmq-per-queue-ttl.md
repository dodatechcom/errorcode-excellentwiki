---
title: "[Solution] RabbitMQ Per-Queue TTL Error"
description: "Fix RabbitMQ per-queue TTL error. Resolve queue time-to-live issues."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ Per-Queue TTL Error

Messages in the queue expire before being consumed. The TTL is set too low.

## Common Causes

- x-message-ttl is set too short
- Messages expire before consumers process them
- TTL value in ms is too small

## How to Fix

### Solution 1

```bash
rabbitmqadmin declare queue name=myqueue arguments='{"x-message-ttl":86400000}'
```

## Related Pages

- [RabbitMQ Connection Error]({{< relref "/tools/rabbitmq/rabbitmq-connection-error" >}})
- [RabbitMQ Queue Error]({{< relref "/tools/rabbitmq/rabbitmq-queue-error" >}})
- [RabbitMQ Exchange Error]({{< relref "/tools/rabbitmq/rabbitmq-exchange-error" >}})
