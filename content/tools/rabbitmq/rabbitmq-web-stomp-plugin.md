---
title: "[Solution] RabbitMQ Web STOMP Plugin Error"
description: "Fix RabbitMQ Web STOMP plugin error. Resolve WebSocket-based STOMP issues."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ Web STOMP Plugin Error

The Web STOMP plugin fails. WebSocket-based STOMP connections are not working.

## Common Causes

- Web STOMP plugin not enabled
- WebSocket port not listening
- Web STOMP handler is misconfigured

## How to Fix

### Solution 1

```bash
rabbitmq-plugins list | grep web_stomp
```

## Related Pages

- [RabbitMQ Connection Error]({{< relref "/tools/rabbitmq/rabbitmq-connection-error" >}})
- [RabbitMQ Queue Error]({{< relref "/tools/rabbitmq/rabbitmq-queue-error" >}})
- [RabbitMQ Exchange Error]({{< relref "/tools/rabbitmq/rabbitmq-exchange-error" >}})
