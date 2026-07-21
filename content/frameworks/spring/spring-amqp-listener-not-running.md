---
title: "Spring AMQP Listener Not Running"
description: "Spring AMQP message listener container fails to start because the RabbitMQ connection factory is misconfigured or the broker is unreachable"
frameworks: ["spring"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when the Spring AMQP listener container fails to initialize and does not consume any messages from the configured RabbitMQ queue.

## Common Causes

- RabbitMQ connection factory host or port is incorrect in application.yml
- Username or password authentication fails against the RabbitMQ broker
- The target queue does not exist or was deleted between deployments
- Virtual host configuration does not match the broker's vhost setup
- TLS/SSL certificate validation fails on the AMQP connection
- Listener container maxConcurrency set to zero or negative value

## How to Fix

1. Verify your RabbitMQ connection factory configuration:

```yaml
# application.yml
spring:
  rabbitmq:
    host: localhost
    port: 5672
    username: guest
    password: guest
    virtual-host: /
    connection-timeout: 5000
```

2. Check the listener container configuration:

```java
@Configuration
public class RabbitMQConfig {
    @Bean
    public SimpleMessageListenerContainer container(
            ConnectionFactory connectionFactory,
            MessageListenerAdapter adapter) {
        SimpleMessageListenerContainer container = new SimpleMessageListenerContainer();
        container.setConnectionFactory(connectionFactory);
        container.setQueueNames("my-queue");
        container.setMessageListener(adapter);
        container.setConcurrency("1-3");
        container.setPrefetchCount(10);
        return container;
    }
}
```

3. Ensure the queue is declared with proper attributes:

```java
@Bean
public Queue myQueue() {
    return new Queue("my-queue", true, false, false);
}
```

## Examples

```java
// Common mistake: listener throws an exception without rejecting the message
@RabbitListener(queues = "my-queue")
public void handleMessage(Message message) {
    String body = new String(message.getBody());
    processMessage(body); // If this throws, the message is requeued
    // and the listener will process it again in an infinite loop
}
```

```text
org.springframework.amqp.rabbit.listener.SimpleMessageListenerContainer:
    Could not refresh AMQP connection -- Channel not open
```

## Prevention

1. Use Spring Boot Actuator health checks for RabbitMQ connectivity
2. Configure dead-letter queues for messages that repeatedly fail processing
3. Set appropriate prefetch count and concurrency to prevent consumer overload
4. Monitor RabbitMQ management UI for queue depth and consumer count
