---
title: "[Solution] spring Kafka Producer Error"
description: "Kafka producer not sending."
frameworks: ["spring"]
error-types: ["framework-error"]
severities: ["error"]
---

Kafka producer not sending.

## Common Causes

Wrong serializer.

## How to Fix

Configure producer.

## Example

```java
@Autowired private KafkaTemplate<String, String> template;
template.send("my-topic", "key", "message");
```
