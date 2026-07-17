---
title: "[Solution] AmqpException — Spring AMQP Fix"
description: "Fix AmqpException in Spring AMQP. Resolve connection, channel, and message handling issues with RabbitMQ."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["spring", "amqp", "rabbitmq", "message-queue", "amqp-exception"]
weight: 5
---

# AmqpException — Spring AMQP Fix

An `AmqpException` is thrown when Spring AMQP encounters an error communicating with RabbitMQ. This can be a connection issue, channel error, or message handling failure.

## What This Error Means

Common messages:

- `AmqpException: None of the listed Exchanges is available for binding`
- `AmqpException: java.io.IOException`
- `AmqpException: Channel shutdown`

## Common Causes

```java
// Cause 1: Exchange or queue not declared
@RabbitListener(queues = "my-queue")
public void listen(String message) { }
// Queue "my-queue" not declared

// Cause 2: Connection lost
// RabbitMQ server restarted

// Cause 3: Message conversion error
@RabbitListener(queues = "my-queue")
public void listen(User user) { }
// Cannot convert JSON to User class
```

## How to Fix

### Fix 1: Declare queues and exchanges

```java
@Configuration
public class RabbitMQConfig {

    @Bean
    public Queue myQueue() {
        return QueueBuilder.durable("my-queue").build();
    }

    @Bean
    public DirectExchange myExchange() {
        return new DirectExchange("my-exchange");
    }

    @Bean
    public Binding binding(Queue myQueue, DirectExchange myExchange) {
        return BindingBuilder.bind(myQueue).to(myExchange).with("routing-key");
    }
}
```

### Fix 2: Configure connection recovery

```java
@Bean
public CachingConnectionFactory connectionFactory() {
    CachingConnectionFactory factory = new CachingConnectionFactory("localhost");
    factory.setRequestedHeartBeat(30);
    factory.setConnectionTimeout(10000);
    factory.setCacheMode(CachingConnectionFactory.CacheMode.CHANNEL);
    factory.setChannelCacheSize(10);
    return factory;
}
```

### Fix 3: Add error handler

```java
@Bean
public RabbitListenerContainerFactory<?> rabbitListenerContainerFactory(
        ConnectionFactory connectionFactory) {
    SimpleRabbitListenerContainerFactory factory = new SimpleRabbitListenerContainerFactory();
    factory.setConnectionFactory(connectionFactory);
    factory.setDefaultRequeueRejected(false);
    factory.setAdviceChain(
        RetryInterceptorBuilder.stateless()
            .retryPolicy(new SimpleRetryPolicy(3))
            .backOffOptions(1000, 2.0, 10000)
            .build());
    return factory;
}
```

## Related Errors

- {{< relref "spring-kafka-concurrency" >}} — IllegalContainerGroupIdException
- {{< relref "kafka-consumer" >}} — CommitFailedException
- {{< relref "testcontainers-rabbitmq" >}} — RabbitMQContainer startup failed
