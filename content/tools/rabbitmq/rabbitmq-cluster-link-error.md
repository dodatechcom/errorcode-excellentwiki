---
title: "[Solution] RabbitMQ Cluster Link Error"
description: "Fix RabbitMQ cluster link error. Resolve inter-node communication issues."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ Cluster Link Error

Nodes cannot communicate with each other over the Erlang distribution protocol.

## Common Causes

- Network connectivity between nodes broken
- Firewall blocking Erlang ports
- Erlang distribution cookie is wrong

## How to Fix

### Solution 1

```bash
ping node2
```

### Solution 2

```bash
nc -zv node2 4369
```

### Solution 3

```bash
nc -zv node2 25672
```

## Related Pages

- [RabbitMQ Connection Error]({{< relref "/tools/rabbitmq/rabbitmq-connection-error" >}})
- [RabbitMQ Queue Error]({{< relref "/tools/rabbitmq/rabbitmq-queue-error" >}})
- [RabbitMQ Exchange Error]({{< relref "/tools/rabbitmq/rabbitmq-exchange-error" >}})
