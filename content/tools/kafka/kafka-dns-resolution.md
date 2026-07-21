---
title: "[Solution] Kafka DNS Resolution Error"
description: "Fix Kafka DNS resolution error. Resolve hostname lookup failures for Kafka brokers."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka DNS Resolution Error

The client cannot resolve the broker hostname. DNS configuration is incorrect or the hostname does not exist.

## Common Causes

- DNS server is not configured
- Hostname does not exist in DNS
- /etc/hosts is missing entry

## How to Fix

### Solution 1

```bash
nslookup broker-hostname
```

### Solution 2

```bash
dig broker-hostname
```

## Related Pages

- [Kafka Broker Error]({{< relref "/tools/kafka/kafka-broker-error" >}})
- [Kafka Topic Error]({{< relref "/tools/kafka/kafka-topic-error" >}})
- [Kafka Consumer Error]({{< relref "/tools/kafka/kafka-consumer-error" >}})
- [Kafka Producer Error]({{< relref "/tools/kafka/kafka-producer-error" >}})
