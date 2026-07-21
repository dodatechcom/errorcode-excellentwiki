---
title: "[Solution] RabbitMQ STOMP Frame Error"
description: "Fix RabbitMQ STOMP frame errors. Resolve invalid STOMP protocol frames causing connection drops."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ STOMP Frame Error

RabbitMQ STOMP frame errors occur when the broker receives a malformed STOMP frame from a client, causing the connection to be terminated.

## Common Causes

- Missing null byte terminator in the STOMP frame body
- Invalid STOMP command or header syntax
- Content-Length header does not match actual body length
- Client sending binary data without the correct encoding

## How to Fix It

### Solution 1: Validate STOMP frame format

Ensure frames follow the STOMP 1.2 spec:

```
CONNECT
accept-version:1.2
host:/

^@
```

### Solution 2: Enable the STOMP plugin

Enable the STOMP adapter:

```bash
rabbitmq-plugins enable rabbitmq_stomp
```

### Solution 3: Check STOMP connection settings

Configure the STOMP listener:

```ini
# rabbitmq.conf
stomp.default_user = guest
stomp.default_pass = guest
stomp.listeners.tcp.1 = 0.0.0.0:61613
```

## Prevent It

- Use a mature STOMP client library
- Ensure body length matches the Content-Length header
- Test STOMP connectivity before deploying clients
