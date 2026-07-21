---
title: "[Solution] Kafka Deprecated Admin API Error"
description: "Fix Kafka deprecated admin API errors. Migrate from old AdminClient to the new KafkaAdminClient methods."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka Deprecated Admin API Error

Kafka deprecated admin API errors occur when using removed or deprecated AdminClient methods that are no longer available in newer Kafka client versions.

## Common Causes

- Application using Kafka client libraries from an older major version
- Direct usage of deprecated AdminClient.create() method
- Removed API methods like createAcls replaced by new equivalents
- Mixing different client library versions in the same application

## How to Fix

1. Update the Kafka client dependency to the latest version:

```xml
<dependency>
  <groupId>org.apache.kafka</groupId>
  <artifactId>kafka-clients</artifactId>
  <version>3.7.0</version>
</dependency>
```

2. Replace deprecated AdminClient creation:

```java
// Old (deprecated)
AdminClient client = AdminClient.create(props);

// New
try (AdminClient client = AdminClient.create(props)) {
    // operations
}
```

3. Use the new listOffsets API:

```java
Map<TopicPartition, OffsetSpec> offsets = Map.of(
    new TopicPartition("my-topic", 0), OffsetSpec.latest()
);
Map<TopicPartition, ListOffsetsResult.Info> result =
    admin.listOffsets(offsets).all().get();
```

## Examples

```bash
# Check client version
kafka-broker-api-versions.sh --bootstrap-server localhost:9092 | head -1
```
