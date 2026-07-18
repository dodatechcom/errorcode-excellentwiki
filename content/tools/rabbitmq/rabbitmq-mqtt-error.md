---
title: "[Solution] RabbitMQ MQTT Error"
description: "Fix RabbitMQ mqtt errors. Learn why this happens and how to resolve it quickly."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# RabbitMQ MQTT Error

RabbitMQ MQTT errors occur when MQTT protocol connections or message delivery fails.

## Why This Happens

- Connection refused
- Topic not subscribed
- QoS not supported
- Auth failed

## Common Error Messages

- `mqtt_connection_error`
- `mqtt_topic_error`
- `mqtt_qos_error`
- `mqtt_auth_error`

## How to Fix It

### Solution 1: Configure MQTT

Enable MQTT plugin:

```bash
rabbitmq-plugins enable rabbitmq_mqtt
```

### Solution 2: Check MQTT connection

Verify MQTT port is accessible:

```bash
nc -zv localhost 1883
```

### Solution 3: Fix auth issues

Configure MQTT authentication.


## Common Scenarios

- **Connection refused:** Check if MQTT plugin is enabled.
- **Topic not subscribed:** Verify topic subscription.

## Prevent It

- Enable MQTT plugin
- Test MQTT connection
- Monitor MQTT metrics
