---
title: "[Solution] RabbitMQ Connection Refused Error"
description: "Fix RabbitMQ connection refused error. Resolve TCP connection issues to the broker."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ Connection Refused Error

The client cannot connect to the RabbitMQ broker. The connection is actively refused by the server.

## Common Causes

- RabbitMQ service is not running
- RabbitMQ is not listening on the expected port
- Firewall is blocking the connection

## How to Fix

### Solution 1

```bash
rabbitmqctl status
```

### Solution 2

```bash
ss -tlnp | grep 5672
```

### Solution 3

```bash
sudo systemctl start rabbitmq-server
```

## Related Pages

- [RabbitMQ Connection Error]({{< relref "/tools/rabbitmq/rabbitmq-connection-error" >}})
- [RabbitMQ Queue Error]({{< relref "/tools/rabbitmq/rabbitmq-queue-error" >}})
- [RabbitMQ Exchange Error]({{< relref "/tools/rabbitmq/rabbitmq-exchange-error" >}})
