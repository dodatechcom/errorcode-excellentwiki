---
title: "[Solution] Kafka Consumer Deserialization Error"
description: "Fix Kafka consumer deserialization errors. Resolve failures when consumers cannot deserialize message keys or values."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka Consumer Deserialization Error

Kafka consumer deserialization errors occur when the deserializer class cannot parse the binary data in a message into the expected type.

## Common Causes

- Schema evolution breaking backward compatibility
- Producer sending data with a different serializer than the consumer expects
- Corrupted message data in the topic
- Avro schema registry returning incompatible schema

## How to Fix

1. Verify the deserializer class matches the producer:

```properties
key.deserializer=org.apache.kafka.common.serialization.StringDeserializer
value.deserializer=org.apache.kafka.common.serialization.StringDeserializer
```

2. For Avro consumers, check schema compatibility:

```bash
curl -X GET "localhost:8081/subjects/my-topic-value/versions/latest"
```

3. Use a dead letter queue to handle deserialization failures:

```properties
errors.deserialization.handler=org.apache.kafka.streams.errors.LogAndContinueExceptionHandler
```

4. Test deserialization manually:

```java
Deserializer<String> deserializer = new StringDeserializer();
String value = deserializer.deserialize("my-topic", record.value());
```

## Examples

```bash
# Read raw messages to inspect format
kafka-console-consumer.sh --bootstrap-server localhost:9092 \
  --topic my-topic --from-beginning --property print.value=true \
  --max-messages 5
```
