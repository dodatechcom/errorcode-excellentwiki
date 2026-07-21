---
title: "[Solution] Spring Kafka Error"
description: "Fix Spring Kafka errors when message production or consumption fails due to broker or configuration issues."
frameworks: ["spring"]
error-types: ["connection-error"]
severities: ["error"]
---

Kafka errors in Spring occur when the broker is unavailable, topic configuration is wrong, or consumer group settings are incorrect.

## Common Causes

- Kafka broker not running
- Bootstrap server URL incorrect
- Topic does not exist and auto-create is disabled
- Consumer group ID not configured
- Deserialization failure for message key/value

## How to Fix

### Configure Kafka Producer

```java
@Configuration
public class KafkaProducerConfig {
    @Bean
    public ProducerFactory<String, String> producerFactory() {
        Map<String, Object> config = new HashMap<>();
        config.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
        config.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class);
        config.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, JsonSerializer.class);
        return new DefaultKafkaProducerFactory<>(config);
    }

    @Bean
    public KafkaTemplate<String, String> kafkaTemplate() {
        return new KafkaTemplate<>(producerFactory());
    }
}
```

### Configure Kafka Consumer

```java
@Configuration
public class KafkaConsumerConfig {
    @Bean
    public ConsumerFactory<String, String> consumerFactory() {
        Map<String, Object> config = new HashMap<>();
        config.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
        config.put(ConsumerConfig.GROUP_ID_CONFIG, "my-group");
        config.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class);
        config.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, JsonDeserializer.class);
        return new DefaultKafkaConsumerFactory<>(config);
    }

    @Bean
    public ConcurrentKafkaListenerContainerFactory<String, String> kafkaListenerContainerFactory() {
        ConcurrentKafkaListenerContainerFactory<String, String> factory =
            new ConcurrentKafkaListenerContainerFactory<>();
        factory.setConsumerFactory(consumerFactory());
        return factory;
    }
}
```

### Handle Consumer Errors

```java
@Component
public class KafkaConsumer {
    @KafkaListener(topics = "orders", groupId = "order-processor")
    public void consume(ConsumerRecord<String, String> record) {
        try {
            // Process message
            log.info("Received: {}", record.value());
        } catch (Exception e) {
            log.error("Failed to process message: {}", record.value(), e);
        }
    }
}
```

## Examples

```java
// Bug -- no error handling
@KafkaListener(topics = "orders")
public void consume(String message) {
    processMessage(message);  // May throw exception
}

// Fix -- add error handling
@KafkaListener(topics = "orders")
public void consumeSafe(String message) {
    try {
        processMessage(message);
    } catch (Exception e) {
        log.error("Failed to process: {}", message, e);
    }
}
```
