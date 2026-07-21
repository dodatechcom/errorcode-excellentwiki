---
title: "[Solution] RabbitMQ Vhost Memory Limit Error"
description: "Fix RabbitMQ vhost memory limit errors. Resolve memory alarms triggered by individual vhost consumption."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ Vhost Memory Limit Error

RabbitMQ vhost memory limit errors occur when a specific vhost exceeds its configured memory limit, blocking producers in that vhost while the broker remains operational for other vhosts.

## Common Causes

- Memory limit set too low for the vhost workload
- Message consumers not keeping up with producers
- Large message bodies accumulating in queues
- Memory-intensive operations like large message routing

## How to Fix It

### Solution 1: Check vhost memory usage

Monitor per-vhost memory:

```bash
rabbitmqctl status | grep -A 5 memory
rabbitmqctl list_queues -q messages memory | head
```

### Solution 2: Increase vhost memory limit

Set a higher memory limit:

```bash
rabbitmqctl set_vhost_limits -p /myvhost '{"max-mem": 4294967296}'
```

### Solution 3: Apply memory policies to limit queue memory

Set per-queue memory limits:

```bash
rabbitmqctl set_policy max-mem-limit ".*" \
  '{"max-length-bytes": 1073741824}' \
  --apply-to queues -p /myvhost
```

## Prevent It

- Set appropriate memory limits per vhost based on workload
- Monitor per-vhost memory consumption
- Use queue TTL and max-length to bound memory usage
