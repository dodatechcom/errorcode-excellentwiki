---
title: "[Solution] spring Kafka Consumer Error"
description: "Kafka consumer not receiving messages."
frameworks: ["spring"]
error-types: ["framework-error"]
severities: ["error"]
---

Kafka consumer not receiving messages.

## Common Causes

Wrong topic or group.

## How to Fix

Check topic and group config.

## Example

```java
@KafkaListener(topics = "my-topic", groupId = "my-group")
public void consume(String message) { /* handle */ }
```
