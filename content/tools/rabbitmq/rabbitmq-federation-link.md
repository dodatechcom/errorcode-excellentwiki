---
title: "[Solution] RabbitMQ Federation Link Error"
description: "Fix RabbitMQ federation link error. Resolve cross-node message federation issues."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ Federation Link Error

The federation link between nodes or exchanges fails. Messages are not federated.

## Common Causes

- Federation plugin not enabled
- Upstream URI is wrong
- Network connectivity to upstream broken

## How to Fix

### Solution 1

```bash
rabbitmq-plugins list | grep federation
```

### Solution 2

```bash
rabbitmqctl status
```

## Related Pages

- [RabbitMQ Connection Error]({{< relref "/tools/rabbitmq/rabbitmq-connection-error" >}})
- [RabbitMQ Queue Error]({{< relref "/tools/rabbitmq/rabbitmq-queue-error" >}})
- [RabbitMQ Exchange Error]({{< relref "/tools/rabbitmq/rabbitmq-exchange-error" >}})
