---
title: "[Solution] Kafka Broker Connection Refused Error"
description: "Fix Kafka broker connection refused error. Resolve TCP connection issues to brokers."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka Broker Connection Refused Error

The client cannot establish a TCP connection to the broker. The broker may be down, the port is wrong, or a firewall is blocking the connection.

## Common Causes

- Broker is not running
- Wrong port number
- Firewall blocks the port

## How to Fix

### Solution 1

```bash
jps -l | grep Kafka
```

### Solution 2

```bash
ss -tlnp | grep 9092
```

## Related Pages

- [Kafka Broker Error]({{< relref "/tools/kafka/kafka-broker-error" >}})
- [Kafka Topic Error]({{< relref "/tools/kafka/kafka-topic-error" >}})
- [Kafka Consumer Error]({{< relref "/tools/kafka/kafka-consumer-error" >}})
- [Kafka Producer Error]({{< relref "/tools/kafka/kafka-producer-error" >}})
