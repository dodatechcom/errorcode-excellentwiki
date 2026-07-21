---
title: "[Solution] RabbitMQ STOMP Plugin Error"
description: "Fix RabbitMQ STOMP plugin error. Resolve STOMP protocol support issues."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ STOMP Plugin Error

The STOMP plugin fails to handle STOMP connections. STOMP clients cannot connect or subscribe.

## Common Causes

- STOMP plugin not enabled
- STOMP port 61613 not listening
- STOMP frame format is invalid

## How to Fix

### Solution 1

```bash
rabbitmq-plugins list | grep stomp
```

### Solution 2

```bash
ss -tlnp | grep 61613
```

## Related Pages

- [RabbitMQ Connection Error]({{< relref "/tools/rabbitmq/rabbitmq-connection-error" >}})
- [RabbitMQ Queue Error]({{< relref "/tools/rabbitmq/rabbitmq-queue-error" >}})
- [RabbitMQ Exchange Error]({{< relref "/tools/rabbitmq/rabbitmq-exchange-error" >}})
