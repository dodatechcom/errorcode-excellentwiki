---
title: "[Solution] RabbitMQ Node Health Check Error"
description: "Fix RabbitMQ node health check error. Resolve health monitoring issues."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ Node Health Check Error

The node health check fails. The node is not responding or is in a degraded state.

## Common Causes

- Node is overloaded
- Mnesia is not running
- Node is partitioned from cluster

## How to Fix

### Solution 1

```bash
rabbitmq-diagnostics check_running
```

## Related Pages

- [RabbitMQ Connection Error]({{< relref "/tools/rabbitmq/rabbitmq-connection-error" >}})
- [RabbitMQ Queue Error]({{< relref "/tools/rabbitmq/rabbitmq-queue-error" >}})
- [RabbitMQ Exchange Error]({{< relref "/tools/rabbitmq/rabbitmq-exchange-error" >}})
