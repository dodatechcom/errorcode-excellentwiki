---
title: "[Solution] RabbitMQ User Not Found Error"
description: "Fix RabbitMQ user not found error. Resolve user existence issues."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ User Not Found Error

The specified user does not exist in RabbitMQ. The user may have been deleted or was never created.

## Common Causes

- User was never created
- User was deleted
- Username is misspelled

## How to Fix

### Solution 1

```bash
rabbitmqctl list_users
```

### Solution 2

```bash
rabbitmqctl add_user myuser mypassword
```

## Related Pages

- [RabbitMQ Connection Error]({{< relref "/tools/rabbitmq/rabbitmq-connection-error" >}})
- [RabbitMQ Queue Error]({{< relref "/tools/rabbitmq/rabbitmq-queue-error" >}})
- [RabbitMQ Exchange Error]({{< relref "/tools/rabbitmq/rabbitmq-exchange-error" >}})
