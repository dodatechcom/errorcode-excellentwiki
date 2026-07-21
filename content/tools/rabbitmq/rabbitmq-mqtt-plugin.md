---
title: "[Solution] RabbitMQ MQTT Plugin Error"
description: "Fix RabbitMQ MQTT plugin error. Resolve MQTT protocol support issues."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ MQTT Plugin Error

The MQTT plugin fails to handle MQTT connections. MQTT clients cannot connect or subscribe.

## Common Causes

- MQTT plugin not enabled
- MQTT port 1883 not listening
- MQTT protocol version issue

## How to Fix

### Solution 1

```bash
rabbitmq-plugins list | grep mqtt
```

### Solution 2

```bash
ss -tlnp | grep 1883
```

## Related Pages

- [RabbitMQ Connection Error]({{< relref "/tools/rabbitmq/rabbitmq-connection-error" >}})
- [RabbitMQ Queue Error]({{< relref "/tools/rabbitmq/rabbitmq-queue-error" >}})
- [RabbitMQ Exchange Error]({{< relref "/tools/rabbitmq/rabbitmq-exchange-error" >}})
