---
title: "[Solution] RabbitMQ Login Refused Error"
description: "Fix RabbitMQ login refused error. Resolve authentication refusal issues."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ Login Refused Error

The broker refuses the login attempt. The user is not authorized or the account is locked.

## Common Causes

- User account is disabled
- User not allowed from this IP
- SASL mechanism not supported

## How to Fix

### Solution 1

```bash
rabbitmqctl list_users
```

### Solution 2

```bash
rabbitmqctl set_user_tags myuser administrator
```

## Related Pages

- [RabbitMQ Connection Error]({{< relref "/tools/rabbitmq/rabbitmq-connection-error" >}})
- [RabbitMQ Queue Error]({{< relref "/tools/rabbitmq/rabbitmq-queue-error" >}})
- [RabbitMQ Exchange Error]({{< relref "/tools/rabbitmq/rabbitmq-exchange-error" >}})
