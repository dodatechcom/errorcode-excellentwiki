---
title: "[Solution] RabbitMQ Exchange Declare Passive Error"
description: "Fix RabbitMQ exchange declare passive errors. Resolve issues when checking exchange existence with passive flag."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ Exchange Declare Passive Error

RabbitMQ exchange declare passive errors occur when a client tries to passively declare an exchange that does not exist on the broker, resulting in a 404 NOT_FOUND error.

## Common Causes

- Exchange was deleted after the client code was deployed
- Exchange name typo in the client declaration
- Connecting to the wrong vhost where the exchange is not defined
- Exchange declared on a different broker in a cluster

## How to Fix It

### Solution 1: Declare the exchange without passive flag

Create the exchange if it does not exist:

```bash
rabbitmqadmin declare exchange name=my-exchange type=direct durable=true
```

### Solution 2: List existing exchanges

Check what exchanges exist:

```bash
rabbitmqadmin list exchanges name type durable vhost
```

### Solution 3: Declare exchange in the application code

Use non-passive declaration to ensure existence:

```java
channel.exchangeDeclare("my-exchange", "direct", true);
```

## Prevent It

- Use non-passive declarations to ensure exchanges exist
- Declare exchanges as part of application startup
- Use infrastructure-as-code for exchange setup
