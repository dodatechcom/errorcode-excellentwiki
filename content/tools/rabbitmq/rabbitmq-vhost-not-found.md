---
title: "[Solution] RabbitMQ Virtual Host Not Found Error"
description: "Fix RabbitMQ virtual host not found error. Resolve vhost reference issues."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ Virtual Host Not Found Error

The virtual host does not exist. The client is connecting to a vhost that was never created.

## Common Causes

- Virtual host was never created
- Virtual host was deleted
- Vhost name is misspelled

## How to Fix

### Solution 1

```bash
rabbitmqctl list_vhosts
```

### Solution 2

```bash
rabbitmqctl add_vhost myvhost
```

## Related Pages

- [RabbitMQ Connection Error]({{< relref "/tools/rabbitmq/rabbitmq-connection-error" >}})
- [RabbitMQ Queue Error]({{< relref "/tools/rabbitmq/rabbitmq-queue-error" >}})
- [RabbitMQ Exchange Error]({{< relref "/tools/rabbitmq/rabbitmq-exchange-error" >}})
