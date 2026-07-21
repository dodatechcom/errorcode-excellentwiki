---
title: "[Solution] RabbitMQ Erlang Cookie Error"
description: "Fix RabbitMQ Erlang cookie error. Resolve Erlang cookie configuration issues."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ Erlang Cookie Error

The Erlang cookie is not properly configured. Nodes cannot authenticate with each other.

## Common Causes

- Cookie file does not exist
- Cookie file has wrong content
- Cookie is not the same on all nodes

## How to Fix

### Solution 1

```bash
cat /var/lib/rabbitmq/.erlang.cookie
```

## Related Pages

- [RabbitMQ Connection Error]({{< relref "/tools/rabbitmq/rabbitmq-connection-error" >}})
- [RabbitMQ Queue Error]({{< relref "/tools/rabbitmq/rabbitmq-queue-error" >}})
- [RabbitMQ Exchange Error]({{< relref "/tools/rabbitmq/rabbitmq-exchange-error" >}})
