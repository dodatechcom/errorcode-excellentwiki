---
title: "[Solution] RabbitMQ Permissions Not Granted Error"
description: "Fix RabbitMQ permissions not granted error. Resolve user permission issues."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ Permissions Not Granted Error

The user does not have the required permissions on the virtual host.

## Common Causes

- User has no permissions on target vhost
- Permission regex does not match
- Configure or write permissions missing

## How to Fix

### Solution 1

```bash
rabbitmqctl list_permissions -p myvhost
```

### Solution 2

```bash
rabbitmqctl set_permissions -p myvhost myuser '.*' '.*' '.*'
```

## Related Pages

- [RabbitMQ Connection Error]({{< relref "/tools/rabbitmq/rabbitmq-connection-error" >}})
- [RabbitMQ Queue Error]({{< relref "/tools/rabbitmq/rabbitmq-queue-error" >}})
- [RabbitMQ Exchange Error]({{< relref "/tools/rabbitmq/rabbitmq-exchange-error" >}})
