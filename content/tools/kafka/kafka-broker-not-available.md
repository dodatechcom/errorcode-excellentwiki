---
title: "[Solution] Kafka Broker Not Available Error"
description: "Fix Kafka broker not available error. Resolve broker connectivity issues in Apache Kafka clusters."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka Broker Not Available Error

The Kafka broker is not reachable. Clients receive broker not available when the broker process is down, the listener is misconfigured, or network connectivity is broken.

## Common Causes

- The broker process is not running
- Listener configuration is wrong in server.properties
- Firewall blocks the listener port

## How to Fix

### Solution 1

```bash
kafka-broker-api-versions.sh --bootstrap-server localhost:9092
```

### Solution 2

```bash
grep '^listeners' /etc/kafka/server.properties
```

### Solution 3

```bash
telnet broker-host 9092
```

## Related Pages

- [Kafka Broker Error]({{< relref "/tools/kafka/kafka-broker-error" >}})
- [Kafka Topic Error]({{< relref "/tools/kafka/kafka-topic-error" >}})
- [Kafka Consumer Error]({{< relref "/tools/kafka/kafka-consumer-error" >}})
- [Kafka Producer Error]({{< relref "/tools/kafka/kafka-producer-error" >}})
