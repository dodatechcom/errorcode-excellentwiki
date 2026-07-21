---
title: "[Solution] RabbitMQ AMQP Handshake Timeout Error"
description: "Fix RabbitMQ AMQP handshake timeout error. Resolve connection establishment timeout issues."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ AMQP Handshake Timeout Error

The AMQP handshake times out before completing. The client and broker fail to negotiate protocol parameters.

## Common Causes

- Network latency between client and broker
- Broker is overloaded
- Handshake timeout is too low

## How to Fix

### Solution 1

```bash
rabbitmqctl status
```

### Solution 2

```bash
netstat -an | grep 5672
```

## Related Pages

- [RabbitMQ Connection Error]({{< relref "/tools/rabbitmq/rabbitmq-connection-error" >}})
- [RabbitMQ Queue Error]({{< relref "/tools/rabbitmq/rabbitmq-queue-error" >}})
- [RabbitMQ Exchange Error]({{< relref "/tools/rabbitmq/rabbitmq-exchange-error" >}})
