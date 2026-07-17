---
title: "AmqpException - AMQP connection error"
description: "Spring AMQP throws AmqpException when it cannot connect to or communicate with a RabbitMQ broker"
frameworks: ["spring"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when Spring AMQP fails to establish or maintain a connection to a RabbitMQ broker. It throws `AmqpException` with connection or channel-level details.

## Common Causes

- RabbitMQ broker is not running or unreachable
- Incorrect connection credentials (username/password)
- Virtual host (`vhost`) does not exist or access is denied
- Connection pool exhausted due to high throughput
- Network partition or firewall blocking AMQP port (5672)

## How to Fix

1. Configure connection properties in `application.yml`:

```yaml
spring:
  rabbitmq:
    host: localhost
    port: 5672
    username: guest
    password: guest
    virtual-host: /
    connection-timeout: 5000
    requested-heartbeat: 30
```

2. Add retry and connection recovery:

```java
@Bean
public CachingConnectionFactory connectionFactory() {
    CachingConnectionFactory factory = new CachingConnectionFactory("localhost");
    factory.setUsername("guest");
    factory.setPassword("guest");
    factory.setRequestedHeartBeat(30);
    factory.setConnectionTimeout(5000);
    factory.setCacheMode(CachingConnectionFactory.CacheMode.CONNECTION);
    factory.setChannelCacheSize(10);
    return factory;
}
```

3. Use `@Retryable` for message listeners:

```java
@RabbitListener(queues = "orders")
@Retryable(
    retryFor = AmqpException.class,
    maxAttempts = 3,
    backoff = @Backoff(delay = 1000)
)
public void processOrder(Order order) {
    // Process the order
}
```

## Examples

```java
// RabbitMQ not running
amqpTemplate.convertAndSend("orders", order);
// AmqpException: None of the CachingConnectionFactory channels are available
```

## Related Errors

- [Kafka error]({{< relref "/frameworks/spring/spring-kafka-concurrency-error" >}})
- [Queue error (Laravel)]({{< relref "/frameworks/laravel/laravel-queue-error" >}})
