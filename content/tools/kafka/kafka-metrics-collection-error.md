---
title: "[Solution] Kafka Metrics Collection Error"
description: "Fix Kafka metrics collection errors. Resolve JMX metrics exporter failures and missing broker metrics."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka Metrics Collection Error

Kafka metrics collection errors occur when the JMX exporter or monitoring agent fails to scrape metrics from the broker, causing gaps in monitoring dashboards.

## Common Causes

- JMX port not enabled or not accessible remotely
- JMX exporter configuration referencing non-existent MBeans
- Firewall blocking JMX port (9999) from monitoring server
- Broker JVM running out of heap for JMX notifications

## How to Fix

1. Enable JMX in the broker startup script:

```bash
export KAFKA_JMX_OPTS="-Dcom.sun.management.jmxremote \
  -Dcom.sun.management.jmxremote.port=9999 \
  -Dcom.sun.management.jmxremote.authenticate=false \
  -Dcom.sun.management.jmxremote.ssl=false"
```

2. Test JMX connectivity:

```bash
java -jar jmxterm.jar -l localhost:9999
> domain kafka.server
> bean kafka.server:type=BrokerTopicMetrics,name=MessagesInPerSec
> get -i Count
```

3. Verify the JMX exporter configuration:

```bash
# Check the exporter YAML config
cat /etc/kafka/jmx_exporter_config.yml
```

4. Restart the broker with JMX enabled:

```bash
kafka-server-stop.sh
kafka-server-start.sh -daemon /etc/kafka/server.properties
```

## Examples

```bash
# Quick JMX test with jmxterm
java -jar jmxterm.jar -l localhost:9999 -n -c <<EOF
domain kafka.server
bean kafka.server:type=BrokerTopicMetrics,name=BytesInPerSec
get -i Count
EOF
```
