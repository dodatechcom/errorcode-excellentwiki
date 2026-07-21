---
title: "[Solution] RabbitMQ Static Shovel Error"
description: "Fix RabbitMQ static shovel errors. Resolve issues with statically configured shovels failing to transfer messages."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ Static Shovel Error

RabbitMQ static shovel errors occur when a statically configured shovel fails to connect to the source or destination broker and cannot transfer messages.

## Common Causes

- Source or destination broker is unreachable
- AMQP credentials in the shovel definition are incorrect
- SSL/TLS configuration mismatch between brokers
- Queue or exchange declared in the shovel definition does not exist

## How to Fix It

### Solution 1: Check shovel status

Monitor shovel status:

```bash
rabbitmqctl list_shovels
```

### Solution 2: Define a static shovel via configuration

Add to rabbitmq.conf:

```ini
shovels.my-shovel.src-protocol = amqp091
shovels.my-shovel.src-uri = amqp://user:pass@source-host:5672
shovels.my-shovel.src-queue = source-queue
shovels.my-shovel.dest-protocol = amqp091
shovels.my-shovel.dest-uri = amqp://user:pass@dest-host:5672
shovels.my-shovel.dest-queue = dest-queue
```

### Solution 3: Restart the shovel

Reset and restart the shovel:

```bash
rabbitmqctl eval 'rabbit_shovel:stop_shovel("my-shovel").'
rabbitmqctl eval 'rabbit_shovel:start_shovel("my-shovel").'
```

## Prevent It

- Monitor shovel status continuously
- Ensure both brokers have the required queues declared
- Test connectivity before configuring the shovel
