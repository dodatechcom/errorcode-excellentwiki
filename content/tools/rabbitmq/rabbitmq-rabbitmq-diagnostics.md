---
title: "[Solution] RabbitMQ rabbitmq-diagnostics Error"
description: "Fix RabbitMQ rabbitmq-diagnostics error. Resolve diagnostics tool issues."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ rabbitmq-diagnostics Error

The rabbitmq-diagnostics command fails. The diagnostics cannot connect to the node.

## Common Causes

- Node is not running
- Diagnostics port is not accessible
- Erlang cookie mismatch

## How to Fix

### Solution 1

```bash
rabbitmq-diagnostics check_running
```

## Related Pages

- [RabbitMQ Connection Error]({{< relref "/tools/rabbitmq/rabbitmq-connection-error" >}})
- [RabbitMQ Queue Error]({{< relref "/tools/rabbitmq/rabbitmq-queue-error" >}})
- [RabbitMQ Exchange Error]({{< relref "/tools/rabbitmq/rabbitmq-exchange-error" >}})
