---
title: "[Solution] Spring RabbitMQ Error"
description: "Fix Spring RabbitMQ errors when message publishing or consumption fails due to configuration or connection issues."
frameworks: ["spring"]
error-types: ["connection-error"]
severities: ["error"]
---

RabbitMQ errors in Spring occur when the broker is unreachable, queue configuration is wrong, or message serialization fails.

## Common Causes

- RabbitMQ server not running
- Connection URL or credentials incorrect
- Queue or exchange not declared
- Message serialization format incompatible
- Consumer not properly configured

## How to Fix

### Configure RabbitMQ

```yaml
# application.yml
spring:
  rabbitmq:
    host: localhost
    port: 5672
    username: guest
    password: guest
    virtual-host: /
```

### Configure Queue and Exchange

```java
@Configuration
public class RabbitMQConfig {
    public static final String QUEUE_NAME = "orders";
    public static final String EXCHANGE_NAME = "order.exchange";
    public static final String ROUTING_KEY = "order.new";

    @Bean
    public Queue ordersQueue() {
        return new Queue(QUEUE_NAME, true);
    }

    @Bean
    public TopicExchange exchange() {
        return new TopicExchange(EXCHANGE_NAME);
    }

    @Bean
    public Binding binding(Queue ordersQueue, TopicExchange exchange) {
        return BindingBuilder.bind(ordersQueue).to(exchange).with(ROUTING_KEY);
    }
}
```

### Publish and Consume Messages

```java
@Service
public class OrderService {
    @Autowired
    private RabbitTemplate rabbitTemplate;

    public void publishOrder(Order order) {
        rabbitTemplate.convertAndSend(EXCHANGE_NAME, ROUTING_KEY, order);
    }
}

@Component
@RabbitListener(queues = "orders")
public class OrderConsumer {
    @RabbitHandler
    public void handleOrder(Order order) {
        // Process order
    }
}
```

### Handle Connection Errors

```java
@Configuration
public class RabbitMQConfig {
    @Bean
    public ConnectionFactory connectionFactory() {
        CachingConnectionFactory factory = new CachingConnectionFactory("localhost");
        factory.setUsername("guest");
        factory.setPassword("guest");
        factory.setRequestedHeartBeat(30);
        factory.setConnectionTimeout(10000);
        return factory;
    }
}
```

## Examples

```yaml
# Bug -- wrong host
spring:
  rabbitmq:
    host: wrong-host  # Connection refused

# Fix -- correct host
spring:
  rabbitmq:
    host: localhost
```
