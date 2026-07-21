---
title: "[Solution] RabbitMQ Message Store Error"
description: "Fix RabbitMQ message store errors. Resolve internal message store corruption and recovery failures."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ Message Store Error

RabbitMQ message store errors occur when the internal persistent message store becomes corrupted or cannot read messages from disk, preventing queue recovery after a restart.

## Common Causes

- Unclean shutdown during a large message persistence operation
- Disk failure affecting the message store directory
- Insufficient disk space during message persistence
- Erlang process crash during message store compaction

## How to Fix It

### Solution 1: Check the message store directory

Inspect the message store files:

```bash
ls -la /var/lib/rabbitmq/mnesia/rabbit@node/msg_store_persistent/
```

### Solution 2: Force recovery on startup

Enable message store recovery:

```bash
rabbitmq-server -rabbit msg_store_type {dets, []}
```

### Solution 3: Reset the node if recovery fails

Last resort -- reset the node (data loss):

```bash
rabbitmqctl stop_app
rabbitmqctl reset
rabbitmqctl start_app
```

## Prevent It

- Ensure sufficient disk space at all times
- Use at least 3 nodes for cluster resilience
- Monitor disk I/O on the message store volume
