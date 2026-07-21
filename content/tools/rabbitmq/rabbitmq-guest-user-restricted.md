---
title: "[Solution] RabbitMQ Guest User Restricted Error"
description: "Fix RabbitMQ guest user restricted error. Resolve guest user access limitations."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ Guest User Restricted Error

The guest user can only connect from localhost by default. Remote connections with guest are rejected.

## Common Causes

- Guest user trying to connect remotely
- loopback_users not configured
- Default security policy restricts guest

## How to Fix

### Solution 1

```bash
rabbitmqctl add_user myuser mypassword
```

### Solution 2

```bash
rabbitmqctl set_user_tags myuser administrator
```

### Solution 3

```bash
rabbitmqctl set_permissions -p / myuser '.*' '.*' '.*'
```

## Related Pages

- [RabbitMQ Connection Error]({{< relref "/tools/rabbitmq/rabbitmq-connection-error" >}})
- [RabbitMQ Queue Error]({{< relref "/tools/rabbitmq/rabbitmq-queue-error" >}})
- [RabbitMQ Exchange Error]({{< relref "/tools/rabbitmq/rabbitmq-exchange-error" >}})
