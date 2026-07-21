---
title: "[Solution] RabbitMQ Cookie Mismatch Error"
description: "Fix RabbitMQ cookie mismatch error. Resolve Erlang cookie authentication issues."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ Cookie Mismatch Error

Nodes cannot join the cluster because their Erlang cookies do not match.

## Common Causes

- Erlang cookie file is different on each node
- Cookie changed after cluster formation
- Cookie file has wrong permissions

## How to Fix

### Solution 1

```bash
cat /var/lib/rabbitmq/.erlang.cookie
```

### Solution 2

```bash
ls -la /var/lib/rabbitmq/.erlang.cookie
```

## Related Pages

- [RabbitMQ Connection Error]({{< relref "/tools/rabbitmq/rabbitmq-connection-error" >}})
- [RabbitMQ Queue Error]({{< relref "/tools/rabbitmq/rabbitmq-queue-error" >}})
- [RabbitMQ Exchange Error]({{< relref "/tools/rabbitmq/rabbitmq-exchange-error" >}})
