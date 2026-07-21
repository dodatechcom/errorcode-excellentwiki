---
title: "[Solution] RabbitMQ Connection Forced Close Error"
description: "Fix RabbitMQ connection forced close error. Resolve broker-initiated connection closures."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ Connection Forced Close Error

The broker forcibly closes a connection. This may be due to protocol errors, idle timeout, or policy.

## Common Causes

- Heartbeat timeout exceeded
- Protocol violation detected
- Connection was idle too long

## How to Fix

### Solution 1

```bash
grep heartbeat /etc/rabbitmq/rabbitmq.conf
```

## Related Pages

- [RabbitMQ Connection Error]({{< relref "/tools/rabbitmq/rabbitmq-connection-error" >}})
- [RabbitMQ Queue Error]({{< relref "/tools/rabbitmq/rabbitmq-queue-error" >}})
- [RabbitMQ Exchange Error]({{< relref "/tools/rabbitmq/rabbitmq-exchange-error" >}})
