---
title: "[Solution] RabbitMQ Cluster Node Not Found Error"
description: "Fix RabbitMQ cluster node not found error. Resolve cluster membership issues."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ Cluster Node Not Found Error

A node referenced in the cluster is not found or not running. Cluster formation is incomplete.

## Common Causes

- Node is down or removed
- Node name mismatch in cluster config
- Erlang cookie is different across nodes

## How to Fix

### Solution 1

```bash
rabbitmqctl cluster_status
```

## Related Pages

- [RabbitMQ Connection Error]({{< relref "/tools/rabbitmq/rabbitmq-connection-error" >}})
- [RabbitMQ Queue Error]({{< relref "/tools/rabbitmq/rabbitmq-queue-error" >}})
- [RabbitMQ Exchange Error]({{< relref "/tools/rabbitmq/rabbitmq-exchange-error" >}})
