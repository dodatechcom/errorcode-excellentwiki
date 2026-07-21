---
title: "[Solution] RabbitMQ Heartbeat Timeout Error"
description: "Fix RabbitMQ heartbeat timeout error. Resolve connection keepalive issues."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ Heartbeat Timeout Error

The connection heartbeat times out. The broker or client detects a dead connection.

## Common Causes

- Heartbeat timeout is too short
- Network issues cause delayed heartbeats
- Client is too busy to send heartbeats

## How to Fix

### Solution 1

```bash
grep heartbeat /etc/rabbitmq/rabbitmq.conf
```

## Related Pages

- [RabbitMQ Connection Error]({{< relref "/tools/rabbitmq/rabbitmq-connection-error" >}})
- [RabbitMQ Queue Error]({{< relref "/tools/rabbitmq/rabbitmq-queue-error" >}})
- [RabbitMQ Exchange Error]({{< relref "/tools/rabbitmq/rabbitmq-exchange-error" >}})
