---
title: "[Solution] RabbitMQ Runtime Parameter Type Error"
description: "Fix RabbitMQ runtime parameter type errors. Resolve invalid parameter value types in cluster configuration."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ Runtime Parameter Type Error

RabbitMQ runtime parameter type errors occur when a runtime parameter is set with a value of the wrong type, such as passing a string where a JSON object is expected.

## Common Causes

- Using a string value instead of a JSON object for a policy
- Incorrect JSON syntax in the parameter value
- Missing required fields in the parameter definition
- Parameter value incompatible with the target component

## How to Fix It

### Solution 1: Check current parameters

View all runtime parameters:

```bash
rabbitmqctl list_parameters -p /myvhost
```

### Solution 2: Set the parameter with correct type

Use properly typed values:

```bash
rabbitmqctl set_parameter federation-upstream my-upstream \
  '{"uri": "amqp://user:pass@remote-host:5672", "prefetch-count": 1000}'
```

### Solution 3: Delete and re-create the parameter

Remove the incorrect parameter and set it again:

```bash
rabbitmqctl clear_parameter federation-upstream my-upstream -p /myvhost
rabbitmqctl set_parameter federation-upstream my-upstream \
  '{"uri": "amqp://user:pass@remote-host:5672"}' -p /myvhost
```

## Prevent It

- Validate JSON syntax before applying parameters
- Test parameters in a non-production environment first
- Use the management API to check parameter schema
